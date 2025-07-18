# Class Assignment-2: Number Theory & Mathematical Problems
# Krishnamurthy Number
# 📌 Problem Statement: A number is a Krishnamurthy number if the sum of the factorials of its digits equals the number itself.
# ✅ Example 1: 145 → (1! + 4! + 5!) = 145
# ✅ Example 2: 40585 → (4! + 0! + 5! + 8! + 5!) = 40585

n=int(input())
while (n>10) :
    f=n%10
    for i in range(1,f):
        p=p*f
        