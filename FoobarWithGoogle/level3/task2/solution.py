def solution_brute_force(l):
    if len(l) < 3:
        return 0
    
    l.sort()
    result = 0

    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j] % l[i] == 0:
                for k in range(j+1, len(l)):
                    if l[k] % l[j] == 0:
                        result += 1

    return result

def solution(l):
    if len(l) < 3:
        return 0

    l.sort()
    result = 0
    counter = [0]*len(l)
    
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                counter[i] += 1
                result += counter[j] 

    return result

# from collections import Counter
# from itertools import combinations

# def solution(l):
#     counts = Counter(l)  # {x: occurrences of x}
#     divisors = Counter()        # {x: distinct proper divisors of x}
#     multiples = Counter()       # {x: distinct proper multiples of x}
#     for x, y in combinations(sorted(counts), 2):
#         if y % x == 0:
#             divisors[y] += 1
#             multiples[x] += 1
#     result = 0
#     for x, n in counts.items():
#         result += divisors[x] * multiples[x]
#         if n >= 2:
#             result += divisors[x] + multiples[x]
#             if n >= 3:
#                 result += 1
#     return result