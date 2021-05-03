############################################################
#########	43. Multiply Strings	####################
############################################################


'''
The process remains the same at the core. Multiply and carry forward. Use array to store the result and join the string later
Time Complexity:O(n) where n is the length of longest string
Space Complexity: O(n) as we use array equivalent or one length more than longest string 
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        for i, v1 in enumerate(reversed(num1)):
            for j, v2 in enumerate(reversed(num2)):
                int1 = ord(v1) - ord('0')
                int2 = ord(v2) - ord('0')
                res[i + j] += int1 * int2
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
        while len(res) > 1 and res[-1] == 0: res.pop()
        return ''.join(str(v) for v in res)[::-1]
