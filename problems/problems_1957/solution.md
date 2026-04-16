# [Python/Java] 模拟

> Author: Benhao
> Date: 2021-08-08
> Upvotes: 3
> Tags: Java, Python, Python3

---

### 解题思路
统计连续的相同字符个数，超过2不加入最终字符串

### 代码

```Python3 []
class Solution:
    def makeFancyString(self, s: str) -> str:
        q = []
        count = 0
        for c in s:
            if q and c == q[-1]:
                count += 1
            else:
                count = 1
            if count < 3:
                q.append(c)
        return ''.join(q)
```
```Java []
class Solution {
    public String makeFancyString(String s) {
        char[] chars = s.toCharArray();
        StringBuilder q = new StringBuilder();
        int count = 0;
        for(char c:chars){
            if(q.length()>0 && q.charAt(q.length()-1) == c)
                count++;
            else
                count = 1;
            if(count < 3)
                q.append(c);
        }
        return q.toString();
    }
}
```