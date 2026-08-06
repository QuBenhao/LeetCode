# [Python/Java/TypeScript/Go] 暴力

> slug: pythonjavatypescriptgo-ba-by-himymben-2zon
> date: 2022-08-06
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: String Matching in an Array (string-matching-in-an-array)
> url: https://leetcode.cn/problems/string-matching-in-an-array/solutions/YvUrSL/pythonjavatypescriptgo-ba-by-himymben-2zon/

---
### 解题思路
一个字符串在所有字符串里以子字符串出现不止一次(抛去自身)，
说明就在答案中。

PS:
可以直接用`indexOf(subStr) != lastIndexOf(subStr)`判断出现了不止一次

### 代码

```Python3 []
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [w for w in words if s.count(w) > 1] if (s := "#".join(words)) else []
```
```Java []
class Solution {
    public List<String> stringMatching(String[] words) {
        String s = String.join("#", words);
        List<String> ans = new ArrayList<>();
        for (String word: words) {
            if (s.indexOf(word) != s.lastIndexOf(word)) {
                ans.add(word);
            }
        }
        return ans;
    }
}
```
```TypeScript []
function stringMatching(words: string[]): string[] {
    const s = words.join("#"), ans = new Array<string>()
    for (const word of words) {
        if (s.indexOf(word) !== s.lastIndexOf(word)) {
            ans.push(word)
        }
    }
    return ans
};
```
```Go []
func stringMatching(words []string) (ans []string) {
    s := strings.Join(words, "#")
    for _, word := range words {
        if strings.Index(s, word) != strings.LastIndex(s, word) {
            ans = append(ans, word)
        }
    }
    return
}
```
简洁写法
```Java []
class Solution {
    public List<String> stringMatching(String[] words) {
        String s = String.join("#", words);
        return Arrays.stream(words).filter(w -> s.indexOf(w) != s.lastIndexOf(w)).collect(Collectors.toList());
    }
}
```
```TypeScript []
function stringMatching(words: string[]): string[] {
    const s = words.join("#")
    return words.filter((word) => s.indexOf(word) !== s.lastIndexOf(word))
};
```