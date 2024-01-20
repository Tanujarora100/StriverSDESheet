class PlusOne:
    def plusOne(self, digits):
        # Start with a carry of 1
        carry = 1
        
        # Iterate through the digits from right to left
        for i in range(len(digits) - 1, -1, -1):
            # Add the carry to the current digit
            digits[i] += carry
            # Update the carry for the next iteration
            carry = digits[i] // 10
            # Update the current digit to be within 0-9
            digits[i] %= 10

        # If there is a carry after the loop, create a new array
        if carry != 0:
            result = [carry] + digits
            return result

        # Return the original digits list
        return digits

