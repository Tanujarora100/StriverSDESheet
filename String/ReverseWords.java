import java.util.ArrayDeque;

class Solution {
    public String reverseWords(String s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < s.length() && Character.isWhitespace(s.charAt(left))) {
            left++;
        }
        //skip the whitespaces for each of the word 

        while (right >= 0 && Character.isWhitespace(s.charAt(right))) {
            right--;
        }
        //skip the whitespaces for each of the word from the right of the window and then keep moving forward.

        ArrayDeque<String> stack = new ArrayDeque<>();
        while (left <= right) {
            StringBuilder sb = new StringBuilder();
                //use a stack because we need to reverse the words so using a stack is helpful.
            // Build each word
            while (left <= right && !Character.isWhitespace(s.charAt(left))) {
                sb.append(s.charAt(left));
                left++;
            }
            //Stop at a whitespace it means a new word is about to be started

            stack.offer(sb.toString());
            //push that word into the stack.

            while (left <= right && Character.isWhitespace(s.charAt(left))) {
                left++;
            }
            //Keep searching for the next word till the next word is reached.
        }

        StringBuilder result = new StringBuilder();
        while (!stack.isEmpty()) {
            result.append(stack.pollLast());
            if (!stack.isEmpty()) {
                result.append(" ");
                //Add this Space to make sure they are space separated.
            }
        }

        return result.toString();
    }
}