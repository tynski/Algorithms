def solution(l):
    if not(l and sum(l) > 2):
        return 0
    l.sort()
    if sum(l) % 3 == 1:
        for i in l:
            if i % 3 == 1:
                l.remove(i)
                return convert(l[::-1])
        m = None
        for i in l:
            if i % 3 == 2:
                if m:
                    l.remove(m)
                    l.remove(i)
                    return convert(l[::-1])
                else:
                    m = i
        return 0
    elif sum(l) % 3 == 2:
        for i in l:
            if i % 3 == 2:
                l.remove(i)
                return convert(l[::-1])
        m = None
        for i in l:
            if i % 3 == 1:
                if m:
                    l.remove(m)
                    l.remove(i)
                    return convert(l[::-1])
                else:
                    m = i
        return 0
    else:
        return convert(l[::-1])

def convert(list): 
    return int("".join([str(i) for i in list]))

print(solution([3, 1, 4, 1, 5, 9]))
print(solution([3, 1, 4, 1]))
print(solution([]))
print(solution([1,1]))
print(solution([2]))
print(solution([1]))
print(solution([2,2]))



