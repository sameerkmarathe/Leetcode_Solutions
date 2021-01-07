#############################################################
#############		7.Reverse Integer	#############
#############################################################


'''
This problem is trivial if you think of the string to integer conversion. But there is a catch!, the number can be negative and in this case the
conversion will not work. A very simple workaround is to store the 'sign' of the number,
reverse the arithmetic part of the number and reinstate the sign. 
Time Complexity: O(n) where n is the length of the integer
Space complexity: O(n) as we store a copy of integer to reverse it.
'''

## Store the sign of the number
s = (x > 0) - (x < 0)
## Do the reversing on the numeric part
r = int(str(s*x)[::-1])
## Stay in the bounds and return the number with sign
return s*r * (r < 2**31)


