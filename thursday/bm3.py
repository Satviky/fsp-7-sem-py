number = 101
def isODD(num):
    return  True if (num & 1) else False
def isEven(num):
    return  not isODD(num)
print(f"{number} is EVEN is {isEven(number)}")
print(f"{number} is ODD is {isODD(number)}")
number = 104
print(f"{number} is EVEN is {isEven(number)}")
print(f"{number} is ODD is {isODD(number)}")