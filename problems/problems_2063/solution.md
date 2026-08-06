# [Go] 统计每个元音字母能各自出现多少次

> slug: go-tong-ji-mei-ge-yuan-yin-zi-mu-neng-ge-yqnl
> date: 2021-11-07
> tags: Go
> question: Vowels of All Substrings (vowels-of-all-substrings)
> url: https://leetcode.cn/problems/vowels-of-all-substrings/solutions/fugYG0/go-tong-ji-mei-ge-yuan-yin-zi-mu-neng-ge-yqnl/

---
### 解题思路
这题的本质是求一个字母能出现在所有子串中多少次，
这个字母出现在它前半段中有 i + 1 种 （子串起始位置），
出现在后半段中有 n - i 种（子串结束位置），
乘起来便是它出现的次数了

### 代码

```golang
func countVowels(word string) (ans int64) {
    n := len(word)
    for i, ch := range word {
        if strings.ContainsRune("aeiou", ch) {
            ans += int64((i + 1) * (n - i))
        }
    }
    return 
}
```