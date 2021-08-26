from random import randint


def bibleSort(alist):
    n = len(alist)
    for j in range(n, 0, -1):
        for i in range(j-1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

    return alist


def shortBibleSort(alist):
    n = len(alist)
    exchange = True
    while n > 0 and exchange:
        exchange = False
        for i in range(n-1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                exchange = True
        n -= 1

    return alist


if __name__ == '__main__':
    alist = [randint(0, 1000) for _ in range(20)]
    blist = alist[:]
    print(alist)

    print(alist)

    shortBibleSort(blist)
    print(blist)
    from timeit import Timer
    a = Timer('bibleSort(alist)', 'from __main__ import alist,bibleSort')
    b = Timer('shortBibleSort(blist)',
              'from __main__ import blist,shortBibleSort')
    r1 = a.timeit(number=1000)
    r2 = b.timeit(number=1000)
    print(r1)
    print(r2)
