import math

def binarySearch(searchedList, target):
    if not searchedList:
    	return 'Dont have list to search'
    
    n = len(searchedList)
    Min = 0
    Max = n-1
 
    while Min<=Max:
        searchPosition = math.floor((Max+Min)/2)
        
        if searchedList[searchPosition] == target:
            return searchPosition
        elif searchedList[searchPosition] < target:
            Min = searchPosition + 1
        else:
            Max = searchPosition - 1
    
    return 'Nothing found'
