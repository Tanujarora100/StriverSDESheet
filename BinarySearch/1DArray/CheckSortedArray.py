def arraySortedOrNot(self, arr, n):
        flag=True
        for i in range(1,n):
            if arr[i-1]>arr[i]:
                flag=False
        return flag