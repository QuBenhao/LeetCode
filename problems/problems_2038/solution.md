# [Python/Java/JavaScript/Go] Simple counting

> slug: pythonjavajavascriptgo-by-himymben-isb6
> date: 2022-03-21
> tags: Go, Java, JavaScript, Python, Python3
> question: Remove Colored Pieces if Both Neighbors are the Same Color (remove-colored-pieces-if-both-neighbors-are-the-same-color)
> url: https://leetcode.cn/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/solutions/TbsVoG/pythonjavajavascriptgo-by-himymben-isb6/

---
### Approach
Alice can only remove the middle A from three consecutive As, and Bob can only remove the middle B from three consecutive Bs, so neither player's moves can affect the other's.
This is therefore just a comparison of how many characters each player can remove from the input.

> Removing a character together with its two neighbors would turn this into a game-theory problem. For example:
> Bob wins with BAAABB.
> Alice wins with BAAABBAAA.
> Bob wins with BBAAABBAAABB.

### Code

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
