##########################################################
############	12. Integer to Roman	##################
##########################################################


'''
The problem is pretty straightforrward to the way we do it. It is required to store a references of roman and corresponding integers and divide the original number by largest to smallest roman to generate the roman string
Time Complexity: O(1) because there are only limited number of roman letters in numbering system
Space Complexity: O(1) because there is a limited number of roman characters a number can have
'''
dic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', \
             100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',\
             9: 'IX', 5: 'V', 4: 'IV', 1: 'I'} 
        
ans = ""
        
for i,v in dic.items():
  ans += (num//i) * v
  num %= i
        
return ans
