# [Python/Java/JavaScript/Go] Simulation with a hash table

> slug: pythonjavajavascriptgo-ha-xi-mo-ni-by-hi-61q8
> date: 2022-02-08
> tags: Go, Java, JavaScript, Python, Python3
> question: Count Number of Pairs With Absolute Difference K (count-number-of-pairs-with-absolute-difference-k)
> url: https://leetcode.cn/problems/count-number-of-pairs-with-absolute-difference-k/solutions/7E4Dfj/pythonjavajavascriptgo-ha-xi-mo-ni-by-hi-61q8/

---
### Approach
I previously solved a simpler version that counts pairs i, j with nums[i] + nums[j] = target. This problem adds an absolute value, but the underlying idea is the same.
$\lvert nums[i] - nums[j] \rvert = k$
Expanding the absolute value gives
$nums[i] - nums[j] = k$ or $nums[j] - nums[i] = k$.
For each $nums[j]$, we therefore need the counts of $nums[j] + k$ and $nums[j] - k$ (which tell us the number of matching $nums[i]$ values).

### Code

```Python3 []
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnts, ans = defaultdict(int), 0
        for num in nums:
            cnts[num], ans = cnts[num] + 1, ans + cnts[num + k] + cnts[num - k]
        return ans
```
```Java []
class Solution {
    public int countKDifference(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        int ans = 0;
        for(int num: nums) {
            ans += map.getOrDefault(num + k, 0) + map.getOrDefault(num - k, 0);
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countKDifference = function(nums, k) {
    const map = new Map()
    let ans = 0
    for(const num of nums) {
        if(map.has(num + k))
            ans += map.get(num + k)
        if(map.has(num - k))
            ans += map.get(num - k)
        if(map.has(num))
            map.set(num, map.get(num) + 1)
        else
            map.set(num, 1)
    }
    return ans
};
```
```Go []
func countKDifference(nums []int, k int) (ans int) {
    cnts := map[int]int{}
    for _, num := range nums {
        ans += cnts[num + k] + cnts[num - k]
        cnts[num]++
    }
    return
}
```

Since the value range is small, an array can serve as a hash table for better performance.
```Java []
class Solution {
    public int countKDifference(int[] nums, int k) {
        int[] cnts = new int[101];
        int ans = 0;
        for(int num: nums) {
            if(num + k < 101)
                ans += cnts[num + k];
            if(num - k > 0)
                ans += cnts[num - k];
            cnts[num]++;
        }
        return ans;
    }
}
```
```Go []
func countKDifference(nums []int, k int) (ans int) {
    cnts := make([]int, 101)
    for _, num := range nums {
        if num + k < len(cnts) {
            ans += cnts[num + k]
        }
        if num - k > 0 {
            ans += cnts[num - k]
        }
        cnts[num]++
    }
    return
}
```
