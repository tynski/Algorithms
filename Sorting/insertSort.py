def insertSort(array):
    N = len(array)
    for j in range(1, N):
        key = array[j]
        i = j - 1
        while array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
    return array
