# [Python/Java/JavaScript/Go] Store sorted sets or use bit manipulation

> slug: pythonjavajavascriptgo-zi-zhi-hashable-s-tuxj
> date: 2021-11-16
> tags: Go, Java, JavaScript, Python, Python3
> question: Maximum Product of Word Lengths (maximum-product-of-word-lengths)
> url: https://leetcode.cn/problems/maximum-product-of-word-lengths/solutions/GNZTGJ/pythonjavajavascriptgo-zi-zhi-hashable-s-tuxj/

---
### Approach
A natural approach is to check whether word sets intersect. Store the maximum length seen for each set in a hash table, then find the largest product with a set disjoint from the current one.
However, Set is unhashable and cannot serve as a hash table key.
Two options: use a string formed by sorting and joining the set, or use 26 bits to represent which letters occur.

### Code

```python3
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d, ans = defaultdict(int), 0
        for w in words:
            s = set(w)
            # Use a sorted, joined string as the hash key
            he = "".join(sorted(s))
            if d[he] < len(w):
                for other in d:
                    # Convert the stored string back to a set; only disjoint sets can produce an answer
                    if not set(other) & s:
                        ans = max(ans, len(w) * d[other])
                d[he] = len(w)
        return ans
```
```Python3 []
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def hashset(word):
            # Use 26 bits to represent which of the 26 letters appear in word
            return sum(1 << (ord(c) - ord('a')) for c in set(word))

        d, ans = defaultdict(int), 0
        for w in words:
            h = hashset(w)
            if d[h] < len(w):
                for other in d:
                    # A bitwise AND of 0 means no letters are shared, so this pair can contribute to the answer
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
