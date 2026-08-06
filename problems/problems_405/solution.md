# [Python/Java/JavaScript] 进制转换

> slug: pythonjava-2jin-zhi-zhuan-huan-wei-16jin-dwen
> date: 2021-10-02
> tags: Java, JavaScript, Python, Python3
> question: Convert a Number to Hexadecimal (convert-a-number-to-hexadecimal)
> url: https://leetcode.cn/problems/convert-a-number-to-hexadecimal/solutions/xjF15C/pythonjava-2jin-zhi-zhuan-huan-wei-16jin-dwen/

---
### 解题思路
用常见的进制转换方法即可(辗转相除)

### 代码

```Python3 []
CONV = "0123456789abcdef"
class Solution:
    def toHex(self, num: int) -> str:
        ans = []
        # 32位2进制数，转换成16进制 -> 4个一组，一共八组
        for _ in range(8):
            ans.append(num%16)
            num //= 16
            if not num:
                break
        return "".join(CONV[n] for n in ans[::-1])
```
```Java []
class Solution {
    private final char[] CONV = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f' };

    public String toHex(int num) {
        StringBuilder sb = new StringBuilder();
        while (sb.length() < 8) {
            sb.append(CONV[num & 0xf]);
            num >>= 4;
            if(num == 0)
                break;
        }
        return sb.reverse().toString();
    }
}
```
```javascript []
/**
 * @param {number} num
 * @return {string}
 */
const CONV = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'];
var toHex = function(num) {
    let ans = [];
    if(num < 0)
        num += 2**32;
    for(let i=0;i<8;i++){
        ans.push(CONV[num % 16]);
        num = Math.floor(num/16);
        if(num == 0)
            break;
    }
    ans.reverse();
    return ans.join("");
};
```