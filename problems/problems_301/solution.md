# [Python/Java/JavaScript] 记忆化DFS

> slug: python-ji-yi-hua-dfs-by-himymben-5b18
> date: 2021-10-27
> tags: Java, JavaScript, Python, Python3
> question: Remove Invalid Parentheses (remove-invalid-parentheses)
> url: https://leetcode.cn/problems/remove-invalid-parentheses/solutions/pmkl93/python-ji-yi-hua-dfs-by-himymben-5b18/

---
### 解题思路
记忆化剪枝 分别删两个连续左括号本质上是一样的,同时还能起到去重的作用

### 代码

```Python3 []
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l:
                    l -= 1
                else:
                    r += 1
        ans = []

        @lru_cache(None)
        def dfs(idx, cl, cr, dl, dr, path):
            if idx == len(s):
                if not dl and not dr:
                    ans.append(path)
                return
            if cr > cl or dl < 0 or dr < 0:
                return
            c = s[idx]
            if c == '(':
                dfs(idx+1,cl,cr,dl-1,dr, path)
            elif c == ')':
                dfs(idx+1,cl,cr,dl,dr-1, path)
            dfs(idx+1,cl+(c=='('),cr+(c==')'),dl,dr, path+c)
        
        dfs(0, 0, 0, l, r, "")
        return ans
```
```Java []
class Solution {
    private String s;
    private int n;
    private Set<String> cache;
    private List<String> ans;
    private StringBuilder sb;
    public List<String> removeInvalidParentheses(String s_) {
        s = s_;
        int l = 0, r = 0;
        n = s.length();
        cache = new HashSet<>();
        ans = new ArrayList<>();
        sb = new StringBuilder();
        for(int i=0;i<n;i++){
            if(s.charAt(i) == '(')
                l++;
            else if(s.charAt(i) == ')')
                if(l > 0)
                    l--;
                else
                    r++;
        }
        dfs(0, 0, 0, l, r);
        return ans;
    }

    private void dfs(int idx, int cl, int cr, int dl, int dr){
        if(cr > cl || dl < 0 || dr < 0)
            return;
        String key = sb.toString() + "#" + idx;
        if(cache.contains(key))
            return;
        cache.add(key);
        if(idx == n){
            if(dl == 0 && dr == 0)
                ans.add(sb.toString());
            return;
        }
        char c = s.charAt(idx);
        if(c == '(')
            dfs(idx + 1, cl, cr, dl-1,dr);
        else if(c == ')')
            dfs(idx + 1, cl, cr, dl, dr-1);
        sb.append(c);
        dfs(idx+1, c=='('?cl+1:cl, c==')'?cr+1:cr,dl,dr);
        sb.delete(sb.length()-1,sb.length());
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @return {string[]}
 */
var removeInvalidParentheses = function(s) {
    // 偷懒儿了，今天不优化了
    const ans = new Set(), path = [];
    const n = s.length;
    let l = 0, r = 0;
    for(let i=0;i<n;i++){
        if(s.charAt(i) == '(')
            l++;
        else if(s.charAt(i) == ')')
            if(l > 0)
                l--;
            else
                r++;
    }
    const res = n - l - r;

    const dfs = (idx, l) => {
        if(l < 0 || n - idx + path.length < res)
            return;
        if(idx == n){
            if(l==0 && path.length == res)
                ans.add(path.join(""))
            return;
        }
        
        path.push(s.charAt(idx));
        dfs(idx+1, l + (s.charAt(idx) == '(') - (s.charAt(idx) == ')'));
        path.pop();
        dfs(idx+1, l);
    }
    dfs(0, 0)
    return [...ans];
};
```