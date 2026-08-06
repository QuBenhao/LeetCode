# [Python/Java] 标准二分查找

> slug: pythonjava-biao-zhun-er-fen-cha-zhao-by-k1ob9
> date: 2021-09-05
> tags: Python, Python3
> question: Binary Search (binary-search)
> url: https://leetcode.cn/problems/binary-search/solutions/x2Ajt1/pythonjava-biao-zhun-er-fen-cha-zhao-by-k1ob9/

---
```Python3 []
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return ans if (ans := bisect_left(nums, target)) < len(nums) and nums[ans] == target else -1
```
```Java []
class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length;
        if(nums[n-1] < target)
            return -1;
        for(int l = 0, r = n - 1; l <= r;){
            int mid = (l + r) / 2;
            if(nums[mid] > target)
                r = mid - 1;
            else if(nums[mid] < target)
                l = mid + 1;
            else
                return mid;
        }
        return -1;
    }
}
```