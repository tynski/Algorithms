def solution(l):
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