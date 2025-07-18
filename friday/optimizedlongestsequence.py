from bisect import bisect_right
class Solution(object):
    def lengthOfLIS(self, nums):
        result = []
        for num in nums:
            i = bisect_right(result, num)
            if (num not in result):
                if (i >= len(result)): result.append(num)
                else: result[i] = num
            print("Inside loop ->", result, i, num)
        print(result)
        return len(result)
print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))