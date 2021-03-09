/***
*
*	29. Divide Two Integers
*
**/


/*
Refer to python file for runtime complexities
*/

class Solution {
    public int divide(int dividend, int divisor) {
        
        
        if (divisor == -1 && dividend == Integer.MIN_VALUE)
            return Integer.MAX_VALUE;
        
        int cnt = 0;
        int a = Math.abs(dividend), b = Math.abs(divisor);
        
        while (a - b >= 0) {
            cnt++;
            a -= b;
        }
        
        return (dividend >= 0 && divisor >= 0) || (dividend <= 0 && divisor <= 0) ? cnt : -cnt;   
    }
}
