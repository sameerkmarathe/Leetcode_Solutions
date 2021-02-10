/**
*
*	16. 3Sum Closest
*
**/

/*
The problem is on similar lines as 3Sum, it is just the 
difference that we need to hold the sum instead of the actual triplet 
that gives the sum. We first sort the array. Then for each element 
we check the elements ahead if they give any improvement. 
If the sum we received is more than the target then we lower our expectations by reducing the high point, vice versa. If the difference is zero we break as we cannot get any better.
Time Complexity: O(n^2) as we check all other elements for a given element
Space Complexity: O(1) as we only store the difference.

*/

class Solution {
public int threeSumClosest(int[] nums, int target) {
    int diff = Integer.MAX_VALUE, sz = nums.length;
    Arrays.sort(nums);
    for (int i = 0; i < sz && diff != 0; ++i) {
        int lo = i + 1, hi = sz - 1;
        while (lo < hi) {
            int sum = nums[i] + nums[lo] + nums[hi];
            if (Math.abs(target - sum) < Math.abs(diff))
                diff = target - sum;
            if (sum < target)
                ++lo;
            else
                --hi;
        }
    }
    return target - diff;
}
}
