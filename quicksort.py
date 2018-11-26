def quicksort(array, first, last):
    if(first < last):
        pivot = partition(array, first, last)
        quicksort(array, first, pivot - 1)
        quicksort(array, pivot + 1, last)


def partition(array, first, last):
    q = first
    for j in range(first, last):
        if(array[j] <= array[last]):
            swap(array, q, j)
            q += 1
    swap(array, q, last)
    return q


def swap(array, first, second):
    array[second], array[first] = array[first], array[second]
