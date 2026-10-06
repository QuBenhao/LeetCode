# [Python/Java/JavaScript] DFS backtracking

> Author: Benhao
> Date: 2021-10-16
> Upvotes: 22
> Tags: Java, JavaScript, Python, Python3

---

### Approach
Sorry, everyone; I worked overtime today and was not in a good state for debugging. At first I thought every pair of digits needed an addition, subtraction, multiplication, or division sign, and spent ages on that...

`+ - * ""`
There are actually four ways to connect adjacent characters: addition, subtraction, multiplication, and concatenation (multiply by 10 and add the current digit, except that a concatenated number cannot start with 0).
At each position, try each connection and record the previous operation awaiting inclusion in the result, the current number, the accumulated value, and the current path.
After connecting all characters, compare the accumulated value with the target and add the path to the answer if they match.
Backtrack to try other possibilities, reusing the same path array without allocating extra copies.

### Code

```Python3 []
ops = ["*", "+", "", "-"]
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(idx, sign, curv, val, path):
            c = num[idx]
            curv = 10 * curv + int(c)
            if idx == n - 1:
                if sign * curv + val == target:
                    path.append(num[idx])
                    ans.append("".join(path))
                    path.pop()
                return
            for i in (-1, 0, 1, 2):
                path.append(num[idx] + ops[i])
                if not i:
                    dfs(idx+1, sign * curv, 0, val, path)
                elif i < 2:
                    dfs(idx+1, i, 0, val + sign * curv, path)
                elif curv or c != '0':
                    dfs(idx+1, sign, curv, val, path)
                path.pop()

        ans = []
        n = len(num)
        dfs(0, 1, 0, 0, [])
        return ans
```
```Java []
class Solution {
    private static final Map<Integer, String> ops = new HashMap<>(){{
        put(0, "*");
        put(-1, "-");
        put(1, "+");
        put(2, "");
    }};
    String num;
    List<String> ans;
    int target;
    public List<String> addOperators(String num_, int target_) {
        num = num_;
        target = target_;
        ans = new ArrayList<>();
        dfs(0, 1L, 0L, 0L, new StringBuilder());
        return ans;
    }

    private void dfs(int idx, long sign, long curv, long val, StringBuilder sb) {
        char c = num.charAt(idx);
        curv = 10 * curv + c - '0';
        if(idx == num.length() - 1){
            if(target - val == sign * curv){
                sb.append(c);
                ans.add(sb.toString());
                sb.deleteCharAt(sb.length()-1);
            }
            return;
        }
        for(Integer k: ops.keySet()){
            String v = ops.get(k);
            sb.append(c);
            sb.append(v);
            if(k == 0)
                dfs(idx+1, sign * curv, 0, val, sb);
            else if(k < 2)
                dfs(idx+1, k, 0, val + sign * curv, sb);
            else if(curv > 0 || c != '0')
                dfs(idx+1, sign, curv, val, sb);
            sb.delete(v!=""?sb.length()-2:sb.length()-1,sb.length());
        };
    }
}
```
```JavaScript []
/**
 * @param {string} num
 * @param {number} target
 * @return {string[]}
 */
const ops = ["-", "*", "+", ""];
var addOperators = function(num, target) {    
    const ans = [], path = [];

    const dfs = (idx, sign, curv, val) => {
        let c = num.charAt(idx);
        curv = 10 * curv + (c - '0');
        if(idx == num.length - 1){
            if(target - val == sign * curv){
                path.push(c);
                ans.push(path.join(""));
                path.pop();
            }
        }
        else{
            for(let i=0;i<ops.length;i++){
                path.push(c + ops[i]);
                if(i == 1)
                    dfs(idx+1,sign * curv, 0, val);
                else if(i < 3)
                    dfs(idx+1,i-1, 0, val + sign * curv);
                else if(curv > 0 || c != '0')
                    dfs(idx+1,sign,curv,val);
                path.pop();
            }
        }
    }

    dfs(0, 1, 0, 0);
    return ans;
};


```
