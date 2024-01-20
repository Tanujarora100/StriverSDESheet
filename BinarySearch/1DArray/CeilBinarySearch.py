def ceilingInSortedArray(n, x, arr):
    if x > arr[n-1]:
        return -1
    # If no answer exist
    start = 0
    end = n-1
    while start <= end:
        mid = start+(end-start)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid+1
        else:
            end = mid-1
    return arr[start]