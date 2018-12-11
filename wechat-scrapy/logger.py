# -*- coding:utf-8 -*-
from logging import handlers
import logging
import time
import os


def get_logger(name):                                                                                              
    name = os.path.join(os.getenv('COMPINFO_LOG_PREFIX', ''), name)
    x = os.path.dirname(name)
    if x and not os.path.isdir(x): os.makedirs(x)

    logger = logging.getLogger('hebaochacha')
    fh = logging.FileHandler(name, encoding='utf8')
    
    formatter = logging.Formatter('%(asctime)s - %(module)s:%(lineno)dL %(process)d [%(levelname)s] %(message)s', '%Y %M %d %H:%M:%S')
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger


if __name__ == '__main__':
    pass
