class Solution:
    @staticmethod
    def doUnion(a, n, b, m):
        # Create a set to store unique elements from both arrays
        unique_elements = set()

        # Add elements from array 'a' to the set
        for i in range(n):
            unique_elements.add(a[i])

        # Add elements from array 'b' to the set
        for i in range(m):
            unique_elements.add(b[i])

        # Return the count of unique elements in the set
        return len(unique_elements)

