# [Python/Java/JavaScript] dfs回溯

> Author: Benhao
> Date: 2021-10-16
> Upvotes: 22
> Tags: Java, JavaScript, Python, Python3

---

### 解题思路
抱歉家人们，今天在公司加班儿，调代码状态不太好。一开始以为每个数字间都要加加减乘除，写了半天...

`+ - * ""`
每个字符与字符实际上有四种连接方式，加减乘和拼接(就是*10再加当前数，特殊情况是不能以0作为开头拼接)。
我们在每个位置遍历尝试不同的连接方式，并记录 上一次运算等待被加入结果、当前数字、当前累计的值和当前路径，
在全部连接结束后，统计累计值和目标值是否相同，如果相同就将路径计入答案。
始终进行回溯去尝试其他方案，在同一个路径数组中拼接，不需要复制额外空间。

### 代码

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