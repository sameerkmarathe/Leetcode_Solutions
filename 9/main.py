###################################################################
###################	9. Palindrome Number	###################
###################################################################

'''
There are traversal ways of solving this problem, but we will first go through an easy hack for python
Time Complexity:O(n) as we convert the integer to string where n is the length of resulting string
Space Complexity:O(1) as we mutate the input we do not use any extra space
'''
x = str(x)
return x[::-1] == x

'''
Coming to the more roboust method for this problem. We traverse half the number. This can be done using string conversion but we will aim to do it without
string conversion.
Time Complexity:O(log(n)) where n has the same definition as before
Space Complexity:O(1) as we use constant amount of memory relative to the input size
Note that this appproach is from leetcode solutions and need some optimization for performance
'''

if x<0 or (not x%10 and x ):
    return False

reverse = 0
while x > reverse:
    reverse = reverse*10 + x%10
    x//=10
return x == reverse or x == reverse//10

