/*

		3. Longest Substring Without Repeating Characters

*/

// Please refer to the python file for more information about the approach

int length = s.length(), ans = 0;


// To cater for extended ASCII
int[] indexArray = new int[256]; 

for (int j = 0, i = 0; j < length; j++) {
    i = Math.max(i, indexArray[s.charAt(j)]);
    ans = Math.max(j - i + 1, ans);
    indexArray[s.charAt(j)] = j + 1;
}
return ans;
