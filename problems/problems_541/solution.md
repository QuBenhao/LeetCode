# [Python/Java] 模拟

> Author: Benhao
> Date: 2021-08-19
> Upvotes: 5
> Tags: Java, Python, Python3

---

```Python3 []
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lt = list(s)
        for i in range(0, len(s), 2 * k):
            lt[i:i+k] = lt[i:i+k][::-1]
        return ''.join(lt)
```
```Java []
class Solution {
    public String reverseStr(String s, int k) {
        char[] chars = s.toCharArray();
        int n = s.length();
        for(int i=0;i<n;i+=2*k){
            int l = i, r = Math.min(i+k-1, n-1);
            while(l < r){
                char tmp = chars[l];
                chars[l] = chars[r];
                chars[r] = tmp;
                l++;
                r--;
            }
        }
        return new String(chars);
    }
}
```
<br>
```Python3 []
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return ''.join([s[i:i+k][::-1] if i % (2 * k) == 0 else s[i:i+k] for i in range(0, len(s), k)])
```
```Java []
class Solution {
    public String reverseStr(String s, int k) {
        StringBuilder sb = new StringBuilder();
        char[] chars = s.toCharArray();
        int n = s.length();
        for(int i=0;i<n;i+=k){
            if(i % (2 * k) == 0)
                for(int j=Math.min(n-1, i + k - 1);j>=i;j--)
                    sb.append(chars[j]);
            else
                sb.append(s.substring(i, Math.min(n, i + k)));
        }
        return sb.toString();
    }
}
```