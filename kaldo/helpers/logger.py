import sys
from time import gmtime, strftime
import psutil
import logging
import numpy as np

datetime = strftime("%a_%d_%b__%Y_%H_%M_%S", gmtime())
logname = 'kaldo_' + str(datetime) + '.log'
logger = logging.getLogger('kaldo')
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
log_level = logging.INFO

logger.setLevel(log_level)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(log_level)
formatter = logging.Formatter(format)
handler.setFormatter(formatter)
logger.addHandler(handler)

def get_logger():
    logger = logging.getLogger('kaldo')
    return logger


def log_size(shape, type=np.float, memory_threshold_in_mb=30):
    shape = np.array(shape)
    out = 'Memory. Available / total: '
    out +=  str(psutil.virtual_memory().available/1e6) + ' MB / '
    out +=  str(psutil.virtual_memory().total/1e6) + ' MB'
    if type == np.float:
        size = 64
    elif type == np.complex:
        size = 128
    out_2 = 'Shape of tensor: ' + str(shape)
    out_2 += ', Type: ' + str(type)
    memory_used_in_mb = np.prod(shape) * size / 8 * 1e-6
    out_3 = 'Size of tensor: ' + str(memory_used_in_mb) + ' MB'
    if memory_used_in_mb > memory_threshold_in_mb:
        log = get_logger().info
    else:
        log = get_logger().debug
    log(out)
    log(out_2)
    log(out_3)
