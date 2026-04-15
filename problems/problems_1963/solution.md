# [Python/Java] 贪心

> Author: Benhao
> Date: 2021-08-08
> Upvotes: 3
> Tags: Java, Python, Python3

---

### 解题思路
每到一个位置，只要我们左括号的个数不少于右括号的个数，它就是平衡的。否则必须进行交换

### 代码

```Python3 []
class Solution:
    def minSwaps(self, s: str) -> int:
        ans = count = 0
        for c in s:
            if c == '[':
                count += 1
            else:
                if not count:
                    # 将最右的'['和这个']'互换，后面的count会多1，但是由于数量相等，不影响再往后的右括号
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