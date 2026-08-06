# [Python/Java/JavaScript/Go] 贪心 + 最小堆 or 排序一次遍历

> slug: pythonjavajavascriptgo-zui-xiao-dui-tan-ao63h
> date: 2021-12-02
> tags: Go, Java, JavaScript, Python, Python3
> question: Maximize Sum Of Array After K Negations (maximize-sum-of-array-after-k-negations)
> url: https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/solutions/NbbMQN/pythonjavajavascriptgo-zui-xiao-dui-tan-ao63h/

---
### 解题思路

由于我们必须反转k次，那么有不止k个负数的话，我们要反转里面最小的k个，这样最大。
有不到k个负数的话（数组会变为全部为正），
剩下的次数反复反转所有数里面绝对值最小的那个
（如果偶数次负负得正所以不变，奇数次相当于只反转一次最小的那个）

### 代码

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
        # 只有一种情况我们需要减去最小的那个，k多余了且是奇数（由于已经加进去了所以要减2倍）
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

不排序也可以，遍历维护k个最小的负数

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
