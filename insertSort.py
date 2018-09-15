def insertSort(List):
	for j in range (len(array)):
		key = array[j]
		i = j-1
		while array[i] > key:
			array[i+1] = array[i]
			i -= 1
		array[i+1] = key
	return array
