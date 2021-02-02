/**
*		6. Zigzag Conversion
**/


/*
This problems are actually simple if you just do it the way `you' will do it if asked it. The process is simple,
just have 'numRows' number of buckets to add characters in and normally iterate the string and put characters in bucket.
To take care of zigzag nature hit the reverse gear once you reach the very last buckets or very first.
Time Complexity: O(n) as we iterate each character in string and n is the length of the string
Space Complexity: O(n) Because we store all characters in some buckets
*/

class Solution {
    public String convert(String s, int numRows) {
        if (numRows <= 1 || numRows > s.length() - 1) return s;
        StringBuilder[] sb= new StringBuilder[numRows];
        
        
        int index=0, step=1;
        
        for (int i=0; i < numRows; i++) sb[i]=new StringBuilder();
        
        for (char character: s.toCharArray()){
            sb[index].append(character);
            if (index==0) step = 1;
            if (index==numRows-1) step = -1;
            index += step;
        }
        return String.join("", sb);
    }
}
