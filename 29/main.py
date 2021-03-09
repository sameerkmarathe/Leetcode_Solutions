###########################################################
##########	29. Divide Two Integers	###################
###########################################################


'''
Just use the subtract formula and do the division till divident goes below divisor
Time Complexity:O(log(n)) n being the numerator length
Space Complexity:O(1) we only use constant space
'''

class Solution:
    def divide(self, dividend, divisor):     
        neg=( (dividend < 0) != (divisor < 0) )
        dividend = left = abs(dividend)
        divisor  = div  = abs(divisor)
        Q = 1
        ans = 0
        while left >= divisor:
            left -= div
            ans  += Q 
            Q    += Q
            div  += div
            if left < div:
                div = divisor
                Q = 1
        if neg:
            return max(-ans, -2147483648)
        else:
            return min(ans, 2147483647)
