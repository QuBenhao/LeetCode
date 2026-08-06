# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-by-himymben-hlbt
> date: 2022-04-20
> tags: Go, Java, JavaScript, Python, Python3
> question: Longest Absolute File Path (longest-absolute-file-path)
> url: https://leetcode.cn/problems/longest-absolute-file-path/solutions/4mrUTi/pythonjavajavascriptgo-by-himymben-hlbt/

---
### 解题思路
按换行符分割输入，根据该行的前缀tab数量确认它属于哪个层级，用哈希记录之前遍历的长度，在遇到文件的'.'时统计答案即可。

### 代码

```Python3 []
# import more_itertools
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        record, ans = defaultdict(int), 0
        for line in input.split("\n"):
            # level, line = more_itertools.ilen(takewhile(lambda x: x == '\t', line)), line.replace("\t","")
            level, line = sum(1 for _ in takewhile(lambda x: x == '\t', line)), line.replace("\t","")
            record[level] = len(line)
            if '.' in line:
                ans = max(ans, sum(record[i] for i in range(level + 1)) + level)
        return ans
```
```Java []
class Solution {
    public int lengthLongestPath(String input) {
        Map<Integer, Integer> map = new HashMap<>();
        int ans = 0, n = input.length();
        for(int i = 0, cur = 0; i < n; i++) {
            int level = 0;
            while(i < n && input.charAt(i) == '\t') {
                level++;
                i++;
            }
            int len = 0;
            boolean isFile = false;
            while(i < n && input.charAt(i) != '\n') {
                len++;
                if(input.charAt(i++) == '.')
                    isFile = true;
            }
            map.put(level, len);
            if(isFile) {
                int sum = 0;
                for(int j = 0; j <= level; j++)
                    sum += map.getOrDefault(j, 0);
                ans = Math.max(ans, sum + level);
            }
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {string} input
 * @return {number}
 */
var lengthLongestPath = function(input) {
    const record = new Map(), n = input.length
    let ans = 0
    for(let i = 0; i < n; i++) {
        let level = 0, len = 0, isFile = false
        while(i < n && input.charCodeAt(i) == '\t'.charCodeAt(0)) {
            level++
            i++
        }
        while(i < n && input.charCodeAt(i) != '\n'.charCodeAt(0)) {
            if(input.charCodeAt(i++) == '.'.charCodeAt(0))
                isFile = true
            len++
        }
        record.set(level, len)
        if(isFile) {
            let sum = 0
            for(let j = 0; j <= level; j++)
                sum += record.get(j)
            ans = Math.max(ans, sum + level)
        }
    }
    return ans
};
```
```Go []
func lengthLongestPath(input string) (ans int) {
    record, n := map[int]int{}, len(input)
    for i := 0; i < n; i++ {
        level, cur, isFile := 0, 0, false
        for i < n && input[i] == '\t' {
            level++
            i++
        }
        for i < n && input[i] != '\n' {
            if input[i] == '.' {
                isFile = true
            }
            i++
            cur++
        }
        record[level] = cur
        if isFile {
            sum := 0
            for j := 0; j <= level; j++ {
                sum += record[j]
            }
            if v := sum + level; v > ans {
                ans = v
            }
        }
    }
    return
}
```