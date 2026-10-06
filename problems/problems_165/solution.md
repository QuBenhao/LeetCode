# [Python/Java] Compare dot-separated components with two pointers

> Author: Benhao
> Date: 2021-08-31
> Upvotes: 25
> Tags: Java, Python, Python3

---

### Approach
At each step, read the number between two dots and compare the two values. Missing components always default to 0.
Thus, `1.0.0.0.0` and `1` are equivalent unless a later component is greater than 0. Keep comparing until a component differs; otherwise, the versions are equal.

### Code

```Python3 []
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        m, n = len(version1), len(version2)
        i = j = 0
        while i < m or j < n:
            a = b = 0
            while i < m and version1[i] != '.':
                a = 10 * a + int(version1[i])
                i += 1
            while j < n and version2[j] != '.':
                b = 10 * b + int(version2[j])
                j += 1
            if a > b:
                return 1
            elif a < b:
                return -1
            i += 1
            j += 1
        return 0
```
```Java []
class Solution {
    public int compareVersion(String version1, String version2) {
        int m = version1.length(), n = version2.length();
        for(int i=0,j=0; i<m||j<n; i++,j++){
            int a = 0, b = 0;
            while(i<m && version1.charAt(i) != '.')
                a = 10 * a + (version1.charAt(i++) - '0');
            while(j<n && version2.charAt(j) != '.')
                b = 10 * b + (version2.charAt(j++) - '0');
            if(a<b)
                return -1;
            else if(a>b)
                return 1;
        }
        return 0;
    }
}
```

### Complexity
Time complexity o(m+n)
Space complexity o(1)
