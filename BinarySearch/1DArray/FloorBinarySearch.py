def floorInSortedArray(n, x, arr):
    if x > arr[n-1]:
        return -1
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
    return arr[end]


A = [2, 4, 8, 6, 15, 16, 17, 19, 21, 22, 23]
X = 27
print(floorInSortedArray(len(A), X, A))