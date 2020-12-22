def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([8,9,10,12,45,123,6,3,12,4,99]))
print(quick_sort([54,23,123,4545,231,1,123,4,524,12312,2,233]))