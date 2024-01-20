public class LongestPalindromeInString {

public String longestPalindrome(String s) {
    // Initialize variables to keep track of the longest palindrome and its start and end indices
    int longestLength = 0;
    int start = 0, end = 0;

    // Iterate through the input string
    for (int i = 0; i < s.length(); i++) {
        // Handle the case when the current character is the same as the next one
        int left = i - 1;
        while (i < s.length() - 1 && s.charAt(i) == s.charAt(i + 1)) {
            ++i; // Move to the next character if it's the same as the current one
        }

        // Expand the palindrome around the current character
        int right = i + 1;
        while (left >= 0 &&
                right < s.length() &&
                s.charAt(left) == s.charAt(right)) {
            --left; // Expand the left bound
            ++right; // Expand the right bound
        }

        // Update the longest palindrome and its start and end indices if a longer palindrome is found
        if (right - left > longestLength) {
            longestLength = right - left;
            start = left + 1; // Update the start index of the longest palindrome
            end = right; // Update the end index of the longest palindrome
        }
    }

    // Return the longest palindrome substring
    return s.substring(start, end);
}
}
