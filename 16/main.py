########################################################
###########	16. 3Sum Closest	################
########################################################


'''
The problem is on similar lines as 3Sum, it is just the difference that we need to hold the sum instead of the actual triplet that gives the sum. We first sort the array. Then for each element we check the elements ahead if they give any improvement. If the sum we received is more than the target then we lower our expectations by reducing the high point, vice versa. If the difference is zero we break as we cannot get any better.
Time Complexity: O(n^2) as we check all other elements for a given element
Space Complexity: O(1) as we only store the difference.
'''

diff=float('inf')
nums.sort()
for i in range(len(nums)):
    lo, hi = i + 1, len(nums) - 1
    while (lo < hi):
        sum = nums[i] + nums[lo] + nums[hi]
        if abs(target - sum) < abs(diff):
            diff = target - sum
        if sum < target:
            lo += 1
        else:
            hi -= 1
    if diff == 0:
        break
return target - diff

