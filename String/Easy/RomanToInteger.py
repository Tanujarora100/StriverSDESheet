class RomanToInteger:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary to store the values of Roman numerals
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # Initialize the total with the value of the last character in the string
        total = values[s[-1]]

        # Iterate through the string from right to left
        for i in range(len(s) - 2, -1, -1):
            # If the current value is less than the next value, subtract it from the total
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                # Otherwise, add it to the total
                total += values[s[i]]

        return total

# Example Usage:
# roman_converter = RomanToInteger()
# result = roman_converter.romanToInt("IX")
# print("Result:", result)
