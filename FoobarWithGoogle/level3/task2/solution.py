def solution(l):
    l.sort()
    result = 0
    lucky_tuple = []

    for i in range(len(l)):
        lucky_tuple = []
        lucky_tuple.append(l[i])
        for j in range(i+1, len(l)):
            if l[j] % l[i] == 0:
                lucky_tuple.append(l[j])
            if len(lucky_tuple) == 3:
                result += 1
                lucky_tuple = []
                lucky_tuple.append(l[i])

    return result