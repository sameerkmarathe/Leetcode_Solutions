####################################################################
############	8. String to Integer(atoi)	####################
####################################################################


'''
This is somewhat mundane problem compared to the previous ones. Regardless is, we can create a solution using in-built str function with some modification.
It is much easier to perform the conversion ourselves.
Time Complexity: O(n) As we iterate the string of length n
Space Complexity: O(1) as we store the resulting integer in variable
'''

maxInt = 2147483647
s = s.strip()
if not s:
    return 0
refer = {"+":1,"-":-1 }
sign, i = 1, 0
if s[0] in refer:
    i+=1
    sign = refer[s[0]]
num = 0
for j in range(i, len(s)):
    if not s[j].isdigit() or num > maxInt:
        break
    num = num * 10 + int(s[j])

return min(max(sign * num, -1-maxInt), maxInt)
