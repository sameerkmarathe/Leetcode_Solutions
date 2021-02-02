/**
*	7. Reverse Number
**/

/*
This problem is trivial if you think of the string to integer conversion. But there is a catch!, the$
conversion will not work. A very simple workaround is to store the 'sign' of the number,
reverse the arithmetic part of the number and reinstate the sign. Code is same as the python one with standard libraries
Time Complexity: O(n) where n is the length of the integer
Space complexity: O(n) as we store a copy of integer to reverse it.
*/

class Solution {
    public int reverse(int x) {
        String reverse = new StringBuilder().append(Math.abs(x)).reverse().toString();
try {
    return (x < 0) ? -1 * Integer.parseInt(reverse)  : Integer.parseInt(reversed);
} catch (NumberFormatException e) {
    return 0;
}
    }
}


