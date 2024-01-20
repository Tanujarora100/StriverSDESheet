def isHappy(n):
    # Create a set to store the numbers we have seen before
    seen_numbers = set()
    while n not in seen_numbers:
        # Add the current number to the set of seen numbers
        seen_numbers.add(n)
        # Calculate the sum of squares of the digits of the current number
        n = sum_of_square(n)
        # If the sum of squares is 1, the number is happy, so return True
        if n == 1:
            return True
    # If we have looped through and not found a sum of squares of 1, the number is not happy, so return False
    return False

def sum_of_square(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit * digit
        n //= 10
    return sum