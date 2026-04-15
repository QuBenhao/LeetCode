# [Python/Java/JavaScript/Go] 暴力 or 二分

> Author: Benhao
> Date: 2022-04-02
> Upvotes: 12
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
按题意模拟即可

### 代码
模拟
```Python3 []
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return min(letters, key=lambda x:(ord(x) - ord(target) - 1)%26)
```
```Java []
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        for(char c: letters)
            if(c > target)
                return c;
        return letters[0];
    }
}
```
```JavaScript []
/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
var nextGreatestLetter = function(letters, target) {
    for(const c of letters)
        if(c > target)
            return c
    return letters[0]
};
```
```Go []
func nextGreatestLetter(letters []byte, target byte) byte {
    for _, b := range letters {
        if b > target {
            return b
        }
    }
    return letters[0]
}
```

二分
```Python3 []
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[r] if (r := bisect_right(letters, target)) < len(letters) else letters[0]
```
```Java []
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int r = letters.length;
        for(int l = 0; l < r; ) {
            int mid = (l + r) >> 1;
            if(letters[mid] <= target)
                l = mid + 1;
            else
                r = mid;
        }
        return r == letters.length ? letters[0] : letters[r];
    }
}
```
```JavaScript []
/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
var nextGreatestLetter = function(letters, target) {
    let r = letters.length
    for(let l = 0; l < r; ) {
        const mid = (l + r) >> 1
        if(letters[mid] <= target)
            l = mid + 1
        else
            r = mid
    }
    return r == letters.length ? letters[0] : letters[r]
};
```
```Go []
func nextGreatestLetter(letters []byte, target byte) byte {
    r := len(letters)
    for l := 0; l < r; {
        mid := (l + r) >> 1
        if letters[mid] <= target {
            l = mid + 1
        } else {
            r = mid
        }
    }
    if r == len(letters) {
        return letters[0]
    }
    return letters[r]
}
```