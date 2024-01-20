#User function Template for python3

def largest( arr, n):
    max_item=0
    for i in range(n):
        if arr[i]>max_item:
            max_item=arr[i]
    return max_item


