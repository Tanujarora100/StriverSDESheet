public class PlusOne {
    public int[] plusOne(int[] digits) {
        // Start with a carry of 1
        int carry = 1;
        // Iterate through the digits from right to left
        for (int i = digits.length - 1; i >= 0; i--) {
            // Add the carry to the current digit
            digits[i] += carry;
            // Update the carry for the next iteration
            carry = digits[i] / 10;
            // Update the current digit to be within 0-9
            digits[i] %= 10;
        }

        // If there is a carry after the loop, we need to create a new array
        if (carry != 0) {
            int[] result = new int[digits.length + 1];
            result[0] = carry;
            // Copy the original digits to the result array
            System.arraycopy(digits, 0, result, 1, digits.length);
            return result;
        }

        // Return the original digits array
        return digits;
    }
}
