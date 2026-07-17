const fs = require('fs').promises;

async function readFile() {
    try {
        console.log('1. 开始读取...');
        const data = await fs.readFile('hello.txt', 'utf8');
        console.log('📄 内容:', data);
        console.log('2. 读取完成');
    } catch (error) {
        console.error('❌ 错误:', error.message);
    }
}

console.log('开始程序');
readFile();
console.log('程序继续执行...');