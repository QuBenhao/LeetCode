# [Python/Java] 双指针

> Author: Benhao
> Date: 2021-08-18
> Upvotes: 8
> Tags: Java, Python, Python3

---

### 解题思路
从左到右找元音字母，从右到左找元音字母，这样对应的交换即可。
因为最终第一个元音字母总是和最后一个交换的，第二个和倒数第二个，依次类推。

### 代码

```Python3 []
class Solution:
    vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
    def reverseVowels(self, s: str) -> str:
        lt = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if lt[l] in self.vowels and lt[r] in self.vowels:
                lt[l], lt[r] = lt[r], lt[l]
                l += 1
                r -= 1
            elif lt[l] in self.vowels:
                r -= 1
            else:
                l += 1
        return ''.join(lt)
```
```Java []
class Solution {
    Set<Character> vowels = new HashSet<>(){{
        add('a');
        add('e'); 
        add('i'); 
        add('o'); 
        add('u'); 
        add('A'); 
        add('E'); 
        add('I'); 
        add('O'); 
        add('U');
    }}; 
    public String reverseVowels(String s) {
        char[] chars = s.toCharArray();
        int l = 0, r = s.length() - 1;
        while(l < r){
            if(vowels.contains(chars[l]) && vowels.contains(chars[r])){
                char tmp = chars[l];
                chars[l++] = chars[r];
                chars[r--] = tmp;
            } else if(vowels.contains(chars[l]))
                r--;
            else
                l++;
        }
        return new String(chars);
    }
}
```