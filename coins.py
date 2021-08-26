def recMC(coinValueList, change, knowResults):
    minCoins = change
    if change in coinValueList:
        knowResults[change] = 1
        return 1
    elif knowResults[change] > 0:
        return knowResults[change]
    else:
        for i in [coinValue for coinValue in coinValueList if coinValue < change]:
            numCoins = 1 + recMC(coinValueList, change-i, knowResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knowResults[change] = minCoins
    return minCoins


if __name__ == '__main__':
    result = recMC([1, 5, 10, 25], 63, [0]*64)
    print(result)
