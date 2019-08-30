
import time
from functools import wraps

def timer_wrap(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        time.sleep(2)
        end = time.time()
        print('执行结果{},共耗时{}秒'.format(result,start-end))
        return result
    return wrapper


@timer_wrap
def add(a,b):
    """
    求和
    :param a:
    :param b:
    :return:
    """
    return a+b

sum = add(4, 5)
print(sum)
