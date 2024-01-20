public class NextPermutation {

    public void nextPermutation(int[] nums) {
        // Find the index of the breakpoint in the array
        int breakIndex = -1;
        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) {
                breakIndex = i;
                break;
            }
        }
        System.out.println(breakIndex);

        // If no breakpoint was found, reverse the entire array in place
        if (breakIndex == -1) {
            int start = 0, end = nums.length - 1;
            while (start < end) {
                int temp = nums[start];
                nums[start] = nums[end];
                nums[end] = temp;
                start++;
                end--;
            }
            return;
        }

        // Find the closest greater element than the element at the breakpoint
        for (int i = nums.length - 1; i > breakIndex; i--) {
            if (nums[i] > nums[breakIndex]) {
                // Swap the element at the breakpoint with the closest greater element
                int temp = nums[i];
                nums[i] = nums[breakIndex];
                nums[breakIndex] = temp;
                break;
            }
        }

        // Reverse the sub-array after the breakpoint to get the next permutation
        int start = breakIndex + 1, end = nums.length - 1;
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}