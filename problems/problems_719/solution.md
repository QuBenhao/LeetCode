# [Python/Java/TypeScript/Go] 值域二分

> slug: pythonjavatypescriptgo-zhi-yu-by-himymbe-tc01
> date: 2022-06-14
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Find K-th Smallest Pair Distance (find-k-th-smallest-pair-distance)
> url: https://leetcode.cn/problems/find-k-th-smallest-pair-distance/solutions/mh6c3k/pythonjavatypescriptgo-zhi-yu-by-himymbe-tc01/

---
### 解题思路
对于第k小很常见的一个解法是对答案的范围进行二分。本题距离越大，一个点可以到的其他点的个数是单调不减的，满足二段性。

对每个答案校验它是否为第k小，需要统计有多少对儿点小于该距离，同样可以对每个点进行二分。或使用滑窗双指针的思想。

### 代码

```python3
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def helper(dist: int) -> int:
            return sum(bisect_right(nums, num + dist) - 1 - i for i, num in enumerate(nums))

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0] + 1), True, key=lambda x: helper(x) >= k)
```
```Python3 []
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def helper(dist: int) -> int:
            ans = i = 0
            for j, num in enumerate(nums):
                # 枚举每个右端点的左端点
                while num - nums[i] > dist:
                    i += 1
                ans += j - i
            return ans

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0] + 1), True, key=lambda x: helper(x) >= k)
```
```Java []
class Solution {
    public int smallestDistancePair(int[] nums, int k) {
        Arrays.sort(nums);
        int left = 0, right = nums[nums.length - 1] - nums[0] + 1;
        while (left < right) {
            int mid = left + right >> 1;
            if (count(nums, mid) >= k) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private int count(int[] nums, int dist) {
        int ans = 0;
        for (int i = 0, j = 0; j < nums.length; j++) {
            while (nums[j] - nums[i] > dist) {
                i++;
            }
            ans += j - i;
        }
        return ans;
    }
}
```
```TypeScript []
function smallestDistancePair(nums: number[], k: number): number {
    const count = (dist: number): number => {
        let ans = 0
        for (let i = 0, j = 0; j < nums.length; j++) {
            while (nums[j] - nums[i] > dist) {
                i++
            }
            ans += j - i
        }
        return ans
    }
    
    nums.sort((a, b) => a - b)
    let left = 0, right = nums[nums.length - 1] - nums[0] + 1
    while (left < right) {
        const mid = (left + right) >> 1
        if (count(mid) >= k) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return left
};
```
```Go []
func smallestDistancePair(nums []int, k int) (left int) {
    count := func(dist int) (ans int) {
        for i, j := 0, 0; j < len(nums); j++ {
            for nums[j] - nums[i] > dist {
                i++
            }
            ans += j - i
        }
        return
    }

    sort.Ints(nums)
    for right := nums[len(nums) - 1] - nums[0] + 1; left < right; {
        mid := (left + right) >> 1
        if count(mid) < k {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return
}
```