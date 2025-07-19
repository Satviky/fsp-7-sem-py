# i was not able to come up with sol ... i wrote what teacher wrote.

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        lentext1 = len(text1)
        lentext2 = len(text2)
        dp = [[0 for j in range(lentext2 + 1)] for i in range(lentext1 + 1)]
        for i in range(lentext1 + 1): dp[i][0] = 0
        for j in range(lentext2 + 1): dp[0][j] = 0
        for i in range(1, lentext1 + 1):
            for j in range(1, lentext2 + 1):
                q = 0
                if (text1[i - 1] == text2[j - 1]):
                    q = 1 + dp[i - 1][j - 1]
                else:
                    q = max(dp[i - 1][j], dp[i][j - 1])
                dp[i][j] = q
        for i in range(len(dp)): print(dp[i])
        return dp[lentext1][lentext2]
print(Solution().longestCommonSubsequence("GXTXTAB", "AGGTAB"))