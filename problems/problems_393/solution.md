# [Python/Java/JavaScript/Go] Simulation

> slug: pythonjavajavascriptgo-by-himymben-yuea
> date: 2022-03-13
> tags: Go, Java, JavaScript, Python, Python3
> question: UTF-8 Validation (utf-8-validation)
> url: https://leetcode.cn/problems/utf-8-validation/solutions/u4W8Un/pythonjavajavascriptgo-by-himymben-yuea/

---
### Approach
I finally understood the problem.
Treat every input integer as an 8-bit binary number.
Simulate from left to right.
If the current number starts with 0, it forms a one-byte character by itself.
If it starts with 110, it must be followed by one number starting with 10 to form a two-byte character.
...
If the leading number starts with $x$ ones, it must be grouped with the next $x-1$ numbers, each starting with 10.
The first number in each group determines how many numbers that group contains.


### Code

```Python3 []
ONE = 1 << 7
TWO = ONE + (1 << 6)

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        while i < len(data):
            l = 1
            while l < 7 and data[i] >> (8 - l) & 1:
                l += 1
            if l == 2 or l > 5:
                return False
            if l > 2:
                l -= 1
            if i + l - 1 >= len(data):
                return False
            for j in range(i + 1, i + l):
                if (data[j] & TWO) != ONE:
                    return False
            i += l
        return True
```
```Java []
class Solution {
    private static final int ONE = 1 << 7, TWO = ONE + (1 << 6);
    public boolean validUtf8(int[] data) {
        for(int i = 0; i < data.length;) {
            int l = 1;
            for(; l < 7 && ((data[i] >> (8 - l)) & 1) == 1; l++) {}
            if(l == 2 || l > 5 || i + l - 2 >= data.length)
                return false;
            if(l > 2) l--;
            for(int j = i + 1; j < i + l; j++)
                if((data[j] & TWO) != ONE)
                    return false;
            i += l;
        }
        return true;
    }
}
```
```JavaScript []
/**
 * @param {number[]} data
 * @return {boolean}
 */
const ONE = 1 << 7, TWO = ONE + (1 << 6)
var validUtf8 = function(data) {
    for(let i = 0; i < data.length; ) {
        let l = 1
        for(;l < 7 && (data[i] >> (8 - l)) & 1 == 1; l++) {}
        if(l == 2 || l > 5 || i + l - 2 >= data.length)
            return false
        if(l > 2)
            l--
        for(let j = i + 1; j < i + l; j++)
            if((data[j] & TWO) != ONE)
                return false
        i += l
    }
    return true
};
```
```Go []
const one int = 1 << 7
const two int = one + (1 << 6)
func validUtf8(data []int) bool {
    for i := 0; i < len(data); {
        l := 1
        for l < 7 && (data[i] >> (8 - l)) & 1 == 1 {
            l++            
        }
        if l == 2 || l > 5 || i + l - 2 >= len(data) {
            return false
        }
        if l > 2 {
            l--
        }
        for j := i + 1; j < i + l; j++ {
            if data[j] & two != one {
                return false
            }
        }
        i += l
    }
    return true
}
```
