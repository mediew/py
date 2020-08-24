from multiprocessing import Process


def proc(*args):
    s = 1
    for i in args:
        s *= i
    print(s)


if __name__ == '__main__':
    # 测试可变变量
    p = Process(target=proc, args=(1, 2, 3, 4, 5, 6, 7))
    p.start()
    p.join()
