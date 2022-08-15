import threading

shared_resource_with_lock = 0
shared_resource_with_no_lock = 0
COUNT = 1000  # 1000000
shared_resource_lock = threading.Lock()


# LOCK MANAGEMENT
def increment_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock += 1
        shared_resource_lock.release()


def decrement_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock -= 1
        shared_resource_lock.release()


# NO LOCK MANAGEMENT
def increment_without_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock += 1


def decrement_without_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock -= 1


if __name__ == "__main__":
    t1 = threading.Thread(target=increment_with_lock)
    t2 = threading.Thread(target=decrement_with_lock)
    t3 = threading.Thread(target=increment_without_lock)
    t4 = threading.Thread(target=decrement_without_lock)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("the value of shared variable with lock management is %s" % shared_resource_with_lock)
    print("the value of shared variable with race condition is %s" % shared_resource_with_no_lock)

# import threading
#
#
# def job1():
#     global A
#     lock.acquire()
#     for i in range(50):
#         A += 1
#         print('job1', A)
#     lock.release()
#
#
# def job2():
#     global A
#     a = lock.acquire(timeout=2)
#     for i in range(50):
#         A += 10
#         print('job2', A)
#     lock.release()
#
#
# if __name__ == '__main__':
#     lock = threading.Lock()
#     A = 0
#     t1 = threading.Thread(target=job1)
#     t2 = threading.Thread(target=job2)
#     # print('locked: ', lock.locked())
#     # print('end job1')
#     t1.start()
#     t2.start()

# print('threads count', threading.active_count())
# t2.join()
