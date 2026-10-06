# [Python/Java/JavaScript/Go] Greedy

> slug: -by-himymben-8jkw
> date: 2022-05-08
> tags: Go, Java, JavaScript, Python, Python3
> question: DI String Match (di-string-match)
> url: https://leetcode.cn/problems/di-string-match/solutions/R6N4sX/-by-himymben-8jkw/

---
### Approach
The problem only cares about the ordering of adjacent positions. 
When the current value must be greater, take the largest available number; when it must be smaller, take the smallest.
Then any remaining number satisfies the condition at the next position.
The remaining numbers form the same recursive problem with one fewer number.
(Let the current minimum and maximum be a,b. If we take the minimum a, the new range is [a + 1, b], 
equivalent to solving the permutation problem on [0, b - a - 1], merely shifted by a+1)

### Code

```Python3 []
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        left, right, ans = 0, len(s), []
        for c in s:
            if c == 'I':
                ans.append(left)
                left += 1
            else:
                ans.append(right)
                right -= 1
        ans.append(left)
        return ans
```
```Java []
class Solution {
    public int[] diStringMatch(String s) {
        int n = s.length();
        int left = 0, right = n;
        int[] ans = new int[n + 1];
        for(int i = 0, idx = 0; i < n; i++) {
            if(s.charAt(i) == 'I') {
                ans[idx++] = left++;
            } else {
                ans[idx++] = right--;
            }
        }
        ans[n] = left;
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @return {number[]}
 */
var diStringMatch = function(s) {
    const n = s.length, ans = new Array()
    let left = 0, right = n
    for(let i = 0; i < n; i++) {
        if(s.charCodeAt(i) === 'I'.charCodeAt(0)) {
            ans.push(left++)
        } else {
            ans.push(right--)
        }
    }
    ans.push(left)
    return ans
};
```
```Go []
func diStringMatch(s string) (ans []int) {
    left, right := 0, len(s)
    for _, r := range s {
        if r == 'I' {
            ans = append(ans, left)
            left++
        } else {
            ans = append(ans, right)
            right--
        }
    }
    ans = append(ans, left)
    return
}
```
