# [Go] Count how many times each vowel appears

> slug: go-tong-ji-mei-ge-yuan-yin-zi-mu-neng-ge-yqnl
> date: 2021-11-07
> tags: Go
> question: Vowels of All Substrings (vowels-of-all-substrings)
> url: https://leetcode.cn/problems/vowels-of-all-substrings/solutions/fugYG0/go-tong-ji-mei-ge-yuan-yin-zi-mu-neng-ge-yqnl/

---
### Approach
The key is to count how many substrings contain a given character.
There are i + 1 choices before and including this character for the substring's starting position,
and n - i choices at or after it for the ending position.
Their product is the number of times it appears.

### Code

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
