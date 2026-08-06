# [Python/Java/JavaScript/Go] 哈希模拟

> slug: pythonjavajavascriptgo-ha-xi-mo-ni-by-hi-61q8
> date: 2022-02-08
> tags: Go, Java, JavaScript, Python, Python3
> question: Count Number of Pairs With Absolute Difference K (count-number-of-pairs-with-absolute-difference-k)
> url: https://leetcode.cn/problems/count-number-of-pairs-with-absolute-difference-k/solutions/7E4Dfj/pythonjavajavascriptgo-ha-xi-mo-ni-by-hi-61q8/

---
### 解题思路
以前做过一个简化版，统计i、j且nums[i] + nums[j] = target的个数，本题只是增加绝对值其实本质没有区别，
$\lvert nums[i] - nums[j] \rvert = k$
绝对值拆分可得
$nums[i] - nums[j] = k$或者$nums[j] - nums[i] = k$
也就是对于$nums[j]$，我们需要知道$nums[j] + k$和$nums[j] - k$有多少个（这样就知道对应的$nums[i]$的个数）

### 代码

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

由于数据范围小，可以使用数组作为哈希表提速
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