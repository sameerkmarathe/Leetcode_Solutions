###########################################
###########	1. Two Sum	###########
###########################################


'''
There are two approaches to this problem. We will go through them one by one.
'''

'''
The first approach is brute force where for each element we will iterate through the list and check if the respective number exists in the repository.
Time Complexity: O(n^2) because of two loops
Space Complexity: O(1) because we do not use any extra memory
'''

'''
for i , num in enumerate(nums):
            for j, another in enumerate(nums):
                if num + another == target and i != j:
                    return [i,j]
'''

'''
The second more elegant approach uses hashmap. The hashmap is dynamically built as we go to allow for duplicates.
Time Compleixity: O(n) as we only do one pass over the list
Space Complexity: O(n) as we keep a hashmap for reference
'''
ind_dict = {}
for i,num in enumerate(nums):
  if target-num in ind_dict:
    return [i, ind_dict[target-num]]
  else:
    ind_dict[num] = i

