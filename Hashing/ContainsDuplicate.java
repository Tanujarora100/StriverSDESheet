package Hashing;

import java.util.HashMap;
import java.util.Map;

public class ContainsDuplicate {

    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++)
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        boolean result = false;
        for (Map.Entry<Integer, Integer> entry : map.entrySet())
            if (entry.getValue() > 1)
                result = true;

        return result;
    }
}
