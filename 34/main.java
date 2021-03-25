/**
*
*	34. Find First and Last Position of Element in Sorted Array
*
**/



/*
This solution is mirrored version of python solution. Refer to python solution for approach
*/

public class Solution {
	public int[] searchRange(int[] nums, int target) {
		int start = Solution.firstGreaterEqual(nums, target);
		if (start == nums.length || nums[start] != target) {
			return new int[]{-1, -1};
		}
		return new int[]{start, Solution.firstGreaterEqual(nums, target + 1) - 1};
	}

	private static int firstGreaterEqual(int[] A, int target) {
		int low = 0, high = A.length;
		while (low < high) {
			int mid = low + ((high - low) >> 1);
			
			if (A[mid] < target) {
				low = mid + 1;
			} else {
				high = mid;
			}
		}
		return low;
	}
}     

