import logging.handlers
import os

log_path = './Log'+os.sep+'hmx.log'


def log_config():
    # 声明日志器对象
    logger=logging.getLogger()
    # 设置日志器级别
    logger.setLevel(level=logging.INFO)
    # 处理器
    sh=logging.StreamHandler()
    # 文件处理器
    trf=logging.handlers.TimedRotatingFileHandler(filename=log_path,when='midnight',interval=1,backupCount=5,encoding='utf-8')
    # 设置文件处理器级别
    trf.setLevel(logging.error)
    # 格式化字符串
    fmt = "%(asctime)s - %(levelno) s - [%(lineno) d行 - %(filename) s - %(funcName) s()] -%(message) s"
    # 格式化器
    formatter=logging.Formatter(fmt)

    # 格式化器添加到处理器
    sh.setFormatter(formatter)
    # 文件处理器添加格式话器
    trf.setFormatter(formatter)
    # 处理器添加到日志器
    logger.addHandler(sh)
    # 日志器添加文件处理器
    logger.addHandler(trf)