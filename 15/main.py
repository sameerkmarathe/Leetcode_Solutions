#####################################################
##########	15. 3Sum	#####################
#####################################################



'''
Sort the array and get the unique ones in. Disregard the duplicate values off the bat
Time complexity: O(n^2) because we perform 2sum every integer unique in the array
Space Complexity: O(n), there can be n/3 triplets unique for the three sum
'''
nums.sort()
n, result = len(nums), []

for i in range(n):
  if i > 0 and nums[i] == nums[i-1]: continue

  target = -nums[i]
  beg, end = i + 1, n - 1

  while beg < end:
    if nums[beg] + nums[end] < target:
      beg += 1
    elif nums[beg] + nums[end] > target:
      end -= 1
    else:
      result.append((nums[i], nums[beg], nums[end]))
      beg += 1
      end -= 1

return set(result)
