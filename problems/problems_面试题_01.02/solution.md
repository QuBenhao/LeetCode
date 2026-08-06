# [Python/Java/TypeScript/Go] 模拟

> slug: pythonjavatypescriptgo-mo-ni-by-himymben-fwa9
> date: 2022-09-26
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Check Permutation LCCI (check-permutation-lcci)
> url: https://leetcode.cn/problems/check-permutation-lcci/solutions/EKRyDc/pythonjavatypescriptgo-mo-ni-by-himymben-fwa9/

---
### 解题思路
判断排序或计数后是否一致即可

### 代码

```Python3 []
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)
```
```Java []
class Solution {
    public boolean CheckPermutation(String s1, String s2) {
        // 不确定是不是都是小写字母但还是这么写了，如果不是的话需要改一下大小和下面减的东西
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