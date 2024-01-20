import java.util.HashMap;
import java.util.Map;

public class RomanToInteger {
    
public int romanToInt(String s) {
     // Create a map to store the values of Roman numerals
     Map<Character, Integer> values = new HashMap<>();
     values.put('I', 1);
     values.put('V', 5);
     values.put('X', 10);
     values.put('L', 50);
     values.put('C', 100);
     values.put('D', 500);
     values.put('M', 1000);

     // Initialize the total with the value of the last character in the string
     int total = values.get(s.charAt(s.length() - 1));

     // Iterate through the string from right to left
     for (int i = s.length() - 2; i >= 0; i--) {
         // If the current value is less than the next value, subtract it from the total
         if (values.get(s.charAt(i)) < values.get(s.charAt(i + 1))) {
             total -= values.get(s.charAt(i));
         } else {
             // Otherwise, add it to the total
             total += values.get(s.charAt(i));
         }
     }
     return total;
 }
}

