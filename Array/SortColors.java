public class SortColors {

    // Time Complexity -O(N)
    // Space Complexity -O(1)
    public void sortColors(int[] nums) {
        int mid = 0; // initialize mid pointer to the beginning of the array
        int high = nums.length - 1; // initialize high pointer to the end of the array
        int low = 0; // initialize low pointer to the beginning of the array

        while (mid <= high) { // loop until mid crosses high
            if (nums[mid] == 0) { // if current element is 0
                int temp = nums[low];
                nums[low] = nums[mid];
                nums[mid] = temp;
                low++; // increment low
                mid++; // increment mid
            } else if (nums[mid] == 1) { // if current element is 1
                mid++; // move to the next element
            } else { // if current element is 2
                int temp = nums[high];
                nums[high] = nums[mid];
                nums[mid] = temp;
                high--; // decrement high
            }
        }
    }

}
