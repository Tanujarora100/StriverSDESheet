package StackAndQueue;

import java.util.ArrayDeque;
import java.util.Deque;

public class CelebrityProblem {

    // User function Template for Java

    // Function to find if there is a celebrity in the party or not.
    int findCelebrity(int[][] partyMatrix, int partySize) {
        // Use a stack to track potential celebrities
        Deque<Integer> potentialCelebrities = new ArrayDeque<>();

        // Populate the stack with all party attendees
        for (int i = 0; i < partySize; i++) {
            potentialCelebrities.push(i);
        }

        // While there is more than one potential celebrity remaining
        while (potentialCelebrities.size() > 1) {
            int personA = potentialCelebrities.pop();
            int personB = potentialCelebrities.pop();
            // If person A knows person B, person A cannot be a celebrity, so person B is
            // pushed back onto the stack
            if (knows(personA, personB, partyMatrix)) {
                potentialCelebrities.push(personB);
            } else {
                // If person A does not know person B, person B cannot be a celebrity, so person
                // A is pushed back onto the stack
                potentialCelebrities.push(personA);
            }
        }
        // The remaining person in the stack is the potential celebrity
        int potentialCelebrity = potentialCelebrities.peek();

        // Verify the potential celebrity
        int zeroCount = 0;
        // Check the row of the potential celebrity for zeros
        for (int i = 0; i < partySize; i++) {
            if (partyMatrix[potentialCelebrity][i] == 0) {
                zeroCount++;
            }
        }
        // If there are non-zero entries in the row, the potential celebrity is not a
        // celebrity
        if (zeroCount != partySize) {
            return -1;
        }

        int oneCount = 0;
        // Check the column of the potential celebrity for ones
        for (int i = 0; i < partySize; i++) {
            if (partyMatrix[i][potentialCelebrity] == 1) {
                oneCount++;
            }
        }
        // If there are not exactly n-1 ones in the column, the potential celebrity is
        // not a celebrity
        if (oneCount != partySize - 1) {
            return -1;
        }

        return potentialCelebrity;
    }

    boolean knows(int a, int b, int[][] M) {
        return M[a][b] == 1;
    }
}
