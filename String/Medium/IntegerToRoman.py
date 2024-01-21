class Solution:
    def intToRoman(self, num: int) -> str:
        # Create a dictionary to map integers to Roman numeral strings
        numeral_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        
        # Create a list of integers in descending order to be used for conversion
        stack = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        
        # Initialize an empty list to store the Roman numerals
        ans = []
        
        # Iterate through the integer to convert it to Roman numerals
        while num > 0:
            # If the current integer is greater than the top of the stack, pop the stack
            if stack[-1] > num:
                stack.pop()
            # Otherwise, subtract the top of the stack from the current integer and append the corresponding Roman numeral to the result list
            else:
                num -= stack[-1]
                ans.append(numeral_map[stack[-1]])
        
        # Join the Roman numeral list into a single string and return the result
        return "".join(map(str, ans))
                    