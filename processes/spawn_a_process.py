import multiprocessing


def foo(i):
    print('called function in process: %s' % i)


if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        p.start()
        p.join()
