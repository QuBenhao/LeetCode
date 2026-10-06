# [Python/Java/TypeScript/Go] Greedy

> slug: -by-himymben-f1pv
> date: 2022-08-03
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Minimum Subsequence in Non-Increasing Order (minimum-subsequence-in-non-increasing-order)
> url: https://leetcode.cn/problems/minimum-subsequence-in-non-increasing-order/solutions/zQwrBN/-by-himymben-f1pv/

---
### Approach
`该子序列的元素之和 严格 大于未包含在该子序列中的各元素之和`
The sum of elements outside the subsequence is the total sum minus the subsequence sum.
Thus, a valid subsequence must have a sum strictly greater than half the total.

To minimize its length, greedily choose the largest numbers: this exceeds half the total using the fewest elements.

### Code

```Python3 []
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        presum = [0] + list(accumulate(nums))
        return nums[:bisect_left(presum, presum[-1] // 2 + 1)]
```
```Java []
class Solution {
    public List<Integer> minSubsequence(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int[] presum = new int[n + 1];
        for (int i = 0; i < nums.length; i++) {
            presum[i + 1] = presum[i] + nums[n - 1 - i];
        }
        int left = 0, right = n, target = presum[n] / 2 + 1;
        while(left < right) {
            int mid = left + right >> 1;
            if (presum[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        List<Integer> list = new ArrayList<>(left);
        for (int i = 0; i < left; i++) {
            list.add(nums[n - 1 - i]);
        }
        return list;
    }
}
```
```TypeScript []
function minSubsequence(nums: number[]): number[] {
    nums.sort((a, b) => b - a)
    const n = nums.length
    const presum = new Array(n + 1).fill(0)
    for (const [i, num] of nums.entries()) {
        presum[i + 1] = presum[i] + num
    }
    let left = 0, right = n
    const target = (presum[n] >> 1) + 1
    while (left < right) {
        const mid = (left + right) >> 1
        if (presum[mid] < target) {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return nums.slice(0, left)
};
```
```Go []
func minSubsequence(nums []int) []int {
    sort.Sort(sort.Reverse(sort.IntSlice(nums)))
    n := len(nums)
    presum := make([]int, n + 1)
    for i, num := range nums {
        presum[i + 1] = presum[i] + num
    }
    left := 0
    for right, target := n, presum[n] / 2 + 1; left < right; {
        mid := (left + right) / 2
        if presum[mid] < target {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return nums[:left]
}
```

### Complexity
Time complexity: $n logn$
