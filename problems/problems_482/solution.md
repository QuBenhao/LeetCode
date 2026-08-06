# [Python/Java/JavaScript] 模拟

> slug: pythonjavajavascript-mo-ni-by-himymben-rfow
> date: 2021-10-03
> tags: Java, JavaScript, Python, Python3
> question: License Key Formatting (license-key-formatting)
> url: https://leetcode.cn/problems/license-key-formatting/solutions/EXYKB2/pythonjavajavascript-mo-ni-by-himymben-rfow/

---
### 解题思路
我们可以将s的所有'-'去掉，然后从后往前k个k个取，最后再反向；
也可以根据去掉后的数量求出每组数的长度，然后正序构造。

### 代码

```Python3 []
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()[::-1]
        return "-".join(s[i:i + k] for i in range(0, len(s), k))[::-1]
```
```Java []
class Solution {
    public String licenseKeyFormatting(String s, int k) {
        StringBuilder sb = new StringBuilder();
        for(int i=s.length()-1,cnt=0;i>=0;i--){
            if(s.charAt(i) != '-'){
                sb.append(Character.toUpperCase(s.charAt(i)));
                cnt++;
                if(cnt%k==0)
                    sb.append('-');
            }
        }
        if(sb.length() > 0 && sb.charAt(sb.length() - 1) == '-')
            sb.delete(sb.length() - 1, sb.length());
        sb.reverse();
        return sb.toString();
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var licenseKeyFormatting = function(s, k) {
    const ans = [];
    let cnt = 0, c = "";
    for(let i=s.length-1;i>=0;i--){
        c = s.charAt(i);
        if(c != '-'){
            ans.push(c.toUpperCase());
            cnt++;
            if(cnt%k==0)
                ans.push('-');
        }
    }
    if(ans.length>0 && ans[ans.length-1]=='-')
        ans.pop();
    return ans.reverse().join("");
};
```