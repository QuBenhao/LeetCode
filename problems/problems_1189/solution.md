# [Python/Java/JavaScript/Go] 简单模拟

> slug: pythonjavajavascriptgo-jian-dan-mo-ni-by-dmuc
> date: 2022-02-13
> tags: Go, Java, JavaScript, Python, Python3
> question: Maximum Number of Balloons (maximum-number-of-balloons)
> url: https://leetcode.cn/problems/maximum-number-of-balloons/solutions/L880nV/pythonjavajavascriptgo-jian-dan-mo-ni-by-dmuc/

---
```Python3 []
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(cnts[c]//2 if c in "lo" else cnts[c] for c in "balon") if (cnts := Counter(text)) else 0
```
```Java []
class Solution {
    public int maxNumberOfBalloons(String text) {
        int b = 0, a = 0, l = 0, o = 0, n = 0;
        for(int i = 0; i < text.length(); i++) {
            switch(text.charAt(i)){
                case 'a':
                    a++;
                    break;
                case 'b':
                    b++;
                    break;
                case 'l':
                    l++;
                    break;
                case 'o':
                    o++;
                    break;
                case 'n':
                    n++;
                    break;
                default:
                    continue;
            }
        }
        return min(a, b, l/2, o/2, n);
    }

    private int min(int... vals){
        int ans = Integer.MAX_VALUE;
        for(int v: vals){
            ans = Math.min(ans, v);
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons = function(text) {
    let b = 0, a = 0, l = 0, o = 0, n = 0
    for(let i = 0; i < text.length; i++){
        switch(text.charAt(i)){
            case 'a':
                a++
                break
            case 'b':
                b++
                break
            case 'l':
                l++
                break
            case 'o':
                o++
                break
            case 'n':
                n++
                break
            default:
                continue
        }
    }
    return Math.min(a, b, Math.floor(l / 2), Math.floor(o / 2), n)
};
```
```Go []
func maxNumberOfBalloons(text string) int {
    b, a, l, o, n := 0, 0, 0, 0, 0
    for i := 0; i < len(text); i++ {
        if text[i] == 'a' {
            a++
        } else if text[i] == 'b' {
            b++
        } else if text[i] == 'l' {
            l++
        } else if text[i] == 'o' {
            o++
        } else if text[i] == 'n' {
            n++
        }
    }
    return min(b, a, l/2, o/2, n)
}

func min(vals ...int) int {
    ans := vals[0]
    for _, v := range vals {
        if v < ans {
            ans = v
        }
    }
    return ans
}
```