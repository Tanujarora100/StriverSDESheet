public class MaximumSubarray {

    public int maxSubArray(int[] nums) {
        // Time complexity: O(n) - where n is the length of the input array nums
        // Space complexity: O(1) - constant space used
        if (nums.length == 1)
            return nums[0];
        int sum = 0; // Initialize the sum of subarray
        int max = Integer.MIN_VALUE; // Initialize the maximum sum seen so far

        for (int n : nums) {
            sum += n; // Add the current number to the sum
            max = Math.max(max, sum); // Update the maximum sum seen so far

            // If the current sum is negative, reset it to 0
            if (sum < 0) {
                sum = 0;
            }
        }
        return max; // Return the maximum sum seen in any subarray
    }
}
