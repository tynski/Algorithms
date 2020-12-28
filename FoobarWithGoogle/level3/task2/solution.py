def solution(l):
    l.sort()
    result = 0

    for i in range(len(l)):
        counter = 1
        for j in range(i+1, len(l)):
            if l[j] % l[i] == 0:
                counter += 1
            if counter == 3:
                result += 1
                counter = 1

    return result