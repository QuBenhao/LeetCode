# [Python/Java] 模拟 时间o(n) 空间o(1)

> Author: Benhao
> Date: 2021-08-16
> Upvotes: 4
> Tags: Java, Python, Python3

---

```Python3 []
class Solution:
    def checkRecord(self, s: str) -> bool:
        return "LLL" not in s and s.count('A') < 2
```
```Java []
class Solution {
    public boolean checkRecord(String s) {
        char[] chars = s.toCharArray();
        int countA = 0, countL = 0;
        for(char c:chars){
            if(c == 'L'){
                countL++;
                if(countL == 3)
                    return false;
            }
            else{
                if(c == 'A'){
                    countA++;
                    if(countA == 2)
                        return false;
                }
                countL = 0;
            }
        }
        return true;
    }
}
```
