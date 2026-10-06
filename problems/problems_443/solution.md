# [Python/Java] Three pointers

> Author: Benhao
> Date: 2021-08-20
> Upvotes: 77
> Tags: Java, Python, Python3

---

### Approach
One pointer marks the current character, another finds the length of its consecutive run, and the last tracks the current read/write position in the array.

### Code

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

### Complexity
Time complexity: $o(n)$
Space complexity: $o(1)$
