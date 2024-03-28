import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

logging.debug('debug message')
logging.info('info message')
logging.warning('warnig massage')
logging.error('error message')
logging.critical('critical message')