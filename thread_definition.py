import threading
from threading import Thread
import time


def function(i):
    time.sleep(5)
    print(f"function called by thread {i}\n")
    return


threads = []
if __name__ == "__main__":
    # for i in range(5):
    #     t = Thread(target=function, args=(i,))
    #     print('name', t.name)
    #     threads.append(t)
    #     t.start()
    #     # print('current_thread', threading.current_thread())
    #     t.join()
    t1 = Thread(target=function, args=(0,), name='thread1')
    t2 = Thread(target=function, args=(1,), name='thread1')
    # t3 = Thread(target=function, args=(2,))
    # t4 = Thread(target=function, args=(3,))
    # t5 = Thread(target=function, args=(4,))
    t1.daemon = True
    print(t1.ident)
    t1.start()
    # t1.join(2.0)
    # print(t1.is_alive())
    # t2.start()
    print(t1.ident)
    # print(t2.ident)
    # t3.start()
    # t4.start()
    # t5.start()
    print('end program')
    print('threads count', threading.active_count())
    # print('count', threading.active_count())


# def dab(a: int) -> int:
#     c = [1, 2, 4, 2.0]
#     for i in c:
#         b = i * 2
#     return b



# from dataclasses import dataclass, field
# from typing import Any
#
#
# @dataclass(order=True)
# class PrioritizedItem:
#     priority: int
#     item: Any = field(compare=False)
