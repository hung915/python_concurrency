import time
from threading import Thread, Event
import random

items = []
event = Event()


class Consumer(Thread):
    def __init__(self, items, event):
        super().__init__()
        self.items = items
        self.event = event

    def run(self):
        while True:
            time.sleep(1)
            self.event.wait()
            print(self.items)
            item = self.items.pop()
            print('Consumer notify : %d popped from list by %s' % (item, self.name))


class Producer(Thread):
    def __init__(self, items, event):
        super().__init__()
        self.items = items
        self.event = event

    def run(self):
        for i in range(5):
            time.sleep(1)
            item = random.randint(0, 100)
            self.items.append(item)
            print('Producer notify : item %d appended to list by %s' % (item, self.name))
            print('Producer notify : event set by %s' % self.name)
            self.event.set()
            print('Producer notify : event cleared by %s \n' % self.name)
            self.event.clear()


if __name__ == '__main__':
    t1 = Producer(items, event)
    t2 = Consumer(items, event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
