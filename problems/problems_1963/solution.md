# [Python/Java] Greedy

> Author: Benhao
> Date: 2021-08-08
> Upvotes: 3
> Tags: Java, Python, Python3

---

### Approach
At each position, the prefix is balanced as long as opening brackets are at least as numerous as closing brackets. Otherwise, a swap is required.

### Code

```Python3 []
class Solution:
    def minSwaps(self, s: str) -> int:
        ans = count = 0
        for c in s:
            if c == '[':
                count += 1
            else:
                if not count:
                    # Swap this ']' with the rightmost '['; later count increases by 1, but equal total counts keep later closing brackets valid
                    ans += 1
                    count += 1
                else:
                    count -= 1
        return ans
```
```Java []
class Solution {
    char[] chars;
    public int minSwaps(String s) {
        chars = s.toCharArray();
        int ans = 0, count = 0;
        for(char c:chars){
            if(c == '[')
                count++;
            else{
                if(count==0){
                    ans++;
                    count++;
                }
                else
                    count--;
            }
        }
        return ans;
    }
}
```
