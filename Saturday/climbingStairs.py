class Solution:
    def climbStairs(self, n: int) -> int:
        def ways(i,dp):
            if dp[i] != -1:
                return dp[i]
            if i==1:
                dp[i]=1
            elif i == 2:
                dp[i]=2
            else:
                dp[i]= ways(i-1,dp)+ ways(i-2,dp)
            return dp[i]

        dp = [-1]* (n+1)
        return ways(n,dp)

        