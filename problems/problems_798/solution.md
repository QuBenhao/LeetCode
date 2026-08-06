# [Python/Java/JavaScript/Go] 差分数组

> slug: pythonjavajavascriptgo-chai-fen-shu-zu-b-xhvy
> date: 2022-03-08
> tags: Go, Java, JavaScript, Python, Python3
> question: Smallest Rotation with Highest Score (smallest-rotation-with-highest-score)
> url: https://leetcode.cn/problems/smallest-rotation-with-highest-score/solutions/VnNi6u/pythonjavajavascriptgo-chai-fen-shu-zu-b-xhvy/

---
### 解题思路
根据题意，可以写出如下暴力代码
```python3
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        diff = [num - i for i, num in enumerate(nums)]
        # num - i ===> num - (i - k) % len(nums)
        ans, mx = 0, sum(d <= 0 for d in diff)
        for k in range(1, len(nums)):
            if (s := sum(num - (i - k) % len(nums) <= 0 for i, num in enumerate(nums))) > mx:
                ans, mx = k, s
        return ans
```

坐标i和数字num都对k最终是否使该位变为小于等于0做出了贡献，且k在连续变动时，这个差值也是连续变动的。
那么有没有一种办法在不知道k的情况下，优先计算什么范围的k会使i和num最终计算差异满足题目呢？

一个数num,最终和坐标差小于等于0，只有一个范围，那就是坐标在`[num, n-1]`之间，而坐标在`[0, num-1]`之间时差显然会大于0。
这就好办了，我们可以根据这个范围和i的取值，模拟出什么样的k会满足题意。

分类讨论:
当i最开始的位置在`[num, n-1]`之间时，不移动本身就会对答案作出一个贡献，即`diff[0]+=1`；
当k逐渐变大时，i会向左移动出num，那个时候对答案不作出贡献了，即`diff[i - num + 1] -= 1`；
持续移动超过最左端`0`以后会回到`n-1`，又会对答案作出贡献，即`diff[i + 1] += 1`。

当i最开始的位置在`[0, num - 1]` 之间时，不移动本身不会对答案作出贡献。移动超过最左端`0`回到`n-1`，会对答案作出贡献，即`diff[i + 1] += 1`；
当继续移动，超过`num`回到`[0, num - 1]` 之间时，又不会再对答案做出贡献了，即`diff[i - num + n + 1] -= 1`。

我们只需要对diff进行遍历，维护每个时刻有多少个坐标满足差小于等于0，最终返回最大且最小的k即可。


### 代码

```Python3 []
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [0] * (n + 1)
        # num ---> n - 1
        for i, num in enumerate(nums):
            if i >= num:
                diff[0] += 1
                diff[i - num + 1] -= 1
                diff[i + 1] += 1
            else:
                diff[i + 1] += 1
                diff[i - num + n + 1] -= 1
        ans = cur = mx = 0
        for i in range(n):
            cur += diff[i]
            if cur > mx:
                ans, mx = i, cur
        return ans
```
```Java []
class Solution {
    public int bestRotation(int[] nums) {
        int n = nums.length;
        int[] diff = new int[n + 1];
        for(int i = 0; i < n; i++) {
            if(i >= nums[i]) {
                diff[0]++;
                diff[i - nums[i] + 1]--;
                diff[i + 1]++;
            } else {
                diff[i + 1]++;
                diff[i - nums[i] + n + 1]--;
            }
        }
        int ans = 0, cur = 0, max = 0;
        for(int i = 0; i < n; i++) {
            cur += diff[i];
            if(cur > max) {
                ans = i;
                max = cur;
            }
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var bestRotation = function(nums) {
    const n = nums.length
    const diff = new Array(n + 1).fill(0)
    for(let i = 0; i < n; i++) {
        if(i >= nums[i]) {
            diff[0]++
            diff[i - nums[i] + 1]--
            diff[i + 1]++
        } else {
            diff[i + 1]++
            diff[i - nums[i] + n + 1]--
        }
    }
    let ans = 0, cur = 0, max = 0
    for(let i = 0; i < n; i++) {
        cur += diff[i]
        if(cur > max) {
            ans = i
            max = cur
        } 
    }
    return ans
};
```
```Go []
func bestRotation(nums []int) (ans int) {
    n := len(nums)
    diff := make([]int, n + 1)
    for i := 0; i < n; i++ {
        if num := nums[i]; i >= num {
            diff[0]++
            diff[i - num + 1]--
            diff[i + 1]++
        } else {
            diff[i + 1]++
            diff[i - num + n + 1]--
        }
    }
    for i, cur, max := 0, 0, 0; i < n; i++ {
        cur += diff[i]
        if cur > max {
            ans, max = i, cur
        }
    }
    return
}
```