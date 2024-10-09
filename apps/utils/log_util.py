import logging
from django.conf import settings


class LogUtil:
    def __init__(self):
        self.logger = self.init_log()
    def init_log(self):
        # 创建一个日志记录器
        # 创建一个日志记录器
        logger = logging.getLogger(settings.LOG_NAME)
        logger.setLevel(logging.DEBUG)

        # 创建一个文件处理器并设置级别和模式为'w'
        file_handler = logging.FileHandler(settings.LOG_PATH, mode='a')
        file_handler.setLevel(logging.DEBUG)

        # 创建一个控制台处理器并设置级别
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # 创建一个格式化器
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 将格式化器添加到处理器
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 将处理器添加到记录器
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger


logUtil = LogUtil()
