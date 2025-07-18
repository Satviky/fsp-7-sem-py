def fibonacciDPTopDown(n, dp):
    print(f"Calling for n = {n}...", dp)
    if (n == 0 or n == 1): return n
    if (dp[n] != 0): return dp[n]
    dp[n] = fibonacciDPTopDown(n - 1, dp) + fibonacciDPTopDown(n - 2, dp)
    return dp[n]
n = int(input("Please enter the value for n:"))
dp = [0 for _ in range(n + 1)]
print(dp)
print(fibonacciDPTopDown(n, dp))
print(dp)