const express = require('express');
const path = require('path');
const app = express();
const port = process.env.PORT || 3000;

// 设置静态文件目录
app.use(express.static(path.join(__dirname, 'public')));

// 启动服务器
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
