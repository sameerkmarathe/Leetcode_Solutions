################################################################
##############	22. Generate Parantheses	################
################################################################


'''
The key is to not let one bigger than the other. It is done by allowing
the weight of the left and right to be stored recursively.
Time Complexity: O(4^n/sqrt(n)) refer to the problem explaination for the same
Space Complexity: Same as the number of such well formed pairs will be nth catalan number
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)
