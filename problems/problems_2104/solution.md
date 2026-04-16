# [Python/Java/JavaScript/Go] 单调栈

> Author: Benhao
> Date: 2022-03-03
> Upvotes: 40
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
参考了[灵老师](https://leetcode.cn/problems/sum-of-subarray-ranges/solution/cong-on2-dao-ondan-diao-zhan-ji-suan-mei-o1op/)和[草莓奶昔](https://leetcode.cn/problems/sum-of-subarray-ranges/solution/dan-diao-zhan-on-by-cao-mei-nai-xi-i-xw3d/)，他们写的都很好很清晰。

题目要求所有区间的最大值减去最小值的和，相当于求每个数作为最大值出现在的区间个数 和 作为最小值出现的区间个数。
最大值维护一个单调递增栈，当当前值比前面的值大时，意味着栈里面的这些小的元素的右边最远到当前值，而栈里面这些小的元素作为最大值始终是它加入时前一个最大值的坐标。
最小值与最大值思路一致，只是逻辑相反。

### 代码

```Python3 []
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans, stack = 0, []
        for i, num in enumerate(nums + [inf]):
            while stack and nums[stack[-1]] < num:
                # 栈顶元素作为最大值的时代结束了, 它作为最大值的区间为它的前一个坐标到当前把它弹出的坐标 
                # 左边选一个作为左端点，右边选一个作为右端点，这个区间上它都是最大值
                # 故出现次数为 组合数 C_l1 * C_r1 
                ans += nums[(j:=stack.pop())] * (i - j) * (j - (stack[-1] if stack else -1))
            stack.append(i)
        stack = []
        for i, num in enumerate(nums + [-inf]):
            while stack and nums[stack[-1]] > num:
                ans -= nums[(j:=stack.pop())] * (i - j) * (j - (stack[-1] if stack else -1))
            stack.append(i)
        return ans
```
```Java []
class Solution {
    public long subArrayRanges(int[] nums) {
        Deque<Integer> stack = new ArrayDeque<>();
        long max = 0;
        int n = nums.length;
        for(int i = 0; i <= n; i++) {
            while(!stack.isEmpty() && (i == n || nums[stack.peekLast()] < nums[i])) {
                int j = stack.pollLast();
                max += (long)nums[j] * (i - j) * (j - (stack.isEmpty() ? -1 : stack.peekLast()));
            }
            stack.offerLast(i);
        }
        stack = new ArrayDeque<>();
        long min = 0;
        for(int i = 0; i <= n; i++) {
            while(!stack.isEmpty() && (i == n || nums[stack.peekLast()] > nums[i])) {
                int j = stack.pollLast();
                min += (long)nums[j] * (i - j) * (j - (stack.isEmpty() ? -1 : stack.peekLast()));
            }
            stack.offerLast(i);
        }
        return max - min;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var subArrayRanges = function(nums) {
    const n = nums.length
    let stack = new Array(), ans = 0n
    for(let i = 0; i <= n; i++) {
        while(stack.length > 0 && (i == n || nums[stack[stack.length - 1]] < nums[i])) {
            const j = BigInt(stack.pop())
            ans += BigInt(nums[j]) * (BigInt(i) - j) * (j - (stack.length > 0 ? BigInt(stack[stack.length - 1]) : -1n))
        }
        stack.push(i)
    }
    stack = new Array()
    for(let i = 0; i <= n; i++) {
        while(stack.length > 0 && (i == n || nums[stack[stack.length - 1]] > nums[i])) {
            const j = BigInt(stack.pop())
            ans -= BigInt(nums[j]) * (BigInt(i) - j) * (j - (stack.length > 0 ? BigInt(stack[stack.length - 1]) : -1n))
        }
        stack.push(i)
    }
    return ans
};
```
```Go []
func subArrayRanges(nums []int) int64 {
    n, max, stack := len(nums), int64(0), []int{}
    for i := 0; i <= n; i++ {
        for l := len(stack); l > 0 && (i == n || nums[stack[l - 1]] < nums[i]); {
            j := stack[l - 1]
            stack = stack[:l - 1]
            if l = len(stack); l > 0 {
                max += int64(nums[j]) * int64(i - j) * int64(j - stack[l - 1])
            } else {
                max += int64(nums[j]) * int64(i - j) * int64(j + 1)
            }
        }
        stack = append(stack, i)
    }
    stack = []int{}
    min := int64(0)
    for i := 0; i <= n; i++ {
        for l := len(stack); l > 0 && (i == n || nums[stack[l - 1]] > nums[i]); {
            j := stack[l - 1]
            stack = stack[:l - 1]
            if l = len(stack); l > 0 {
                min += int64(nums[j]) * int64(i - j) * int64(j - stack[l - 1])
            } else {
                min += int64(nums[j]) * int64(i - j) * int64(j + 1)
            }
        }
        stack = append(stack, i)
    }
    return max - min
}
```