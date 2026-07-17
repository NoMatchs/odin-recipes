const { app, BrowserWindow, Tray, Menu, clipboard, ipcMain } = require('electron');
const path = require('path');
const fs = require('fs');

let mainWindow = null;
let tray = null;
let history = [];
const HISTORY_FILE = path.join(__dirname, 'history.json');
const MAX_HISTORY = 20;

// 加载历史记录
function loadHistory() {
    try {
        if (fs.existsSync(HISTORY_FILE)) {
            const data = fs.readFileSync(HISTORY_FILE, 'utf8');
            history = JSON.parse(data);
            return history;
        }
    } catch (error) {
        console.error('加载历史失败:', error);
    }
    return [];
}

// 保存历史记录
function saveHistory(data) {
    try {
        fs.writeFileSync(HISTORY_FILE, JSON.stringify(data, null, 2));
        history = data;
    } catch (error) {
        console.error('保存历史失败:', error);
    }
}

// 添加新内容到历史
function addToHistory(text) {
    if (!text || text.trim() === '') return;
    
    let list = loadHistory();
    // 去重
    list = list.filter(item => item !== text);
    // 添加到开头
    list.unshift(text);
    // 限制数量
    if (list.length > MAX_HISTORY) {
        list = list.slice(0, MAX_HISTORY);
    }
    saveHistory(list);
    
    // 通知渲染进程更新
    if (mainWindow) {
        mainWindow.webContents.send('history-updated', list);
    }
}

// 创建主窗口
function createWindow() {
    mainWindow = new BrowserWindow({
        width: 600,
        height: 500,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        },
        icon: path.join(__dirname, 'icon.png') // 可选
    });

    mainWindow.loadFile('index.html');
    
    // 窗口关闭时隐藏而不是退出
    mainWindow.on('close', (event) => {
        event.preventDefault();
        mainWindow.hide();
    });
}

// 创建系统托盘
function createTray() {
    tray = new Tray(path.join(__dirname, 'icon.png')); // 需要准备图标
    
    const contextMenu = Menu.buildFromTemplate([
        { label: '📋 显示剪贴板工具', click: () => {
            if (mainWindow) {
                mainWindow.show();
            }
        }},
        { label: '📚 历史记录', submenu: getHistoryMenu() },
        { type: 'separator' },
        { label: '清空历史', click: () => {
            saveHistory([]);
            if (mainWindow) {
                mainWindow.webContents.send('history-updated', []);
            }
        }},
        { type: 'separator' },
        { label: '退出', click: () => {
            app.quit();
        }}
    ]);
    
    tray.setToolTip('📋 剪贴板工具');
    tray.setContextMenu(contextMenu);
    
    // 左键点击显示/隐藏
    tray.on('click', () => {
        if (mainWindow.isVisible()) {
            mainWindow.hide();
        } else {
            mainWindow.show();
        }
    });
}

// 生成历史记录菜单
function getHistoryMenu() {
    const historyList = loadHistory();
    if (historyList.length === 0) {
        return [{ label: '暂无记录', enabled: false }];
    }
    
    return historyList.slice(0, 10).map((item, index) => ({
        label: item.length > 30 ? item.slice(0, 30) + '...' : item,
        click: () => {
            clipboard.writeText(item);
            // 可选：发送通知
            if (mainWindow) {
                mainWindow.webContents.send('clipboard-updated', item);
            }
        }
    }));
}

// 监听剪贴板变化
let lastText = '';
function startClipboardMonitor() {
    setInterval(() => {
        try {
            const currentText = clipboard.readText();
            if (currentText && currentText !== lastText) {
                lastText = currentText;
                addToHistory(currentText);
                
                // 更新托盘菜单
                if (tray) {
                    const menu = Menu.buildFromTemplate([
                        { label: '📋 显示剪贴板工具', click: () => {
                            if (mainWindow) mainWindow.show();
                        }},
                        { label: '📚 历史记录', submenu: getHistoryMenu() },
                        { type: 'separator' },
                        { label: '清空历史', click: () => {
                            saveHistory([]);
                            if (mainWindow) {
                                mainWindow.webContents.send('history-updated', []);
                            }
                        }},
                        { type: 'separator' },
                        { label: '退出', click: () => app.quit() }
                    ]);
                    tray.setContextMenu(menu);
                }
            }
        } catch (error) {
            // 忽略错误
        }
    }, 1000); // 每秒检测一次
}

// 应用启动
app.whenReady().then(() => {
    createWindow();
    createTray();
    startClipboardMonitor();
    
    // 加载历史
    const historyData = loadHistory();
    if (mainWindow) {
        mainWindow.webContents.on('did-finish-load', () => {
            mainWindow.webContents.send('history-updated', historyData);
        });
    }
});

// 所有窗口关闭
app.on('window-all-closed', (event) => {
    event.preventDefault();
});

// 处理 IPC 消息（从渲染进程接收）
ipcMain.on('get-history', (event) => {
    event.returnValue = loadHistory();
});

const { globalShortcut } = require('electron');

// 在 app.whenReady 中添加
globalShortcut.register('CommandOrControl+Shift+V', () => {
    if (mainWindow) {
        if (mainWindow.isVisible()) {
            mainWindow.hide();
        } else {
            mainWindow.show();
        }
    }
});

// 应用退出前注销快捷键
app.on('will-quit', () => {
    globalShortcut.unregisterAll();
});

// 在 createWindow 后添加
app.whenReady().then(() => {
    createWindow();
    // 默认隐藏窗口
    mainWindow.hide();
    createTray();
    startClipboardMonitor();
    // ... 其他代码
});