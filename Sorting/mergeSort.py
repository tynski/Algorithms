def mergeSort(array):
    N = len(array)
    if N == 1:
        return array
    arrayHalf = N // 2
    firstHalf = mergeSort(array[arrayHalf:])
    secondHalf = mergeSort(array[:arrayHalf])
    return merge(firstHalf, secondHalf)


def merge(p, r):
    i = 0
    j = 0
    sortedArray = []

    while i < len(p) and j < len(r):
        if p[i] < r[j]:
            sortedArray.append(p[i])
            i += 1
        else:
            sortedArray.append(r[j])
            j += 1

    if i < len(p):
        sortedArray.extend(p[i:])
    if j < len(r):
        sortedArray.extend(r[j:])

    return sortedArray


print(mergeSort([4,5,8,4,2,4,1]))
print(mergeSort([12, 11, 13, 5, 6, 7]))
