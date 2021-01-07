class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] indexes = new int[2];
        HashMap<Integer,Integer> temp = new HashMap<>();
        for(int i = 0; i < nums.length;i++){
            if(temp.containsKey(target-nums[i])){
                indexes[0] = temp.get(target-nums[i]);
                indexes[1] = i;
                return indexes;
            }
            else{
                temp.put(nums[i],i);
            }
        }
        return indexes;
    }
}
