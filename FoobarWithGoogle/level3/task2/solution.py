def solution(l):
    if len(l) < 3:
        return 0

    result = 0
    counter = [0]*len(l)
    
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                counter[i] += 1
                result += counter[j] 

    return result