# [Python/Java/JavaScript/Go] Greedy

> slug: pythonjavajavascriptgo-tan-xin-by-himymb-0nn5
> date: 2022-02-27
> tags: Go, Java, JavaScript, Python, Python3
> question: Optimal Division (optimal-division)
> url: https://leetcode.cn/problems/optimal-division/solutions/Wx5acx/pythonjavajavascriptgo-tan-xin-by-himymb-0nn5/

---
### Approach
However the parentheses are added, the first number remains the only numerator, and the second number is always part of the denominator.
The numerator cannot increase, so maximize the result by making the denominator as small as possible.
Since all numbers are positive integers, divide the second number by as many subsequent numbers as possible.

### Code

```Python3 []
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        return "/".join(map(str, nums)) if len(nums) <= 2 else "{}/({})".format(nums[0], "/".join(map(str, nums[1:])))
```
```Java []
class Solution {
    public String optimalDivision(int[] nums) {
        int n = nums.length;
        StringBuilder sb = new StringBuilder();
        sb.append(nums[0]);
        if(n > 1) {
            sb.append("/");
            if(n > 2)
                sb.append("(");
            sb.append(nums[1]);
            for(int i = 2; i < n; i++) {
                sb.append("/");
                sb.append(nums[i]);
            }
            if(n > 2)
                sb.append(")");
        }
        return sb.toString();
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {string}
 */
var optimalDivision = function(nums) {
    const ans = [], n = nums.length
    ans.push(nums[0])
    if(n > 1) {
        ans.push("/")
        if(n > 2)
            ans.push("(")
        ans.push(nums[1])
        for(let i = 2; i < n; i++) {
            ans.push("/")
            ans.push(nums[i])
        }
        if(n > 2)
            ans.push(")")
    }
    return ans.join("")
};
```
```Go []
func optimalDivision(nums []int) string {
    n, ans := len(nums), &strings.Builder{}
    ans.WriteString(strconv.Itoa(nums[0]))
    if n > 1 {
        ans.WriteByte('/')
        if n > 2 {
            ans.WriteByte('(')
        }
        ans.WriteString(strconv.Itoa(nums[1]))
        for i := 2; i < n; i++ {
            ans.WriteByte('/')
            ans.WriteString(strconv.Itoa(nums[i]))
        }
        if n > 2 {
            ans.WriteByte(')')
        }
    }
    return ans.String()
}
```
