/***
*
*	42. Trapping Rain Water
*
***/


/*
This is a pure translation of python solution
*/

class Solution {
    public int trap(int[] height) {
        int ans = 0, h1 = 0, h2 = 0;
        for(int i = 0; i < height.length; i++) {
            h1 = Math.max(h1,height[i]);
            h2 = Math.max(h2,height[height.length-i-1]);
            ans = ans + h1 + h2 - height[i];
            }
        return  ans - height.length*h1;
            
    }
}
