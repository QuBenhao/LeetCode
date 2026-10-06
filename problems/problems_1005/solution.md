# [Python/Java/JavaScript/Go] Greedy + min-heap or sorting with one traversal

> slug: pythonjavajavascriptgo-zui-xiao-dui-tan-ao63h
> date: 2021-12-02
> tags: Go, Java, JavaScript, Python, Python3
> question: Maximize Sum Of Array After K Negations (maximize-sum-of-array-after-k-negations)
> url: https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/solutions/NbbMQN/pythonjavajavascriptgo-zui-xiao-dui-tan-ao63h/

---
### Approach

We must negate a number k times. If there are more than k negative numbers, negate the k smallest ones to maximize the sum.
If there are fewer than k negative numbers (so the array becomes entirely positive),
use the remaining operations to repeatedly negate the number with the smallest absolute value.
(An even number of negations leaves it unchanged; an odd number is equivalent to negating that smallest number once.)

### Code

```python3
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k and nums:
            if nums[0] < 0:
                heapq.heappush(nums, -heapq.heappop(nums))
                k -= 1
            else:
                if nums[0] and k % 2:
                    heapq.heappush(nums, -heapq.heappop(nums))
                break
        return sum(nums)
```

```Python3 []
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        m, ans = inf, 0
        for num in nums:
            m = min(m, abs(num))
            if num < 0 and k:
                k -= 1
                ans -= num
            else:
                ans += num
        # Subtract the smallest value only when the remaining k is odd (subtract twice its value because it was already added)
        return ans - 2 * m if k and k % 2 else ans
```
```Java []
class Solution {
    public int largestSumAfterKNegations(int[] nums, int k) {
        Arrays.sort(nums);
        int m = 101, ans = 0;
        for(int num: nums){
            m = Math.min(m, Math.abs(num));
            if(num < 0 && k-- > 0)
                ans -= num;
            else
                ans += num;
        }
        return k > 0 && k % 2 != 0 ? ans - 2 * m : ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var largestSumAfterKNegations = function(nums, k) {
    nums.sort((a,b)=>a-b)
    let m = 101, ans = 0
    for(const num of nums){
        m = Math.min(m, Math.abs(num))
        if(num < 0 && k-- > 0)
            ans -= num
        else
            ans += num
    }
    return k > 0 && k % 2 != 0 ? ans - 2 * m : ans
};
```
```Go []
func largestSumAfterKNegations(nums []int, k int) int {
    sort.Ints(nums)
    m, ans := 101, 0
    for _, num := range nums {
        m = minAbs(m, num)
        if num < 0 && k > 0 {
            k--
            ans -= num
        } else {
            ans += num
        }
    }
    if k > 0 && k % 2 == 1 {
        return ans - 2 * m
    }
    return ans
}

func minAbs(a, b int) int {
    if a < 0{
        a = -a
    }
    if b < 0{
        b = -b
    }
    if a > b {
        return b
    }
    return a
}
```

Sorting is optional: maintain the k smallest negative numbers during a traversal.

```Python3
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        window = []
        m, ans = 101, 0
        for num in nums:
            m, ans = min(m, abs(num)), ans + num
            if num < 0:
                heapq.heappush(window, -num)
                if len(window) > k:
                    heapq.heappop(window)
        ans += 2 * sum(window)
        return ans - 2 * m if (n:=len(window)) < k and (k - n) % 2 else ans
```
