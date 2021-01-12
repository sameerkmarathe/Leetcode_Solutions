###############################################################
###############	10.Regular Expression Matching	###############
###############################################################



'''
This problem is understandable if you have idea about regex matching. Although a linear approach for this problem is difficult due to possibilities of regex arising. So we turn to DP and perform the matching by taking one character extra per iteration from the text
Time Complexity: O(product of string lengths) where strings represent the text and pattern
Space Complexity: O(minimum of length of two string) as we only need to memoize the results of the previous iteration and use it to build the current table. 
Note that this code was formulated from the explaination given in the solution.
'''
lentext = len(text)
lenpat = len(pattern)
prev =  [False] * (lenpat + 1)
nex = [False] * (lenpat + 1)
nex[-1] = True
# print(dp)
for i in range(lentext+1)[::-1]:
    for j in range(lenpat)[::-1]:
        first_match = i < lentext and pattern[j] in [text[i], '.']
        if j+1 < lenpat and pattern[j+1] == '*':
            nex[j] = nex[j+2] or first_match and prev[j]
        else:
            nex[j] = first_match and prev[j+1]
        # print(dp)
    # print(dp)
    prev = [i for i in nex]
    nex = [False] * (lenpat + 1)


return prev[0]
