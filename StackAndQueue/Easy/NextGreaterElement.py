def nextLargerElement(arr, n):
    st = []
    ans = []
    st.append(-1)
    for i in range(n-1, -1, -1):
        while st[-1] <= arr[i] and len(st) > 1:
            st.pop()
        ans.append(st[-1])
        st.append(arr[i])
    return list(reversed(ans))


A = [1, 2, 3, 4]
print(nextLargerElement(A, len(A)))