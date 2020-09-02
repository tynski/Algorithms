# Software Mansion code task
## Description
Write a function that receives two sequences: A and B of integers and returns one sequence C. Sequence C should c
ontain all elements from sequence A (maintaining the order) except those, that are present in sequence B **p** times, 
where **p** is a prime number.

Example:
```
A=[2,3,9,2,5,1,3,7,10]
B=[2,1,3,4,3,10,6,6,1,7,10,10,10]
C=[2,9,2,5,7,10]
```

## Time complexity analysis
The Big O time analysis for the given algorithm is O(n^5). Worst-case time complexity may be scary, though in typical use case creating a dictionary with numbers frequency and use of counter domain here: `[i for i in a if not i in skip_them]` can be much faster.

## Dependencies
Python 3.8.5
