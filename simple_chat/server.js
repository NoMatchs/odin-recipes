const express = require('express');
const http = require('http');
const { Server } = require("socket.io");

const app = express();
const server = http.createServer(app);
const io = new Server(server);

// 当有人访问网站首页时，把 index.html 发给他
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// 监听聊天连接
io.on('connection', (socket) => {
  console.log('一个用户连接了');
  
  // 收到某人发的消息，就广播给所有人（包括自己）
  socket.on('chat message', (msg) => {
    io.emit('chat message', msg); 
  });
});

server.listen(3000, () => {
  console.log('聊天室运行在 http://localhost:3000');
});