/**
*
*	4. Median of two sorted arrays
*
*/


/*
To do this problem as quickly as possible, it is necessary to combine two sorted arrays virtually and work on it.
The intuition behind this is explained very well in this blog, referenced for the solution below:
https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46
Also refer to @StefanPochmann for a beautiful solution with same idea.
Time complexity: O(log(lengths of lists)) as we effectively perform a binary search
Space Complexity: O(1) as we use no additional data structure
*/

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {

	if (nums1.length > nums2.length) return findMedianSortedArrays(nums2, nums1);
	
	int m = nums1.length, n = nums2.length;

	int mini = 0, maxi = m , halflen = (m+n+1)/2;
	
	while(mini<=maxi){
	
		int i = (mini+maxi)/2;
		int j = halflen - i;
		
		if (i > 0 && nums1[i-1] > nums2[j]){
			maxi = i - 1;	
		} else if (i < m && nums2[j-1] > nums1[i]) {
			mini = i + 1;
		} else {
			
            int lmax = 0, rmin = 0;
			if (i==0) lmax = nums2[j-1];
			else if (j==0)  lmax = nums1[i-1];
			else lmax = Math.max(nums1[i-1], nums2[j-1]);

			if  ((m+n) % 2 != 0){
				return lmax;
			}
			
			if (i==m) rmin = nums2[j];
			else if(j==n) rmin = nums1[i];
			else rmin = Math.min(nums1[i], nums2[j]);
			
			return (float)(lmax + rmin) / 2.0;
		}

	} 

    return 0;
    }
    
}

