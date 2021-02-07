/**
*
*	13. Integer to Roman
*
**/



/*
The problem is pretty straightforrward to the way we do it. It is required to store a references of roman and corresponding integers and divide the original number by largest to smallest roman to generate the roman string
Time Complexity: O(1) because there are only limited number of roman letters in numbering system
Space Complexity: O(1) because there is a limited number of roman characters a number can have
Note:Java maps do not have order, so we will keep two arrays
*/


class Solution {
    public static String intToRoman(int num){
	if (num < 1 || num > 3999) return "";
	
	StringBuilder result = new StringBuilder();
	
	String[] roman = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
	int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
	
	int i = 0;
            //iterate until the number becomes zero, NO NEED to go until the last element in roman array
	while (num >0) {
		while ( num >= values[i]) {
			num -= values[i];
			result.append(roman[i]);
		}
		i++;
	}
	return result.toString();
}
}

