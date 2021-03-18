##########################################################
#########	32. Longest Valid Parantheses	##########
##########################################################



'''
The approach is to have a stack and and push indices of one type of braces in.
If the opposing brace comes in you compare with the index currently in and capture the length difference as max length
Time Complexity: O(n) because we iterate over n elements
Space Complexity: O(n) because we store n indices in worst case
'''

lass Solution:
    def longestValidParentheses(self, s: str) -> int:
        left,right, maxlength = 0, 0, 0;
        for i in range(len(s)): 
            if s[i] == '(':
                left+=1
            else:
                right+=1
            
            if left == right:
                maxlength = max(maxlength, 2 * right)
            elif right >= left:
                left = right = 0
                       
        left,right = 0, 0;
        for i in range(len(s))[::-1]: 
            if s[i] == '(':
                left+=1
            else:
                right+=1
            
            if left == right:
                maxlength = max(maxlength, 2 * left)
            elif left >= right:
                left = right = 0
        return maxlength
