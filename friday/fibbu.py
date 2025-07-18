# time complexity O(n) and space complexity O(n)
def fibonacciDPBottomUp(n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    print(dp)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp)
    return dp[n]
n = int(input("Please enter the value for n:"))
print(fibonacciDPBottomUp(n))