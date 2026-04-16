# [Python/Java] 双指针逐位比较(小数点)

> Author: Benhao
> Date: 2021-08-31
> Upvotes: 25
> Tags: Java, Python, Python3

---

### 解题思路
我们每次统计小数点和小数点之间的数字大小，然后比较两者谁大即可。没有的始终默认为0。
也就是说`1.0.0.0.0`和`1`没有区别，除非后面有个大于0的一位，我们要一直比较到出现大小差异的那位，否则他们相等。

### 代码

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

### 复杂度
时间复杂度 o(m+n)
空间复杂度 o(1)