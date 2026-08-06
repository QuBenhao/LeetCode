# [Python/Java/JavaScript/Go] 存储排序后的set 或 位运算替代

> slug: pythonjavajavascriptgo-zi-zhi-hashable-s-tuxj
> date: 2021-11-16
> tags: Go, Java, JavaScript, Python, Python3
> question: Maximum Product of Word Lengths (maximum-product-of-word-lengths)
> url: https://leetcode.cn/problems/maximum-product-of-word-lengths/solutions/GNZTGJ/pythonjavajavascriptgo-zi-zhi-hashable-s-tuxj/

---
### 解题思路
很直观的想到用集合去判断单词之间有没有交集，然后用哈希表存储之前的一些集合的最长长度，在这些长度里找当前集合不存在交集的最大乘积。
但是Set是unhashable的，不能作为哈希表的key。
两种解决方案，用排序后拼接的字符串代替；或用26位位运算表示26个字母被使用的情况。

### 代码

```python3
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d, ans = defaultdict(int), 0
        for w in words:
            s = set(w)
            # 用排序后拼接的字符串作为哈希值
            he = "".join(sorted(s))
            if d[he] < len(w):
                for other in d:
                    # 取出来的字符串再取集合，集合没有交集才有可能作为答案
                    if not set(other) & s:
                        ans = max(ans, len(w) * d[other])
                d[he] = len(w)
        return ans
```
```Python3 []
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def hashset(word):
            # 用26位位运算表示二十六个字母在word中被使用的情况
            return sum(1 << (ord(c) - ord('a')) for c in set(word))

        d, ans = defaultdict(int), 0
        for w in words:
            h = hashset(w)
            if d[h] < len(w):
                for other in d:
                    # 如果位运算&的结果为0，说明他们没有使用过同样的字母，可以计算答案
                    if not other & h:
                        ans = max(d[other] * len(w), ans)
                d[h] = len(w)
        return ans
```
```Java []
class Solution {
    public int maxProduct(String[] words) {
        Map<Integer, Integer> map = new HashMap<>();
        int ans = 0;
        for(String word: words){
            int h = hash(word), n = word.length();
            if(map.containsKey(h) && map.get(h) >= n)
                continue;
            for(int other: map.keySet()){
                if((other & h) == 0){
                    ans = Math.max(ans, map.get(other) * n);
                }
            }
            map.put(h, n);
        }
        return ans;
    }

    private int hash(String word){
        int res = 0;
        for(int i=0;i<word.length();i++)
            res |= 1 << (word.charAt(i) - 'a');
        return res;
    }
}
```
```JavaScript []
/**
 * @param {string[]} words
 * @return {number}
 */
var maxProduct = function(words) {
    const map = new Map();
    let ans = 0;
    for(const word of words){
        const h = hash(word), n = word.length;
        if(map.has(h) && map.get(h) >= n)
            continue;
        for(const other of map.keys())
            if((other & h) == 0)
                ans = Math.max(ans, map.get(other) * n);
        map.set(h, n);
    }
    return ans;
};

var hash = function(word) {
    let res = 0;
    for(let i=0;i<word.length;i++)
        res |= 1 << (word[i].charCodeAt() - 'a'.charCodeAt());
    return res;
};
```
```Go []
func maxProduct(words []string) int {
    hash := func(word string) int {
        res := 0
        for _, r := range word{
            res |= 1 << (r - 'a')
        }
        return res
    }

    m, ans := map[int]int{}, 0
    for _, word := range words {
        h := hash(word)
        if m[h] < len(word) {
            for other, v := range m {
                if((other & h) == 0){
                    if tmp := v * len(word); tmp > ans {
                        ans = tmp
                    }
                }
            }
            m[h] = len(word)
        }
    }
    return ans
}
```