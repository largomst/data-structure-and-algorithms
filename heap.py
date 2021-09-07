import random
from compare import compare
from sort import selectSort


def heapInsert(arr, index):
    def parent(index): return (index-1) // 2 if index - 1 > 0  \
        else (index - 1) // -2
    while arr[index] > arr[parent(index)]:
        arr[index], arr[(index-1)//2] = arr[(index-1)//2], arr[index]
        index = parent(index)


def heapify(arr, index, heapSize):
    left = index*2+1
    while left < heapSize:
        if left+1 < heapSize and arr[left+1] > arr[left]:
            largest = left+1
        else:
            largest = left
        if arr[largest] > arr[index]:
            arr[largest], arr[index] = arr[index], arr[largest]
            index = largest
        else:
            break
        left = index*2+1


def heapSort(arr):
    n = len(arr)
    heapSize = 0
    # for i in range(n):
    #     heapInsert(arr, i)
    for i in range(n-1, -1, -1):
        heapify(arr, i, n)
    heapSize = n
    while heapSize > 0:
        arr[0], arr[heapSize-1] = arr[heapSize-1], arr[0]
        heapSize -= 1
        heapify(arr, 0, heapSize)


if __name__ == '__main__':
    arr = [random.randint(0, 100) for i in range(100)]
    heapSort(arr)
    print(arr)
    compare(heapSort, selectSort)
