def mergeSort(array):
	arrayLength = len(array)
	if arrayLength == 1:
	  return array
	arrayHalf = arrayLength//2
	firstHalf = mergeSort(array[arrayHalf:])
	secondHalf = mergeSort(array[:arrayHalf])
	return merge(firstHalf, secondHalf)
	
def merge(leftArray, rightArray):
  i = 0
  j = 0
  sortedArray = []
  while i<len(leftArray) and j<len(rightArray):
	  if leftArray[i] < rightArray[j]:
		  sortedArray.append(leftArray[i])
		  i += 1
	  else:
		  sortedArray.append(rightArray[j])
		  j += 1
  if i < len(leftArray):
	  sortedArray.extend(leftArray[i:])
  if j < len(rightArray):
	  sortedArray.extend(rightArray[j:])
  return sortedArray
