# [Python/Java/JavaScript] 递归

> slug: pythonjavajavascript-di-gui-by-himymben-pxpp
> date: 2021-10-14
> tags: Java, JavaScript, Python, Python3
> question: Count and Say (count-and-say)
> url: https://leetcode.cn/problems/count-and-say/solutions/DDJZyh/pythonjavajavascript-di-gui-by-himymben-pxpp/

---
### 解题思路
把这个看成两个题，如何将形如"1211"转换成"111221"。
然后就是递归了。

### 代码

```Python3 []
class Solution:
    @lru_cache(None)
    def countAndSay(self, n: int) -> str:
        def count(s):
            ans, cnt = [], 0
            for i,c in enumerate(s + "#"):
                if not i or s[i-1] == c:
                    cnt += 1
                if i and c != s[i-1]:
                    ans.append(str(cnt))
                    ans.append(s[i-1])
                    cnt = 1
            return "".join(ans)
        return "1" if n == 1 else count(self.countAndSay(n-1))
```
```Java []
class Solution {
    private static final Map<Integer,String> cache = new HashMap<>(){{put(1, "1");}};
    public String countAndSay(int n) {
        if(cache.containsKey(n))
            return cache.get(n);
        String res = count(countAndSay(n-1));
        cache.put(n, res);
        return res;
    }

    private String count(String s) {
        s += "#";
        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if(i == 0 || s.charAt(i-1) == c)
                cnt++;
            if(i > 0 && s.charAt(i-1) != c){
                sb.append(cnt+"");
                sb.append(s.charAt(i-1));
                cnt = 1;
            }
        }
        return sb.toString();
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {string}
 */
const cache = new Map();
var countAndSay = function(n) {
    if(n == 1)
        return "1";
    if(cache.has(n))
        return cache.get(n);
    const res = count(countAndSay(n-1));
    cache.set(n, res);
    return res;
};
var count = function(s) {
    s += "#";
    const ans = [];
    let cnt = 0, last;
    for(let i=0;i<s.length;i++){
        let c = s.charAt(i);
        if(last == c || last === undefined)
            cnt++;
        else if(last != undefined){
            ans.push(cnt + "");
            ans.push(last);
            cnt = 1;
        }
        last = c;
    }
    return ans.join("");
}
```