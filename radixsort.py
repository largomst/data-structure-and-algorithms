from compare import compare, generateRandomArray
from heap import heapSort


def maxbits(arr):
    if arr:
        max_num = max(arr)
        res = 0
        while max_num != 0:
            max_num = max_num // 10
            res += 1
        return res
    else:
        return 0


def getDigit(num, d):
    for _ in range(d-1):
        num //= 10
    return num % 10


def radixSort(arr):
    def radixSortIn(arr, l, r, digit):
        RADIX = 10
        bucket = [0]*(r-l+1)
        for d in range(1, digit+1):
            count = [0] * RADIX  # 每次都要清空
            for i in range(l, r+1):
                j = getDigit(arr[i], d)
                count[j] += 1
            for i in range(1, RADIX):  # 构造前缀和表
                count[i] = count[i] + count[i-1]
            for i in range(r, l-1, -1):  # 入桶
                j = getDigit(arr[i], d)
                bucket[count[j]-1] = arr[i]
                count[j] -= 1
            # assert sum(bucket) == sum(arr[l:r+1])
            for j in range(0, r-l+1):  # 出桶
                arr[l+j] = bucket[j]
    return radixSortIn(arr, 0, len(arr)-1, maxbits(arr))


if __name__ == "__main__":
    assert maxbits([1, 100, 1000]) == 4
    assert getDigit(10201, 1) == 1
    assert getDigit(10201, 3) == 2
    # arr = [101, 100, 231, 98, 89]
    # radixSort(arr)
    # print(arr)

    compare(heapSort, radixSort)
