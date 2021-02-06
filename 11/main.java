/**
*
*	11. Container With Most Water
*
**/


/*
Classic two pointer problem. We can brute force to check every combination but this is slow. It is much 
better to encroach the space where we store the water represented as two pointers. 
Note the maximum capacity along the process.
Time Complexity: O(n) because we visit each element once.
Space Complexity: O(1) because we only need constant amount of space to store the information. 
*/

class Solution {
    public int maxArea(int[] height) {
	int ans = 0 left = 0, right = len(height) - 1;
	while (left < right):

    	if (height[left] < height[right]) {
        	ans = Math.max(ans, (right - left) * height[left]);
        	left+=1;
    	} else {
        	ans = Math.max(ans, (right - left) * height[right]);
        	right-=1;
    	}

	return ans;
    }
}
