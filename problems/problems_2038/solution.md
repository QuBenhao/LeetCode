# [Python/Java/JavaScript/Go] 简单计数

> slug: pythonjavajavascriptgo-by-himymben-isb6
> date: 2022-03-21
> tags: Go, Java, JavaScript, Python, Python3
> question: Remove Colored Pieces if Both Neighbors are the Same Color (remove-colored-pieces-if-both-neighbors-are-the-same-color)
> url: https://leetcode.cn/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/solutions/TbsVoG/pythonjavajavascriptgo-by-himymben-isb6/

---
### 解题思路
由于Alice只能删除连续三个A中间的A，Bob只能删除连续三个B中间的B，所以他们之间互相是无法做到影响对方的操作的。
这其实并不是一个博弈，只是根据输入判断谁能删除的字符更多而已。

> 如果删掉字符并删掉周围两个字符，才会变成博弈的题，比如：
> BAAABB 是Bob胜
> BAAABBAAA 是Alice胜
> BBAAABBAAABB 是Bob胜

### 代码

```Python3 []
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        i, j, s, n = 0, 0, 0, len(colors)
        while i < n:
            while j < n and colors[j] == colors[i]:
                j += 1
            if j - i >= 3:
                s += j - i - 2 if colors[i] == 'A' else i + 2 - j
            i = j
        return s > 0
```
```Java []
class Solution {
    public boolean winnerOfGame(String colors) {
        int s = 0, n = colors.length();
        for(int i = 0, j = 0; i < n; i = j) {
            while(j < n && colors.charAt(j) == colors.charAt(i))
                j++;
            if(j - i >= 3)
                s += colors.charAt(i) == 'A' ? j - i - 2 : i + 2 - j;
        }
        return s > 0;
    }
}
```
```JavaScript []
/**
 * @param {string} colors
 * @return {boolean}
 */
var winnerOfGame = function(colors) {
    const n = colors.length
    let s = 0
    for(let i = 0, j = 0; i < n; i = j) {
        while(j < n && colors.charCodeAt(i) === colors.charCodeAt(j))
            j++
        if(j - i >= 3)
            s += colors.charCodeAt(i) == 'A'.charCodeAt(0) ? j - i - 2 : i + 2 - j
    }
    return s > 0
};
```
```Go []
func winnerOfGame(colors string) bool {
    s, n := 0, len(colors)
    for i, j := 0, 0; i < n; i = j {
        for j < n && colors[i] == colors[j] {
            j++
        }
        if v := j - i - 2; v > 0 {
            if colors[i] == 'A' {
                s += v
            } else {
                s -= v
            }
        }
    }
    return s > 0
}
```