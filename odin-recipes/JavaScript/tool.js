// 现在可以使用 clipboardy 了（但要注意版本问题）
const clipboard = require('clipboardy');

// 写入
clipboard.writeSync('Hello from npm!');
console.log('✅ 已写入');

// 读取
const text = clipboard.readSync();
console.log('📋 内容:', text);