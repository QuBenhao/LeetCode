# [Python/Java/JavaScript/Go] 贪心大模拟

> slug: python-tan-xin-da-mo-ni-by-himymben-6cbl
> date: 2022-03-01
> tags: Go, Java, JavaScript, Python, Python3
> question: Find the Closest Palindrome (find-the-closest-palindrome)
> url: https://leetcode.cn/problems/find-the-closest-palindrome/solutions/vX4eK9/python-tan-xin-da-mo-ni-by-himymben-6cbl/

---
### 解题思路

[贪心]一个数字最近的回文数是取自身的一半，再做加减一再做对称里的一个数。
但是细节情况特别多，比如99最近的是101而不是根据贪心生成的88或1001，1001最近的是999也不是99或者1111。
最后决定把所有有可能性的答案加进去然后比较最小的作为答案。

PS: 代码中对长度为1的特判可以去掉，因为后面还是可以正常处理长度为1的结果。

### 代码

```Python3 []
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            return str(int(n) - 1)
        l = len(n)
        half, v, ov = n[:l//2], int(n[:(l+1)//2]), int(n)
        res = set()
        s1, s2 = str(v-1), str(v + 1)
        res.add("9" * (l - 1))
        res.add("1" + "0" * (l - 1) + "1")
        if l % 2:
            res.add(s1[:-1] + s1[-1] + s1[:-1][::-1])
            res.add(s2[:-1] + s2[-1] + s2[:-1][::-1])
        else:
            res.add(s1 + s1[::-1])
            res.add(s2 + s2[::-1])
        if n[::-1] != n:
            res.add(half + n[l//2] + half[::-1] if l % 2 else half + half[::-1])
        if n in res:
            res.remove(n)
        return min(res, key = lambda x:(abs((k:=int(x)) - ov), k))
```
```Java []
class Solution {
    public String nearestPalindromic(String n) {
        int len = n.length();
        if(len == 1)
            return String.valueOf(Integer.parseInt(n) - 1);
        Set<Long> set = new HashSet<>();
        set.add((long)Math.pow(10, len - 1) - 1);
        set.add((long)Math.pow(10, len) + 1);
        long half = Long.parseLong(n.substring(0, (len+1)/2)), nVal = Long.parseLong(n);
        if((len & 1) == 1) {
            set.add(getLong((half + 1) / 10, half + 1));
            set.add(getLong(half / 10, half));
            set.add(getLong((half - 1) / 10, half - 1));
        } else {
            set.add(getLong(half + 1, half + 1));
            set.add(getLong(half, half));
            set.add(getLong(half - 1, half - 1));
        }
        long ans = -1;
        for(Long other: set) {
            if(other != nVal) {
                if(ans == -1)
                    ans = other;
                else if(Math.abs(other - nVal) < Math.abs(ans - nVal))
                    ans = other;
                else if(other < ans && Math.abs(other - nVal) == Math.abs(ans - nVal))
                    ans = other;
            }
        }
        return String.valueOf(ans);
    }

    private long getLong(long original, long v) {
        for(;original>0;original/=10)
            v = 10 * v + original % 10;
        return v;
    }
}
```
```JavaScript []
/**
 * @param {string} n
 * @return {string}
 */
var nearestPalindromic = function(n) {
    getBigInt = function(orignal, v) {
        for(;orignal > 0; orignal /= 10n)
            v = 10n * v + orignal % 10n
        return v
    }

    const len = n.length, nVal = BigInt(n)
    if(len == 1)
        return nVal - 1n + ''
    const half = BigInt(n.substr(0, (len + 1) >> 1)), ans = new Set()
    ans.add(BigInt(Math.pow(10, len - 1)) - 1n)
    ans.add(BigInt(Math.pow(10, len)) + 1n)
    if(len & 1 == 1) {
        ans.add(getBigInt((half+1n)/10n, half + 1n))
        ans.add(getBigInt(half/10n, half))
        ans.add(getBigInt((half-1n)/10n, half - 1n))
    } else {
        ans.add(getBigInt(half + 1n, half + 1n))
        ans.add(getBigInt(half, half))
        ans.add(getBigInt(half - 1n, half - 1n))
    }
    let res = -1
    for(const other of ans) {
        if(other != nVal) {
            if(res == -1)
                res = other
            let o = other - nVal, r = res - nVal
            if(o < 0)
                o *= -1n
            if(r < 0)
                r *= -1n
            if(o < r || (other < res && o == r))
                res = other
        }
    }
    return res + ''
};
```
```Go []
func nearestPalindromic(n string) string {
    getNum := func(original, v int64) int64 {
        for ; original > 0; original /= 10 {
            v = 10 * v + original % 10
        }
        return v
    }

    l := len(n)
    nVal, _ := strconv.ParseInt(n, 10, 64)
    if l == 1{
        return strconv.FormatInt(nVal - 1, 10) 
    }
    ans := map[int64]bool{}
    ans[int64(math.Pow(10, float64(l - 1))) - 1] = true
    ans[int64(math.Pow(10, float64(l))) + 1] = true
    half, _ := strconv.ParseInt(n[:(l+1)/2], 10, 64)
    if l & 1 == 1 {
        ans[getNum((half + 1)/10, half + 1)] = true
        ans[getNum(half/10, half)] = true
        ans[getNum((half - 1)/10, half - 1)] = true
    } else {
        ans[getNum(half + 1, half + 1)] = true
        ans[getNum(half, half)] = true
        ans[getNum(half - 1, half - 1)] = true
    }
    res := int64(-1)
    for other, _ := range ans {
        if other != nVal && other > 0 {
            if res == -1 {
                res = other
            } else if d1, d2 := absSub(other, nVal), absSub(res, nVal); d1 < d2 {
                res = other
            } else if other < res && d1 == d2 {
                res = other
            }
        }
    }
    return strconv.FormatInt(res,10) 
}

func absSub(a, b int64) int64 {
    if a < b {
        return b - a
    }
    return a - b
}
```