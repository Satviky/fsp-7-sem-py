# questions
|sr|title|external web link|References|
|--|-----|-----------------|----------|
|1||Min number of steps to reach n->1| [leetcode]()| [Readme reference](##Min-number-of-steps)
|2| Keyboard Row | [Leetcode](https://leetcode.com/problems/keyboard-row/description/) |[Readme Reference](##Keyboard-rows)
|3| Climbing Stairs| [Leetcode](https://leetcode.com/problems/climbing-stairs) | [Readme reference](##Climbing-Stairs)

## Min number of steps
Not pasting the code here as there are two ways i solved the problem. Lik to solution have been attached.
1. if (n%3==0) n=n//3
2. if (n%2==0) n=n//2
3. otherwise n=n-1

2 approach have been useds
1. top down [read the code](/Saturday/min-no-of-steps.py)
2. Bottum up [read the code](/Saturday/minSteps-bu.py)

## Keyboard rows

```py
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1= set('qwertyuiop')
        r2=set('asdfghjkl')
        r3=set('zxcvbnm')
        v_word=[]
        for word in words:
            w = set(word.lower())
            if w.issubset(r1) or w.issubset(r2) or w.issubset(r3):
                v_word.append(word)
        return v_word
```

## Climbing Stairs
```py
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
 ```

## LCS
1. [solution 1](/Saturday/lcs1.py)
2. [solution 2](/Saturday/lcs2.py)

## Min path sum
```py
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if i>0 and j>0:
                    grid[i][j] = min(grid[i][j] + grid[i-1][j], grid[i][j] + grid[i][j-1])
                elif i>0 :
                    grid[i][j] += grid[i-1][j]
                elif j>0:
                    grid[i][j] += grid[i][j-1]
        return grid[-1][-1]
```
