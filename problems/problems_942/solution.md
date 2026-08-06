# [Python/Java/JavaScript/Go] 贪心

> slug: -by-himymben-8jkw
> date: 2022-05-08
> tags: Go, Java, JavaScript, Python, Python3
> question: DI String Match (di-string-match)
> url: https://leetcode.cn/problems/di-string-match/solutions/R6N4sX/-by-himymben-8jkw/

---
### 解题思路
由于题目仅在乎相邻位置的大小关系, 
那么大于时我们取当时可取里的最大、小于时我们当时可取里的最小,
这样后一个位置选任何可取内的数字都满足条件,
且剩下的数字正好是少一个数字的递归问题。
(设当前最小和最大分别为a,b, 假如取的是最小的数字a, 那么新的范围是[a + 1, b], 
相当于解决[0, b - a - 1]的排列问题, 只是映射偏移了a+1而已)

### 代码

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