class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> temp = new HashMap<>();
        for(int i = 0; i < nums.length;i++){
            if(temp.containsKey(target-nums[i]))
                return new int[]{temp.get(target-nums[i]),i};
            temp.put(nums[i],i);
        }
        return null;
    }
}
