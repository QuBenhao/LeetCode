# [Python/Java/JavaScript] 从低位开始累加

> slug: pythonjavajavascript-cong-di-wei-kai-shi-uoi4
> date: 2021-10-18
> tags: Java, JavaScript, Python, Python3
> question: Number Complement (number-complement)
> url: https://leetcode.cn/problems/number-complement/solutions/dlA2aE/pythonjavajavascript-cong-di-wei-kai-shi-uoi4/

---
```Python3 []
class Solution:
    def findComplement(self, num: int) -> int:
        i = ans = 0
        while num:
            if not num & 1:
                ans += 1 << i
            num >>= 1
            i += 1
        return ans
```
```Java []
class Solution {
    public int findComplement(int num) {
        int ans = 0;
        for(int i=0;num>0;i++){
            if((num&1)==0)
                ans+=1<<i;
            num>>=1;
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number} num
 * @return {number}
 */
var findComplement = function(num) {
    let ans = 0;
    for(let i=0;num>0;i++){
        if((num&1)==0)
            ans+=1<<i;
        num>>=1;
    }
    return ans;
};
```