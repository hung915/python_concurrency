import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s', )


def threading_with(statement):
    with statement:
        logging.debug(f'{statement} acquired via with')


def threading_not_with(statement):
    statement.acquire()
    try:
        logging.debug(f'{statement} acquired directly')
    finally:
        statement.release()


if __name__ == '__main__':
    lock = threading.Lock()
    rlock = threading.RLock()
    condition = threading.Condition()
    mutex = threading.Semaphore(1)
    threading_synchronization_list = [lock, rlock, condition, mutex]

    for statement in threading_synchronization_list:
        t1 = threading.Thread(target=threading_with,
                              args=(statement,))
        t2 = threading.Thread(target=threading_not_with,
                              args=(statement,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
