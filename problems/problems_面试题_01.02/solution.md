# [Python/Java/TypeScript/Go] Simulation

> slug: pythonjavatypescriptgo-mo-ni-by-himymben-fwa9
> date: 2022-09-26
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Check Permutation LCCI (check-permutation-lcci)
> url: https://leetcode.cn/problems/check-permutation-lcci/solutions/EKRyDc/pythonjavatypescriptgo-mo-ni-by-himymben-fwa9/

---
### Approach
Check whether the sorted strings or character counts match.

### Code

```Python3 []
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)
```
```Java []
class Solution {
    public boolean CheckPermutation(String s1, String s2) {
        // I assumed lowercase letters without being certain; otherwise, adjust the array size and the offset subtracted below
        int[] cnts = new int[26];
        for (int i = 0; i < s1.length(); i++) {
            cnts[s1.charAt(i) - 'a']++;
        }
        for (int i = 0; i < s2.length(); i++) {
            cnts[s2.charAt(i) - 'a']--;
        }
        for (int i = 0; i < cnts.length; i++) {
            if (cnts[i] != 0) {
                return false;
            }
        }
        return true;
    }
}
```
```TypeScript []
function CheckPermutation(s1: string, s2: string): boolean {
    const cnts: Array<number> = new Array<number>(26).fill(0)
    for (let i = 0; i < s1.length; i++) {
        cnts[s1.charCodeAt(i) - 'a'.charCodeAt(0)]++;
    }
    for (let i = 0; i < s2.length; i++) {
        cnts[s2.charCodeAt(i) - 'a'.charCodeAt(0)]--;
    }
    for (const v of cnts) {
        if (v != 0) {
            return false
        }
    }
    return true
};
```
```Go []
func CheckPermutation(s1 string, s2 string) bool {
    cnts := make([]int, 26)
    for i := 0; i < len(s1); i++ {
        cnts[s1[i] - 'a']++
    }
    for i := 0; i < len(s2); i++ {
        cnts[s2[i] - 'a']--
    }
    for _, v := range cnts {
        if v != 0 {
            return false
        }
    }
    return true
}
```
