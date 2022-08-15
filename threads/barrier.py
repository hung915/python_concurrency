# program to demonstrate
# barriers in python

import threading

barrier = threading.Barrier(3)


class MyThread(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_ID = thread_id

    def run(self):
        print(str(self.thread_ID) + "\n")
        print("Parties = " + str(barrier.parties) + "\n")
        print("n_waiting = " + str(barrier.n_waiting) + "\n")
        barrier.wait()


thread1 = MyThread(100)
thread2 = MyThread(101)

thread1.start()
thread2.start()

barrier.wait()

print(str(barrier.broken) + "\n")
barrier.reset()
print("n_waiting after reset = " + str(barrier.n_waiting))
barrier.abort()
print("End")
