import java.util.Arrays;

public class ValidAnagram {

    public boolean isAnagram(String s, String t) {
        // Create arrays to store the count of each letter in the input strings
        int[] arrayOne = new int[26];
        int[] arrayTwo = new int[26];

        // Iterate through the first input string and update the count of each letter
        for (int i = 0; i < s.length(); i++)
            arrayOne[s.charAt(i) - 'a']++;

        // Iterate through the second input string and update the count of each letter
        for (int i = 0; i < t.length(); i++)
            arrayTwo[t.charAt(i) - 'a']++;

        // Check if the counts of each letter in both arrays are equal
        return Arrays.equals(arrayOne, arrayTwo);
    }
}
