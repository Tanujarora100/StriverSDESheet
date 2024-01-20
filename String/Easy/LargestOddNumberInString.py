class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Start from the end of the number and iterate backwards
        for i in range(len(num) - 1, -1, -1):
            # Get the integer value of the current character
            n = int(num[i])
            # Check if the integer is odd
            if n % 2 != 0:
                # If it's odd, return the substring from the start to the current position
                return num[:i + 1]
        # If no odd number is found, return an empty string
        return ""


