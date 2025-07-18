# Class Assignment-3: Madam Number (Palindrome Number)
# 📌 Problem Statement: A number is a Madam number if it remains the same when reversed.
# ✅ Example 1: 121 → Reverse = 121 ✅
# ✅ Example 2: 1331 → Reverse = 1331 ✅

n=int(input("enter a number: "))
m= str(n)
s=m[::-1]
if s==m:print("yes")
else: print("no")