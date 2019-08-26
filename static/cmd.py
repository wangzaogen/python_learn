import os
import sched
import time
from datetime import datetime

schedule = sched.scheduler(time.time, time.sleep)

def tip(inc):
    os.system("msg * 是时候喝口水动一动了")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    schedule.enter(inc, 0, tip, (inc,))

def main(inc=60):
    # enter四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，
    # 给该触发函数的参数（tuple形式）
    schedule.enter(0, 0, tip, (inc,))
    schedule.run()


# 10s 输出一次
main(1800)
