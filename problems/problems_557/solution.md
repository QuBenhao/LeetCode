# [Go] 双指针 or 栈

> slug: go-shuang-zhi-zhen-by-himymben-yxh3
> date: 2022-01-21
> tags: Go
> question: Reverse Words in a String III (reverse-words-in-a-string-iii)
> url: https://leetcode.cn/problems/reverse-words-in-a-string-iii/solutions/spNRwd/go-shuang-zhi-zhen-by-himymben-yxh3/

---
```golang
func reverseWords(s string) string {
    bs := []byte(s)
    for i, j := 0, 0; j <= len(s); j++ {
        if j == len(s) || s[j] == ' '{
            r := j
            j -= 1
            for i < j {
                bs[i], bs[j] = bs[j], bs[i]
                i++
                j--
            }
            j = r
            i = j + 1
        }
    }
    return string(bs[:])
}
```
```golang
func reverseWords(s string) string {
    stack, ans := []byte{}, []byte{}
    for i := 0; i <= len(s); i++ {
        if i == len(s) || s[i] == ' ' {
            for len(stack) > 0 {
                b := stack[len(stack) - 1]
                stack = stack[:len(stack)-1]
                ans = append(ans, b)
            }
            ans = append(ans, ' ')
        } else {
            stack = append(stack, s[i])
        }
    }
    return string(ans[:len(ans) - 1])
}
```