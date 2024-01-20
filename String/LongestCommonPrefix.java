import java.util.Arrays;

public class LongestCommonPrefix {

    public String longestCommonPrefix(String[] strs) {
        // Sort the array in lexicographic order (alphabetically)
        Arrays.sort(strs);
        String strStart = strs[0];
        String strLast = strs[strs.length - 1];
        int count = 0;

        // Compare characters of the first and last strings
        for (int i = 0; i < strStart.length(); i++) {
            if (strStart.charAt(i) != strLast.charAt(i)) {
                break;
            } else {
                count++;
            }
        }

        if (count == 0) {
            return "";
        } else {
            return strStart.substring(0, count);
        }
    }
}
