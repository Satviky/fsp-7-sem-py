# Single Number - I
# Given a non-empty array of integers, every element appears twice except one. Find that single one.
# * Example-1: input: [11, 33, 22, 44, 33, 11, 22], output: 44
# * Example-2: input: [10, 20, 40, 30, 20, 10, 60, 60, 30], output: 40


# nums=map(int, input("n: ").split())
nums=list(map(int, input().split()))

count_map = {}
for num in nums:
    if num in count_map:
        count_map[num] += 1
    else:
        count_map[num] = 1

for num in count_map:
    if count_map[num] == 1:
        print("Single number is:", num)
        break
