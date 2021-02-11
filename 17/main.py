#############################################################
#############	17. Letter Combination	#####################
#############################################################


'''
The idea is to backtrack through the map of each digit for combination
Time Complexity: O(3^N×4^M)  is the number of digits in the input that maps to 3 letters and M is the number of digits in the input that maps to 4 and N+M is the total number digits
Space Complexity: Same as above as we can have that many solutions
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if '' == digits: return []
        maps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ret=['']
        for c in digits:
            comb=[]
            for y in ret:
                for x in maps[c]:
                    comb.append(y+x)
            ret=comb
        return ret

