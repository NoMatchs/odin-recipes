require('dotenv').config();
const express = require('express');
const cors = require('cors');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const sqlite3 = require('sqlite3').verbose();
const { promisify } = require('util');

const app = express();
app.use(cors());
app.use(express.json());

// ---------- 1. 连接 SQLite 数据库 ----------
const db = new sqlite3.Database('./habit.db', (err) => {
  if (err) {
    console.log('❌ 数据库连接失败', err);
  } else {
    console.log('✅ SQLite 数据库连接成功');
  }
});

// 把 db 的方法转成 Promise，方便用 async/await
const dbRun = promisify(db.run.bind(db));
const dbGet = promisify(db.get.bind(db));
const dbAll = promisify(db.all.bind(db));

// ---------- 2. 创建数据表（相当于 MongoDB 的 Collection） ----------
async function initTables() {
  // 用户表
  await dbRun(`
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT UNIQUE NOT NULL,
      password TEXT NOT NULL,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
  `);

  // 打卡记录表
  await dbRun(`
    CREATE TABLE IF NOT EXISTS checkins (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id INTEGER NOT NULL,
      habit_type TEXT NOT NULL,
      score INTEGER DEFAULT 1,
      note TEXT,
      date DATE NOT NULL,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (user_id) REFERENCES users (id)
    )
  `);

  // 为了查询性能，加上索引
  await dbRun(`CREATE INDEX IF NOT EXISTS idx_checkins_user_date ON checkins(user_id, date)`);
  await dbRun(`CREATE INDEX IF NOT EXISTS idx_checkins_user_habit ON checkins(user_id, habit_type)`);
  
  console.log('✅ 数据表初始化完成');
}

initTables().catch(err => console.log('❌ 建表失败', err));

// ---------- 3. 辅助函数：把日期转成 YYYY-MM-DD 格式 ----------
function getTodayStr() {
  const d = new Date();
  const year = d.getFullYear();
  const month = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

// ---------- 4. 验证登录的中间件 ----------
const authMiddleware = async (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ msg: '请先登录' });
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.userId = decoded.userId;
    next();
  } catch {
    res.status(401).json({ msg: 'token无效或已过期' });
  }
};

// ---------- 5. 注册 ----------
app.post('/api/register', async (req, res) => {
  const { username, password } = req.body;
  if (!username || !password) {
    return res.status(400).json({ msg: '用户名和密码不能为空' });
  }

  try {
    // 检查用户名是否已存在
    const exist = await dbGet('SELECT id FROM users WHERE username = ?', [username]);
    if (exist) {
      return res.status(400).json({ msg: '用户名已存在' });
    }

    const hashed = await bcrypt.hash(password, 10);
    
    // 改用 db.run 直接执行，并手动获取 lastID
    const result = await new Promise((resolve, reject) => {
      db.run(
        'INSERT INTO users (username, password) VALUES (?, ?)',
        [username, hashed],
        function(err) {
          if (err) reject(err);
          else resolve({ lastID: this.lastID });
        }
      );
    });
    
    res.json({ msg: '注册成功', userId: result.lastID });
  } catch (err) {
    res.status(500).json({ msg: '注册失败', error: err.message });
  }
});
// ---------- 6. 登录 ----------
app.post('/api/login', async (req, res) => {
  const { username, password } = req.body;
  try {
    const user = await dbGet('SELECT * FROM users WHERE username = ?', [username]);
    if (!user) {
      return res.status(400).json({ msg: '用户不存在' });
    }

    const ok = await bcrypt.compare(password, user.password);
    if (!ok) {
      return res.status(400).json({ msg: '密码错误' });
    }

    const token = jwt.sign({ userId: user.id }, process.env.JWT_SECRET, { expiresIn: '7d' });
    res.json({ msg: '登录成功', token, userId: user.id });
  } catch (err) {
    res.status(500).json({ msg: '登录失败', error: err.message });
  }
});

// ---------- 7. 打卡 ----------
app.post('/api/checkin', authMiddleware, async (req, res) => {
  const { habitType, score, note } = req.body;
  if (!habitType) {
    return res.status(400).json({ msg: '请指定习惯类型' });
  }

  try {
    const today = getTodayStr();
    
    // 检查今天是否已经打过卡
    const exist = await dbGet(
      'SELECT id FROM checkins WHERE user_id = ? AND habit_type = ? AND date = ?',
      [req.userId, habitType, today]
    );
    if (exist) {
      return res.status(400).json({ msg: '今天已打卡，明天再来吧' });
    }

    // 改用 db.run 直接执行，并手动获取 lastID
    const result = await new Promise((resolve, reject) => {
      db.run(
        'INSERT INTO checkins (user_id, habit_type, score, note, date) VALUES (?, ?, ?, ?, ?)',
        [req.userId, habitType, score || 1, note || '', today],
        function(err) {
          if (err) reject(err);
          else resolve({ lastID: this.lastID });
        }
      );
    });

    // 查询刚插入的记录返回
    const newRecord = await dbGet(
      'SELECT * FROM checkins WHERE id = ?',
      [result.lastID]
    );
    res.json({ msg: '打卡成功 ✅', checkin: newRecord });
  } catch (err) {
    res.status(500).json({ msg: '打卡失败', error: err.message });
  }
});
// ---------- 8. 统计数据 ----------
app.get('/api/stats', authMiddleware, async (req, res) => {
  const { habitType } = req.query;
  if (!habitType) {
    return res.status(400).json({ msg: '请指定习惯类型' });
  }

  try {
    // 获取最近30天的数据
    const records = await dbAll(
      `SELECT date, score, COUNT(*) as count 
       FROM checkins 
       WHERE user_id = ? AND habit_type = ? AND date >= date('now', '-30 days')
       GROUP BY date
       ORDER BY date ASC`,
      [req.userId, habitType]
    );

    // 把数据转成前端好用的格式
    const stats = {};
    records.forEach(r => {
      stats[r.date] = {
        count: r.count,
        totalScore: r.score * r.count  // 如果同一天有多条，总分
      };
    });

    // 计算总打卡天数
    const totalDays = records.length;

    // 顺便算一下连续打卡（连续天数）
    let streak = 0;
    if (totalDays > 0) {
      // 从今天往前推
      let checkDate = new Date();
      for (let i = 0; i < 30; i++) {
        const dateStr = checkDate.toISOString().split('T')[0];
        const found = records.find(r => r.date === dateStr);
        if (found) {
          streak++;
          checkDate.setDate(checkDate.getDate() - 1);
        } else {
          break;  // 断了就停
        }
      }
    }

    res.json({
      habitType,
      stats,
      totalDays,
      streak: streak,
      msg: '统计成功'
    });
  } catch (err) {
    res.status(500).json({ msg: '统计失败', error: err.message });
  }
});

// ---------- 9. 启动服务 ----------
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`🚀 服务已启动: http://localhost:3000`);
  console.log(`📁 数据文件: ${__dirname}/habit.db`);
});