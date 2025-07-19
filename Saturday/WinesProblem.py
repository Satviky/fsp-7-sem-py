def wineProfitTopDown(wines, i, j, y):
    # base case
    if (i > j): return 0
    # recursive case
    option1 = wines[i]*y + wineProfitTopDown(wines, i+1, j, y+1)
    option2 = wines[j]*y + wineProfitTopDown(wines, i, j-1, y+1)
    return max(option1, option2)
wines = [2, 3, 5]
print(wineProfitTopDown(wines, 0, len(wines) - 1, 1))