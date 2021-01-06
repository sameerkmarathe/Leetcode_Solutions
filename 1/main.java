/*

		1. Two Sum 

*/

/*
Please refer the python file for more information on the approach
*/

Map<Integer,Integer> indDict = new HashMap<>();
for(int i = 0; i < nums.length; i++) {
    if(indDict.containsKey(target-nums[i])) {
        return new int[]{i, indDict.get(target-nums[i])};

    } else {
        indDict.put(nums[i], i);
    }

}
return null;

