import os
import logging
import time
import json
from logging import Handler, FileHandler, StreamHandler


class PathFileHandler(FileHandler):

    def __init__(self, path, filename, mode='a', encoding=None, delay=False):
        if not os.path.exists(path):
            os.mkdir(path)
        self.baseFilename = os.path.join(path, filename)
        self.mode = mode
        self.encoding = encoding
        self.delay = delay
        if delay:
            Handler.__init__(self)
            self.stream = None
        else:
            StreamHandler.__init__(self, self._open())


class Loggers(object):
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    '''
        %(name)s            Name of the logger (logging channel)
        %(levelno)s         Numeric logging level for the message (DEBUG, INFO,
                            WARNING, ERROR, CRITICAL)
        %(levelname)s       Text logging level for the message ("DEBUG", "INFO",
                            "WARNING", "ERROR", "CRITICAL")
        %(pathname)s        Full pathname of the source file where the logging
                            call was issued (if available)
        %(filename)s        Filename portion of pathname
        %(module)s          Module (name portion of filename)
        %(lineno)d          Source line number where the logging call was issued
                            (if available)
        %(funcName)s        Function name
        %(created)f         Time when the LogRecord was created (time.time()
                            return value)
        %(asctime)s         Textual time when the LogRecord was created
        %(msecs)d           Millisecond portion of the creation time
        %(relativeCreated)d Time in milliseconds when the LogRecord was created,
                            relative to the time the logging module was loaded
                            (typically at application startup time)
        %(thread)d          Thread ID (if available)
        %(threadName)s      Thread name (if available)
        %(process)d         Process ID (if available)
        %(message)s         The result of record.getMessage(), computed just as
                            the record is emitted
    '''

    def __init__(self, filename='{date}.log'.format(date=time.strftime("%Y-%m-%d_%H%M%S", time.localtime())),
                        level='info',
                        log_dir=os.path.join("..", "logs"),
                        fmt='[%(asctime)s] [%(thread)d - %(threadName)s - %(process)d] [%(levelname)s] '
                            '[%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
                  ):

        self.logger = logging.getLogger(filename)

        # self.directory = os.path.join(os.getcwd(), log_dir)
        self.directory = log_dir
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别

        if not self.logger.handlers:
            # stream_handler = logging.StreamHandler()  # 往屏幕上输出
            # stream_handler.setFormatter(format_str)
            file_handler = PathFileHandler(path=self.directory, filename=filename, mode='a',encoding='utf-8')
            file_handler.setFormatter(format_str)
            # self.logger.addHandler(stream_handler)
            self.logger.addHandler(file_handler)

    def log_case_info(self, url, data, method, status_code, result):
        if isinstance(data, dict):
            data = json.dumps(data, ensure_ascii=False)  # 如果data是字典格式，转化为字符串
        self.logger.info("请求url:{0}".format(url))
        self.logger.info("请求参数:{0}".format(data))
        self.logger.info("请求方法:{0}".format(method))
        self.logger.info("返回数据:{0}".format(result))
        if status_code < 400:
            self.logger.info("请求状态码:{0}".format(status_code))
        if status_code >= 400:
            self.logger.error("请求状态码:{0}".format(status_code))


if __name__ == "__main__":
    log = Loggers(level='debug')
    # 示例
    log.log_case_info("test_case","http://baidu.com","N/A","GET",500,"{aac:aac}")

    # txt = "将信息打印到日志文件中......"
    # log.logger.info(4)
    # log.logger.info(5)
    # log.logger.info(txt)
    # log.logger.warning("this is warning")
