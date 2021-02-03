/**
*
*
*		8. String to Integer(atoi)
*
*
**/





/*
This is somewhat mundane problem compared to the previous ones. Regardless is, we can create a solution usin$
It is much easier to perform the conversion ourselves.
Time Complexity: O(n) As we iterate the string of length n
Space Complexity: O(1) as we store the resulting integer in variable
*/

class Solution {
    public int myAtoi(String s) {
        
	int index = 0, sign = 1, total = 0;
    
    if(s.length() == 0) return 0;

    
    while(str.charAt(index) == ' ' && index < str.length())
        index ++;

    
    if(str.charAt(index) == '+' || str.charAt(index) == '-'){
        sign = str.charAt(index) == '+' ? 1 : -1;
        index ++;
    }
    
    
    while(index < str.length()){
        int digit = str.charAt(index) - '0';
        if(digit < 0 || digit > 9) break;

        
        if(Integer.MAX_VALUE/10 < total || Integer.MAX_VALUE/10 == total && Integer.MAX_VALUE %10 < digit)
            return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;

        total = 10 * total + digit;
        index ++;
    }
    return total * sign;
}

}
