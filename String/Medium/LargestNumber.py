from functools import cmp_to_key

class LargestNumber:
    def largestNumber(self, nums):
        # Convert numbers to strings
        num_str = list(map(str, nums))

        # Custom comparator for sorting by concatenating a and b in different orders and comparing the results
        def compare(a, b):
            return (b + a) - (a + b)

        # Sort the list of numbers as strings using the custom comparator
        num_str.sort(key=cmp_to_key(compare))

        # Concatenate the sorted strings to form the largest number
        result = ''.join(num_str)

        # Remove leading zeros, or return '0' if result is zero
        final_result = result.lstrip('0') or '0'

        return final_result
