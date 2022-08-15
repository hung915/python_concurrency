import threading
import requests
import time


# def ping(url):
#     res = requests.get(url)
#     print(f'{url}: {res.text}')
#
#
# urls = [
#     'http://httpstat.us/200',
#     'http://httpstat.us/400',
#     'http://httpstat.us/404',
#     'http://httpstat.us/408',
#     'http://httpstat.us/500',
#     'http://httpstat.us/524'
# ]
#
# start = time.time()
# for url in urls:
#     ping(url)
# print(f'Sequential: {time.time() - start : .2f} seconds')
#
# print()
#
# start = time.time()
# threads = []
# for url in urls:
#     thread = threading.Thread(target=ping, args=(url,))
#     threads.append(thread)
#     thread.start()
# for thread in threads:
#     thread.join()
#
# print(f'Threading: {time.time() - start : .2f} seconds')


# class MyThread(threading.Thread):
#     def __init__(self, url):
#         threading.Thread.__init__(self)
#         self.url = url
#         self.result = None
#
#     def run(self):
#         res = requests.get(self.url)
#         self.result = f'{self.url}: {res.text}'
#
#
# urls = [
#     'http://httpstat.us/200',
#     'http://httpstat.us/400',
#     'http://httpstat.us/404',
#     'http://httpstat.us/408',
#     'http://httpstat.us/500',
#     'http://httpstat.us/524'
# ]
#
# start = time.time()
#
# threads = [MyThread(url) for url in urls]
# for thread in threads:
#     thread.start()
# for thread in threads:
#     thread.join()
# for thread in threads:
#     print(thread.result)
#
# print(f'Took {time.time() - start : .2f} seconds')
#
# print('Done.')


class MyThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.result = None

    def run(self):
        res = requests.get(self.url)
        self.result = f'{self.url}: {res.text}'

urls = [
    'http://httpstat.us/200',
    'http://httpstat.us/200?sleep=20000',
    'http://httpstat.us/400'
]

start = time.time()

threads = [MyThread(url) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
for thread in threads:
    print(thread.result)

print(f'Took {time.time() - start : .2f} seconds')

print('Done.')
