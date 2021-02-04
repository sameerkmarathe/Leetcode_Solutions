/**
*
*	9. Palindrome Number
*
**/


/*
Coming to the more roboust method for this problem. We traverse half the number. This can be done using string conversion but we will aim to do it without
string conversion.
Time Complexity:O(log(n)) where n has the same definition as before
Space Complexity:O(1) as we use constant amount of memory relative to the input size
Note that this appproach is from leetcode solutions and need some optimization for performance
*/

class Solution {
    public boolean isPalindrome(int x) {

	if (x<0 || ( x%10 == 0 && x != 0)){
    		return false;
	}

	int reverse = 0;
	while(x > reverse){
    		reverse = reverse*10 + x%10;
    		x/=10;
	}
	return x == reverse || x == reverse/10;
	
        
    }
}


