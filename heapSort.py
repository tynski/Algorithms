def heapSort(array):
    n = len(array)
    maxHeap(array, n)
    extractElements(array, n)
	
def maxHeap(array, n):
    for i in range(n, -1, -1):
        heapify(array, n, i)

def extractElements(array, n):
    for i in range(n-1, 0, -1):
        swap(array, 0, i)
        heapify(array, i, 0)

def heapify(array, n, i):
    maxValue = i
    left = 2*i + 1
    right = 2*i + 2
	
    if left < n and array[i] < array[left]:
        maxValue = left
    
    if right < n and array[maxValue] < array[right]:
        maxValue = right
	
    if maxValue != i:
        swap(array, maxValue, i)
        heapify(array, n, maxValue)

def swap(array, firstIndex, secondIndex):
	array[secondIndex], array[firstIndex] = array[firstIndex], array[secondIndex]
