import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GroupAnagrams {

    List<List<String>> groupAnagrams(String[] strs) {
        // If the input array is empty, return an empty list
        if (strs.length == 0)
            return new ArrayList<>();

        // Create a map to store anagrams, with the anagram representation as the key
        // and the list of anagrams as the value
        Map<String, List<String>> anagrams = new HashMap<>();

        // Iterate through each string in the input array
        for (String s : strs) {
            // Create an array to store the count of each character in the string
            int[] count = new int[26];

            // Populate the count array by iterating through each character in the string
            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }

            // Convert the count array to a string to use as the key for the anagrams map
            String key = Arrays.toString(count);

            // If the key is not already in the map, add it with an empty list as the value
            if (!anagrams.containsKey(key)) {
                anagrams.put(key, new ArrayList<>());
            }

            // Add the current string to the list of anagrams for the corresponding key
            anagrams.get(key).add(s);
        }

        // Return a new list containing all the lists of anagrams from the map
        return new ArrayList<>(anagrams.values());
    }
}
