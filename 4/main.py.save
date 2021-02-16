################################################################
#############	4. Median of Two Sorted Arrays	################
################################################################


'''
To do this problem as quickly as possible, it is necessary to combine two sorted arrays virtually and work on it.
The intuition behind this is explained very well in this blog, referenced for the solution below:
https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46
Also refer to @StefanPochmann for a beautiful solution with same idea.
Time complexity: O(log(lengths of lists)) as we effectively perform a binary search
Space Complexity: O(1) as we use no additional data structure
'''

nums1, nums2 = sorted((nums1,nums2), key = len)
m, n = len(nums1), len(nums2)
        

mini, maxi, half_len = 0, m, (m + n + 1) // 2
while mini <= maxi:
            
  i = (mini + maxi) // 2
  j = half_len - i
                  
  if i > 0 and nums1[i-1] > nums2[j]:
  # Too many elements taken from first array
    maxi = i - 1
  
  elif i < m and nums2[j-1] > nums1[i]:
  ## Go to right in the first array
    mini = i + 1
            
  else:
  # This looks the right i
    if i == 0: lmax = nums2[j-1]
    elif j == 0: lmax = nums1[i-1]
    else: lmax = max(nums1[i-1], nums2[j-1])

    if (m + n) % 2:
      return lmax

    if i == m: rmin = nums2[j]
    elif j == n: rmin = nums1[i]
    else: rmin = min(nums1[i], nums2[j])

    return (lmax + rmin) / 2.0

