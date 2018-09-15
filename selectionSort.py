def selectionSort(array):
    for index in range(len(array)):
        swap(array,index,indexOfMinimum(array, index))

def indexOfMinimum(array,startIndex):
    minIndex = startIndex
    minVal = array[startIndex]
    for index in range(minIndex + 1, len(array)):
        if array[index] < minVal:
            minIndex = index
            minVal = array[index]
    return minIndex

def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp
