package Hashing;

import java.util.HashMap;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        // Create a HashMap to store the difference between the target and each element
        // of the nums array
        HashMap<Integer, Integer> map = new HashMap<>();
        // Create an array to store the result
        int result[] = new int[2];
        // Iterate through the nums array
        for (int i = 0; i < nums.length; i++) {
            // Check if the map contains the difference between the target and the current
            // element
            if (map.containsKey(target - nums[i])) {
                // If found, store the index of the difference and the current index in the
                // result array
                result[0] = map.get(target - nums[i]);
                result[1] = i;
            }
            // Store the current element and its index in the map
            map.put(nums[i], i);
        }
        // Return the result array
        return result;
    }
}
