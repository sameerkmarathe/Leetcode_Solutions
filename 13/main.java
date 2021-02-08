/**
*
*		13. Roman to Integer
*
**/

/*

Purely opposite process of the previous problem. Here we have the smallest roman as the reference, we traverse the Roman string in reverse order to check if the string has crossed into bigger domain(exploiting the rules of roman number writing) and subsequently get the number corresponding the current character in observation
Time Complexity : O(length of roman string) because we iterate the string
Space Complexity: O(1) because we just have integer to update and return

*/

class Solution {
    public int romanToInt(String s) {
        if (s == null || s.length() == 0)
		return -1;
	HashMap<Character, Integer> map = new HashMap<Character, Integer>(){{
        
        put('I', 1);
	put('V', 5);
	put('X', 10);
	put('L', 50);
	put('C', 100);
	put('D', 500);
	put('M', 1000);
        
        
    }};
	
	int len = s.length(), result = map.get(s.charAt(len - 1));
	for (int i = len - 2; i >= 0; i--) {
		if (map.get(s.charAt(i)) >= map.get(s.charAt(i + 1)))
			result += map.get(s.charAt(i));
		else
			result -= map.get(s.charAt(i));
	}
	return result;
    }
}
