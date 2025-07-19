# Day 1
>[!warning]
> this is not maintained and checked and my laptop was messing up on the days this folder was being made.

## Data Structure
Way to store data in the memory of a computer.
Important:
1. chosing appropriate data structure
2. each data structure algo have it's own advantages and disadvantages.
3. using standard library available in prog lang is a good idea.

### Algorithm Types
They are mutliple difference types of algorithms are possible. Some of the importance types are:

1. Simple recursive

2. Backtracking
    
    N-queen Problem |chess Board Problem

3. Divide and Conquere 

    tic Tac Toe
4. Dynamic Prog

    A milestone
    |TD| BU|
    |--|---|
    | memoization | tabulation|

    problem is simple but application aint'


5. Greedy

    constructs solution by making the choice that looks back at that moment
    >[!warning]
    > No backtracking.

    difficulty is to find a greedy strategy that always producesand optimal solution to the problem.
    inbuilt
    - selection [higeshest val]
    - optimality check ; am i getting min no of coin
    - feasibility check ; the sol in which i am moving 
    - objective ; did i reached objective

6. Branch and Bound
7. Brute Force

8. Randomized

## Graphs
1. DFS
2. BFS
3. Kruskal
4. Prim
5. Dijkstra
6. Warshall
7. Floyd
8. Bellman Ford -> routing

## some ofglobal contests company exam
- ICPC
- IOI
- Snackdown
- Google Codejam
- Google Kickstart
- Fackbook Hacker Cup

# Time and Space Complexity
- quantifies the amount of time taken by an algo to run as a function of the len take input

## order of growth
way of saying how execution time of prog and time and space occupied by prog keep changing overtime

ex: bigO

### BigO
    - asymptotic upper bound, we use O notation.
    - aymptotic lower bound, we use ohm- notation

>[!note]
> you may get the data, you may not get the data... non deterministic data. reducing the time complexity, the main challenge.

> time complexity of loop is considered as O(loglogn)

# Day 2

```py
AAAAAAAAAAA -> 11 A
.BBBBBBBBB -> 1. 9 B
..CCCCCCC -> 2. 7 C
...DDDDD -> 3. 5 D
....EEE -> 4. 3 E
.....F -> 5. 1 F
....GGG -> 4. 3 F
...HHHHH -> 3. 5 H
..IIIIIII -> 2. 7 I
.JJJJJJJJJ -> 1. 9J
KKKKKKKKKKK -> 11 K
```


|--|  |--|  |--|  |--|
|--|  |--|  |--|  |--|
|--|  |--|  |--|  |--|
|--|  |--|  |--|  |--|
|--|  |--|  |--|  |--|
|--|  |--|  |--|  |--|
