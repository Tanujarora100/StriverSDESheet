import java.util.HashSet;

public class HappyNumber {

    public boolean isHappy(int n) {
        // Create a HashSet to store the numbers we have seen before
        HashSet<Integer> seenNumbers = new HashSet<>();

        // Continue looping until we encounter a number we have seen before
        while (!seenNumbers.contains(n)) {
            // Add the current number to the set of seen numbers
            seenNumbers.add(n);

            // Calculate the sum of squares of the digits of the current number
            n = sumOfSquare(n);

            // If the sum of squares is 1, the number is happy, so return true
            if (n == 1) {
                return true;
            }
        }
        // If we have looped through and not found a sum of squares of 1, the number is
        // not happy, so return false
        return false;
    }

    // Helper function to calculate the sum of squares of the digits of a number
    private int sumOfSquare(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }

}
