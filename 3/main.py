#########################################################################################
##############	3. Longest Substring Without Repeating Characters	#################
#########################################################################################


'''
This problem is pretty trivial when you try to come up with a logic to emulate our brain doing the same thing
There are three key insights in this:
1. Starting from the left, look to the right to till we hit any repeating character
2. When we hit a repeating character jump our observation window to exclude the previous occurance of the same characrer
3. Constantly check for the maximum stretched window i.e. our answer. Note that we can easily store the substring instead of the length as answer here
This is a classic two-pointer problem laced with some book-keeping. The choice for the data structure is the one that can map character to its previous occurance index, quite naturally a hashmap/dictionary
Time Complexity: O(n) as we look at the character only once
Space Compexity: O(1) arguably as the input string can only include 256 unique characters (E-ASCII scheme), resulting in a 256 key-value pair hashmap in worst case.
'''
left = res= 0 
## To store previous occurance of a character
prev_map = dict()
        
for right,character in enumerate(s):
  left = max(prev_map[character] + 1, left) if character in prev_map else left
            
  prev_map[character] = right
            
  res = max(right - left + 1, res)
            
return res
        

