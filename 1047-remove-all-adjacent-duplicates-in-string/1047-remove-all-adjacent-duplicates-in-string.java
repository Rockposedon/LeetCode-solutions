public class Solution {
    public String removeDuplicates(String s) {
        
        // Use StringBuilder to build the result
        StringBuilder result = new StringBuilder();
        
        // Iterate through each character in the string
        for (char c : s.toCharArray()) {
            // If the result is not empty and the last character is the same as the current one
            if (result.length() > 0 && result.charAt(result.length() - 1) == c) {
                // Remove the last character from the result
                result.deleteCharAt(result.length() - 1);
            } else {
                // Add the current character to the result
                result.append(c);
            }
        }
        
        return result.toString();
    }
}