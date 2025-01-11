def median(arr):
    n = len(arr)
    arr.sort()

    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2

    return arr[n//2]
