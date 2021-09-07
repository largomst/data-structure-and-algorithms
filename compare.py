import random


def generateRandomArray(maxSize=100, maxValue=100):
    arr = [random.randint(0, maxValue)
           for i in range(random.randint(0, maxSize))]
    return arr


def compare(func1, func2, testTime=50_000, maxSize=100, maxValue=100, ):
    succeed = True
    for i in range(testTime):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()
        try:
            func1(arr1)
            func2(arr2)
        except Exception as e:
            print(e)
            print('len: ', len(arr1))
        else:
            if arr1 != arr2:
                succeed = False
                break
    print('Nice' if succeed else 'Fuck')
