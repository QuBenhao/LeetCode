# [Python/Java/JavaScript/Go] Monotonic stack

> Author: Benhao
> Date: 2022-03-03
> Upvotes: 40
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
I referred to [灵老师](https://leetcode.cn/problems/sum-of-subarray-ranges/solution/cong-on2-dao-ondan-diao-zhan-ji-suan-mei-o1op/) and [草莓奶昔](https://leetcode.cn/problems/sum-of-subarray-ranges/solution/dan-diao-zhan-on-by-cao-mei-nai-xi-i-xw3d/); both explanations are clear and well written.

The required sum of each interval's maximum minus its minimum can be computed by counting how many intervals contain each number as their maximum and as their minimum.
For maxima, maintain an increasing monotonic stack. When the current value is larger than earlier values, it determines the right boundary for those smaller stack elements. Their left boundary as a maximum is the index of the preceding larger value when they were pushed.
Use the same idea for minima, with the comparisons reversed.

### Code

```Python3 []
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans, stack = 0, []
        for i, num in enumerate(nums + [inf]):
            while stack and nums[stack[-1]] < num:
                # The stack top's time as the maximum ends here; its interval boundaries are the preceding index and the current index that pops it
                # Choose a left endpoint on the left and a right endpoint on the right; this element is the maximum throughout each such interval
                # Therefore its occurrence count is C_l1 * C_r1
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
