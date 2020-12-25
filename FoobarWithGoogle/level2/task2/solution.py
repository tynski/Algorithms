def solution(l):
    if sum(l) % 3 == 1:
        l.sort()
        for i in l:
            if i % 3 == 1:
                l.remove(i)
                return convert(l[::-1])
        return 0
    elif sum(l) % 3 == 2:
        l.sort()
        for i in l:
            if i % 3 == 2:
                l.remove(i)
                return convert(l[::-1])
        return 0
    else:
        return convert(l.sort(reversed=True))

def convert(list): 
    return int("".join([str(i) for i in list]))

def remove_bad_digit(l):
    for i in l:
        if i % 3:
            l.remove(i)


print(solution([3, 1, 4, 1, 5, 9]))
    