# [Python/Java] Greedily count L and R

> Author: Benhao
> Date: 2021-09-07
> Upvotes: 6
> Tags: Java, Python, Python3

---

### Approach
The input string is balanced, with equal counts of L and R. Removing a balanced substring leaves equal counts of L and R. Splitting off a substring whenever possible therefore gives the largest number of substrings.

### Code

```Python3 []
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = cur = 0
        for c in s:
            if c == 'L':
                cur += 1
            else:
                cur -= 1
            if not cur:
                ans += 1
        return ans
```
```Java []
class Solution {
    public int balancedStringSplit(String s) {
        int ans = 0;
        for(int i=0, cur=0;i<s.length();i++){
            if(s.charAt(i) == 'L')
                cur++;
            else
                cur--;
            if(cur == 0)
                ans++;
        }
        return ans;
    }
}
```
