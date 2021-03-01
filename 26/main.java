/***
*
*	26. Remove Duplicates from Sorted Array
*
**/

/*
Just replace the elements with non-duplicates
Time Complexity:O(N) number of elements in array is N and visit them once
Space Complexity:O(1) constant space is required to store pointer
*/

class Solution {
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int i = 0;
    for (int j = 1; j < nums.length; j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}
}
