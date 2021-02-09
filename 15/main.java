/**
*
*	15. 3Sum
*
**/


/*

Sort the array and get the unique ones in. Disregard the duplicate values off the bat
Time complexity: O(n^2) because we perform 2sum every integer unique in the array
Space Complexity: O(n), there can be n/3 triplets unique for the three sum
*/

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
	List<List<Integer>> res = new ArrayList();
        if (nums.length < 3) return res;
        Arrays.sort(nums);
        for(int i = 0; i < nums.length - 2; i++){
            if(nums[i] > 0) break;
            if(i == 0 || (i > 0) && (nums[i] != nums[i-1])){
                int lo = i + 1, hi = nums.length - 1, sum = 0-nums[i];
                while (lo < hi){
                    if (nums[lo] + nums[hi] == sum){
                        res.add(Arrays.asList(nums[i], nums[lo], nums[hi]));
                        while (lo < hi && nums[lo] == nums[lo+1]) lo++;
                        while (lo < hi && nums[hi] == nums[hi-1]) hi--;
                        lo++;
                        hi--;
                    }
                    else if (nums[lo] + nums[hi] < sum) lo++;
                    else hi--;
                }                    
            }
        }
        return res;       
    }
}
