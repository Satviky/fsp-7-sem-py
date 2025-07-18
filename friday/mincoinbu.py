import math
def minCoinsBottomUp(N, coins, T):
    dp = [0 for i in range(N + 1)]
    for n in range(1, N + 1):

        dp[n] = math.inf
        for i in range(T):
            if (n - coins[i] >= 0):
                subprob = dp[n - coins[i]]
                dp[n] = min(dp[n], subprob + 1)
    return dp[n]
N = 15; coins = [1, 7, 10]
T = len(coins)
print(minCoinsBottomUp(N, coins, T))