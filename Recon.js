const fs = require('fs'); // 引入文件系统模块

// 1. 读取 JSON 数据文件
const invoices = JSON.parse(fs.readFileSync('./invoices.json', 'utf8'));
const plays = JSON.parse(fs.readFileSync('./plays.json', 'utf8'));

// 2. 粘贴你提供的函数代码
function statement (invoice, plays) {
    let totalAmount = 0;
    let volumeCredits = 0;
    let result = `Statement for ${invoice.customer}\n`; 
    const format = new Intl.NumberFormat("en-US",
    { style: "currency", currency: "USD", minimumFractionDigits: 2 }).format; 
    
    for (let perf of invoice.performances) {
        const play = plays[perf.playID];
        let thisAmount = 0;
        switch (play.type) {
            case "tragedy":
                thisAmount = 40000;
                if (perf.audience > 30) {
                    thisAmount += 1000 * (perf.audience - 30);
                }
                break;
            case "comedy":
                thisAmount = 30000;
                if (perf.audience > 20) {
                    thisAmount += 10000 + 500 * (perf.audience - 20); 
                }
                thisAmount += 300 * perf.audience;
                break;
            default:
                throw new Error(`unknown type: ${play.type}`); 
        }
        // add volume credits
        volumeCredits += Math.max(perf.audience - 30, 0); 
        // add extra credit for every ten comedy attendees 
        if ("comedy" === play.type) volumeCredits += Math.floor(perf.audience / 5);
        // print line for this order
        result += ` ${play.name}: ${format(thisAmount/100)} (${perf.audience} seats)\n`; 
        totalAmount += thisAmount;
    }
    result += `Amount owed is ${format(totalAmount/100)}\n`; 
    result += `You earned ${volumeCredits} credits\n`; 
    return result;
}

// 3. 调用函数并打印结果
// 注意：invoices.json 里可能是一个数组，这里假设取第一个账单
console.log(statement(invoices[0], plays)); 