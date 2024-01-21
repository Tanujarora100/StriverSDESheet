class Solution:
    def minValue(self, a, b, n):
        a.sort()
        b.sort(reverse=True)
        cumulative_sum = 0
        for i in range(n):
            cumulative_sum += a[i]*b[i]
        return cumulative_sum