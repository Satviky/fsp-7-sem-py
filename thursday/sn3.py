def singleNumber(nums):
    # return(sum(set(nums))*3 - sum(nums))//2
    result = 0
    for i in range(32):  # 32-bit integer
        bit_sum = 0
        for num in nums:
            if (num >> i) & 1:
                bit_sum += 1
        if bit_sum % 3 != 0:
            result |= (1 << i)
    
    if result >= 2**31:
        result -= 2**32
    return result

nums = [11, 22, 33, 44, 33, 11, 22, 33, 22, 11]
print(singleNumber(nums))
