# [Python/Java/TypeScript/Go] DFS + in-place marking

> Author: Benhao
> Date: 2022-07-17
> Upvotes: 26
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
Follow each array value as the next index. Revisiting an index closes a cycle; find the largest cycle.
Start a recursive traversal from each position. Mark visited entries as -1 and continue using their original values until reaching -1.

The array has no duplicate elements, so paths cannot intersect; it consists of separate cycles.


There was a good question in the comments.
Here is the difference between `nums[idx], idx = -1, nums[idx]` and `idx, nums[idx] = nums[idx], -1`:
> Python first evaluates and stores all values on the right-hand side.
> It then assigns the targets on the left in order. If idx is assigned first, nums[idx] no longer refers to the position you intended,
> because idx has changed. The target is looked up using idx; it is not an independently fixed variable.

### Code

```Python3 []
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def dfs(idx: int) -> int:
            # A visited position ends the cycle; return to calculate its length
            if nums[idx] == -1:
                return 0
            # Save the next index and mark this position as visited
            nxt, nums[idx] = nums[idx], -1
            return 1 + dfs(nxt)
        
        # Find the largest cycle starting from an index
        return max(dfs(i) for i in range(len(nums)))
```
```Java []
class Solution {
    public int arrayNesting(int[] nums) {
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            ans = Math.max(ans, dfs(nums, i));
        }
        return ans;
    }

    private int dfs(int[] nums, int idx) {
        if (nums[idx] == -1) {
            return 0;
        }
        int nxt = nums[idx];
        nums[idx] = -1;
        return 1 + dfs(nums, nxt);
    }
}
```
```TypeScript []
function arrayNesting(nums: number[]): number {
    const dfs = (idx: number): number => {
        if (nums[idx] == -1) {
            return 0
        }
        let nxt = nums[idx]
        nums[idx] = -1
        return 1 + dfs(nxt)
    }
    let ans = 0
    for (let i = 0; i < nums.length; i++) {
        ans = Math.max(ans, dfs(i))
    }
    return ans
};
```
```Go []
func arrayNesting(nums []int) (ans int) {
    var dfs func (idx int) int
    dfs = func(idx int) int {
        if nums[idx] == -1 {
            return 0
        }
        nxt := nums[idx]
        nums[idx] = -1
        return 1 + dfs(nxt)        
    }
    for i := 0; i < len(nums); i++ {
        if v := dfs(i); v > ans {
            ans = v
        }
    }
    return
}
```

Iterative version
```python3
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            idx, cur = i, 0
            while nums[idx] != -1:
                nums[idx], idx, cur = -1, nums[idx], cur + 1
            ans = max(ans, cur)
        return ans
```
