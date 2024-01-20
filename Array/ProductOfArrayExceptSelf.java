public class ProductOfArrayExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];

        // Calculate the product of all elements to the left of each index
        int prefixProduct = 1;
        for (int i = 0; i < n; i++) {
            ans[i] = prefixProduct;
            prefixProduct *= nums[i];
        }

        // Calculate the product of all elements to the right of each index
        int suffixProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            ans[i] *= suffixProduct;
            // Pehle suffix product se multiply kia and baad mei suffix product ko current
            // element se
            // Trick yahi hai pehle multiply karo without and then suffix product ko badha
            // do
            // for the next iteration.
            suffixProduct *= nums[i];
        }

        // Time Complexity-O(N)
        // Space Complexity-O(N)

        return ans;
    }
}
