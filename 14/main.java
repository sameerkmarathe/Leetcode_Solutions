/**
*
*	14. Longest Common Prefix
*
**/


/*
The solution is a simple sweep. As the common prefix is over array 
it should be present in all strings inside an array. 
Compare the first string with the second to find the prefix then 
compare that prefix with the third and so on. 
As the length of string can be as long as we want to, this problem has a pseudopolynomial time complexity
Time Complexity: O(n) As we look at each string once for comparison
Space Complexity: O(1) As we only store the prefix

*/

class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++)
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) return "";
            }        
        return prefix;
    }
}
