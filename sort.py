from random import randint


def selectSort(alist):
    n = len(alist)
    for j in range(n, 0, -1):
        for i in range(j):
            maxPosition = 0
            if alist[i] > alist[maxPosition]:
                maxPosition = i
        alist[maxPosition], alist[j] = alist[j], alist[maxPosition]


def bibleSort(alist):
    n = len(alist)
    for j in range(n-1, 0, -1):
        # n 个元素的数组需要作 n-1 次比较
        for i in range(j):
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


def selectSort(alist):
    n = len(alist)
    for j in range(n, 0, -1):
        positionMax = 0
        for i in range(j):
            if alist[i] > alist[positionMax]:
                positionMax = i
        alist[j-1], alist[positionMax] = alist[positionMax], alist[j-1]
    return alist


def order(alist):
    n = len(alist)-1
    i = 0
    for i in range(n):
        if alist[i] > alist[i+1]:
            return False
    return True


if __name__ == '__main__':
    alist = [randint(0, 1000) for _ in range(20)]
    blist = alist[:]
    clist = alist[:]
    dlist = alist[:]
    assert order(bibleSort(alist))
    assert order(shortBibleSort(blist))
    assert order(selectSort(clist))

    from timeit import Timer
    a = Timer('bibleSort(alist)', 'from __main__ import alist,bibleSort')
    b = Timer('shortBibleSort(blist)',
              'from __main__ import blist,shortBibleSort')
    c = Timer('selectionSort(alist)', 'from __main__ import alist,selectSort')
    r1 = a.timeit(number=1000)
    r2 = b.timeit(number=1000)
    r3 = b.timeit(number=1000)
    print(r1)
    print(r2)
    print(r3)
