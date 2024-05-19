class Solution {

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

    private void dfs(int[] nums, List<List<Integer>> ans, int x) {
        if (x == nums.length - 1) {
            ans.add(Arrays.stream(nums).boxed().toList());
            return;
        }
        for (int i = x; i < nums.length; i++) {
            swap(nums, x, i);
            dfs(nums, ans, x + 1);
            swap(nums, x, i);
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        dfs(nums, ans, 0);
        return ans;
    }
}