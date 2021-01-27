##############################################################
################	13. Roman to Integer	 #############
##############################################################


'''
Purely opposite process of the previous problem. Here we have the smallest roman as the reference, we traverse the Roman string in reverse order to check if the string has crossed into bigger domain(exploiting the rules of roman number writing) and subsequently get the number corresponding the current character in observation
Time Complexity : O(length of roman string) because we iterate the string
Space Complexity: O(1) because we just have integer to update and return 
'''

roman_dict={'I' : 1,
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000}
ans=0
ref='I'
for i in s[::-1]:
  if roman_dict[i]<roman_dict[ref]:
    ans-=roman_dict[i]
                
  else:
    ans+=roman_dict[i]
  ref=i
return ans
            
