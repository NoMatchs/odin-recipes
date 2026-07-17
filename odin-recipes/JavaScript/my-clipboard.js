// 导入模块
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// 1. 使用系统命令操作剪贴板
function writeToClipboard(text) {
    try {
        // Windows 命令
        const cleanText = text.replace(/"/g, '\\"');
        execSync(`powershell -command "Set-Clipboard -Value \\"${cleanText}\\""`, {
            stdio: 'ignore'
        });
        return true;
    } catch (error) {
        console.error('写入失败:', error.message);
        return false;
    }
}

function readFromClipboard() {
    try {
        const result = execSync('powershell -command "Get-Clipboard"', {
            encoding: 'utf8'
        });
        return result.trim();
    } catch (error) {
        console.error('读取失败:', error.message);
        return '';
    }
}

// 2. 保存历史记录
const HISTORY_FILE = path.join(__dirname, 'history.json');

function saveHistory(text) {
    let history = [];
    
    // 读取现有历史
    if (fs.existsSync(HISTORY_FILE)) {
        try {
            const data = fs.readFileSync(HISTORY_FILE, 'utf8');
            history = JSON.parse(data);
        } catch (error) {
            console.error('读取历史失败:', error.message);
        }
    }
    
    // 添加新内容（去重）
    history = history.filter(item => item !== text);
    history.unshift(text);
    
    // 只保留最近20条
    if (history.length > 20) {
        history = history.slice(0, 20);
    }
    
    // 保存
    try {
        fs.writeFileSync(HISTORY_FILE, JSON.stringify(history, null, 2));
        console.log('✅ 历史已保存');
    } catch (error) {
        console.error('保存历史失败:', error.message);
    }
}

// 3. 主程序
console.log('📋 剪贴板工具');
console.log('=============');

// 测试写入
const testText = '这是通过 Node.js 写入的文本！';
console.log('✏️ 写入:', testText);
if (writeToClipboard(testText)) {
    console.log('✅ 写入成功');
}

// 测试读取
const clipboardText = readFromClipboard();
console.log('📖 读取到:', clipboardText);

// 保存历史
if (clipboardText) {
    saveHistory(clipboardText);
}

// 显示历史
if (fs.existsSync(HISTORY_FILE)) {
    console.log('\n📚 历史记录:');
    const history = JSON.parse(fs.readFileSync(HISTORY_FILE, 'utf8'));
    history.forEach((item, index) => {
        console.log(`${index + 1}. ${item}`);
    });
}