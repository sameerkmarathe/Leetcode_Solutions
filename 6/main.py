###############################################################
###############	     6. Zigzag Conversion       ###############
###############################################################

'''
This problems are actually simple if you just do it the way `you' will do it if asked it. The process is simple, just have 'numRows' number of buckets to add characters in and normally iterate the string and put characters in bucket. To take care of zigzag nature hit the reverse gear once you reach the very last buckets or very first.
Time Complexity: O(n) as we iterate each character in string and n is the length of the string
Space Complexity: O(n) Because we store all characters in some buckets
'''

if numRows == 1 or numRows > len(s) -1:
    return s

##Buckets to keep characters in
ans = [""] * numRows

index, step = 0, 1

##reverse the step when you hit edge buckets
stepdict={0:1,numRows-1:-1}

for char in s:
    ans[index] += char

    step = stepdict.get(index,step)

    index += step

return "".join(ans)
