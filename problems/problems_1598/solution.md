# [Python/Java/TypeScript/Go] 模拟

> slug: pythonjavatypescriptgo-mo-ni-by-himymben-dhlf
> date: 2022-09-08
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Crawler Log Folder (crawler-log-folder)
> url: https://leetcode.cn/problems/crawler-log-folder/solutions/ljij0P/pythonjavatypescriptgo-mo-ni-by-himymben-dhlf/

---
### 解题思路
维护一个数字简单模拟栈即可。如果需要知道文件夹顺序，可以实际维护一个栈。

### 代码

```Python3 []
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cur = 0
        for log in logs:
            match log:
                case "../":
                    cur = max(cur - 1, 0)
                case "./":
                    pass
                case _:
                    cur += 1
        return cur
```
```Java []
class Solution {
    public int minOperations(String[] logs) {
        int ans = 0;
        for (String log: logs) {
            if ("../".equals(log)) {
                ans = Math.max(ans - 1, 0);
            } else if (!"./".equals(log)) {
                ans++;
            }
        }
        return ans;
    }
}
```
```TypeScript []
function minOperations(logs: string[]): number {
    let ans: number = 0
    for (const log of logs) {
        if ("../" === log) {
            ans = Math.max(0, ans - 1)
        } else if ("./" !== log) {
            ans++
        }
    }
    return ans
};
```
```Go []
func minOperations(logs []string) (ans int) {
    for _, log := range logs {
        if "../" == log {
            if ans > 0 {
                ans--
            }
        } else if "./" != log {
            ans++
        }
    }
    return
}
```