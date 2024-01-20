import java.util.Arrays;

public class LargestNumber {

    public String largestNumber(int[] nums) {
        String[] numStr = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            numStr[i] = String.valueOf(nums[i]);
        }

        Arrays.sort(numStr, (a, b) -> (b + a).compareTo(a + b));

        StringBuilder result = new StringBuilder("");
        for (String str : numStr) {
            result.append(str);
        }

        String finalResult = result.toString();
        return finalResult.startsWith("0") ? "0" : finalResult;
    }
    // Time complexity: O(n log n) where n is the number of elements in the input
    // array.
    // Space complexity: O(n) where n is the number of elements in the input array.
}
