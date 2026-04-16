# [Python/Java] 三指针

> Author: Benhao
> Date: 2021-08-20
> Upvotes: 77
> Tags: Java, Python, Python3

---

### 解题思路
一个指针标记当前字符，另一个指针找这个字符有连续多少个，最后一个指针标记当前在数组中的读写位置。

### 代码

```Python3 []
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        write = 0
        while i < n:
            j = i
            while j < n and chars[j] == chars[i]:
                j += 1
            chars[write] = chars[i]
            write += 1
            if j - i > 1:
                for c in str(j-i):
                    chars[write] = c
                    write += 1
            i = j
        return write
```
```Java []
class Solution {
    public int compress(char[] chars) {
        int n = chars.length, write = 0;
        for(int i=0;i<n;){
            int j = i;
            while(j < n && chars[i] == chars[j])
                j++;
            chars[write++] = chars[i];
            if(j - i > 1){
                String tmp = Integer.toString(j-i);
                for(int k=0;k<tmp.length();k++)
                    chars[write++] = tmp.charAt(k);
            }
            i = j;
        }
        return write;
    }
}
```

### 复杂度
时间复杂度: $o(n)$
空间复杂度: $o(1)$