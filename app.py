import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # 读取配置
    app.config.from_object(Config())
    
    # 初始化数据库
    db.init_app(app)
    
    with app.app_context():
        try:
            db.create_all()
            logger.info("数据库连接成功，表已创建（如果不存在）")
        except Exception as e:
            logger.error(f"数据库连接失败: {e}")
    
    @app.route("/")
    def index():
        return "Flask Railway 数据库测试成功"
    
    return app

class Config:
    def __init__(self):
        logger.info("初始化基础配置...")
        
        self.SECRET_KEY = os.environ.get("RAILWAY_SECRET_KEY", "dev")
        self.SQLALCHEMY_DATABASE_URI = os.environ.get("RAILWAY_DATABASE_URL", "sqlite:///app.db")
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        logger.info(f"数据库连接 URL: {self.SQLALCHEMY_DATABASE_URI}")

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))