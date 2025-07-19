#https://leetcode.com/problems/longest-common-subsequence/description/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        return self.helper(text1,text2,0,0)
    def helper(self,text1,text2,i,j):
        if i == len(text1) or  j == len(text2):
            return 0
        if text1[i] == text2[j]:
            return 1+self.helper(text1,text2,i+1,j+1)
        else:
            return max(self.helper(text1,text2,i+1,j), self.helper(text1,text2,i,j+1))
        

# submitting this on leetcode doesn't work because for test case 17, it fails.
# Reason of failure: Time limit exceeded.