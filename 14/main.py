###################################################
######	14. Longest Common Prefix	###########
###################################################


'''
The solution is a simple sweep. As the common prefix is over array it should be present in all strings inside an array. Compare the first string with the second to find the prefix then compare that prefix with the third and so on. As the length of string can be as long as we want to, this problem has a pseudopolynomial time complexity
Time Complexity: O(n) As we look at each string once for comparison
Space Complexity: O(1) As we only store the prefix
'''

def helper(str1, str2):
    str1, str2 = sorted((str1,str2), key = len)
    for i,c in enumerate(str1):
        if str2[i]!=c:
            return str2[:i]
    return str1
if not strs: return ""
commonpref = strs[0]
for string in strs[1:]:
    commonpref = helper(commonpref, string)
return commonpref


