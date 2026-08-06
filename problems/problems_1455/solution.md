# [Python/Java/TypeScript/Go] 模拟

> slug: pythonjavatypescriptgo-by-himymben-e5bb
> date: 2022-08-21
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Check If a Word Occurs As a Prefix of Any Word in a Sentence (check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence)
> url: https://leetcode.cn/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/solutions/dO46Fq/pythonjavatypescriptgo-by-himymben-e5bb/

---
### 解题思路
嗯

### 代码

```Python3 []
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split(" "), 1):
            if word[:len(searchWord)] == searchWord:
                return i
        return -1
```
```Java []
class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {
        String[] splits = sentence.split(" ");
        for (int i = 0; i < splits.length; i++) {
            if (splits[i].length() >= searchWord.length() && splits[i].substring(0, searchWord.length()).equals(searchWord)) {
                return i + 1;
            }
        }
        return -1;
    }
}
```
```TypeScript []
function isPrefixOfWord(sentence: string, searchWord: string): number {
    return sentence.split(" ").findIndex((value: string) => value.startsWith(searchWord)) + 1 || -1
};
```
```Go []
func isPrefixOfWord(sentence string, searchWord string) int {
    splits := strings.Split(sentence, " ")
    for i, s := range splits {
        if len(s) >= len(searchWord) && s[:len(searchWord)] == searchWord {
            return i + 1
        }
    }
    return -1
}
```