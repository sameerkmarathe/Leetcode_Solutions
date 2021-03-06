##########################################################
#############	28. Implement strStr()	##################
##########################################################


'''
It is only a matter of using str.find to perform the operation
Time Complexity:O(n) finding the index involves iterating the bigger string, n is the length of haystack
Space Complexity:O(1) we only need to store the index
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif not haystack:
            return -1
        return haystack.find(needle)
        
