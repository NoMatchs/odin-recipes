const { app, BrowserWindow } = require('electron');

function createWindow() {
  const win = new BrowserWindow({
    width: 420,
    height: 750,
    webPreferences: { nodeIntegration: true }
  });
  win.loadFile('index.html');  // 加载你的打卡页面
}

app.whenReady().then(createWindow);