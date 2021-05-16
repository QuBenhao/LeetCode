class Solution {
    public int[] sortedSquares(int[] nums) {
        int start = 0, left = 0, right = 0, index = 0, n = nums.length;
        int[] result = new int[n];
        for(;start<n;start++){
            if(nums[start] >= 0)
                break;
        }
        left = start - 1;
        right = start;
        while(left>=0 || right < n){
            if(left<0 || (right < n && nums[right] <= - nums[left])){
                result[index] = nums[right] * nums[right];
                right++;
            }else{
                result[index] = nums[left] * nums[left];
                left--;
            }
            index ++;
        }
        return result;
    }
}
