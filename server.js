const express = require('express');
const path = require('path');
const helmet = require('helmet');  // 引入 helmet
const app = express();
const port = process.env.PORT || 3000;

// 设置 helmet 来配置 CSP
app.use(helmet.contentSecurityPolicy({
    directives: {
        defaultSrc: ["'self'"],  // 只允许同源加载资源
        fontSrc: ["'self'", "https://fonts.gstatic.com"],  // 允许加载字体文件
        styleSrc: ["'self'", "https://fonts.googleapis.com"],  // 允许加载样式表
        imgSrc: ["'self'"],  // 只允许加载图片
        scriptSrc: ["'self'"],  // 只允许加载脚本
    }
}));

// 设置静态资源文件夹
app.use(express.static(path.join(__dirname, 'public')));

// 启动服务器
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
