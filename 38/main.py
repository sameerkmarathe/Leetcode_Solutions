####################################################
#########	38. Count and Say	############
####################################################



'''
Keep track of the first letter in the sequence and count consecutive occurances.
Once you encounter a new letter you add the previous count and letter to the chain.
Repeat n-1 times (since we seeded the initial '1' case).
 We always update temp after the inner loop since we will never have already added the last sequence.
Time Complexity: O(n) because we need to loop over n letters
Space Complexity: O(n) because we can store n-1 chracters max
'''


class Solution:
    def countAndSay(self, n):
        s = '1'
        for _ in range(n-1):
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count)+let
                    let = l
                    count = 1
            temp += str(count)+let
            s = temp
        return s
