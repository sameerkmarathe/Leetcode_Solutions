/***
*
*	43. Multiply Strings
*
**/


/*
Please refer to python file for complexity information
*/

class Solution {
    public String multiply(String num1, String num2) {
        int m = num1.length(), n = num2.length();
        int[] ans = new int[m + n];
        for(int i = m - 1; i >= 0; i--) {
            for(int j = n - 1; j >= 0; j--) {
                int mul = (num1.charAt(i) - '0') * (num2.charAt(j) - '0'); 
                int p1 = i + j, p2 = i + j + 1;
                int sum = mul + ans[p2];
                ans[p1] += sum / 10;
                ans[p2] = (sum) % 10;
            }
        }  

        StringBuilder sb = new StringBuilder();
        for(int digit : ans) if(!(sb.length() == 0 && digit == 0)) sb.append(digit);
        return sb.length() == 0 ? "0" : sb.toString();
}
}
