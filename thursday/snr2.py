class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return (sum(set(nums))*3-sum(nums))//2
        
        res = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                res |= (1 << i)

        if res >= 2**31:
            res -= 2**32
        return res