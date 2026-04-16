# 哈希模拟

> Author: Benhao
> Date: 2022-12-12
> Upvotes: 6
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

```Python3 []
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(sentence) >= 26 and len(set(sentence)) == 26
```
```Go []
func checkIfPangram(sentence string) bool {
    if len(sentence) < 26 {
        return false
    }
    set := map[rune]struct{}{}
    for _, r := range sentence {
        set[r] = struct{}{}
    }
    return len(set) == 26
}
```
```Java []
class Solution {
    public boolean checkIfPangram(String sentence) {
        return sentence.chars().distinct().count() == 26;
    }
}
```
```Cpp []
class Solution {
public:
    bool checkIfPangram(string sentence) {
        set<char> s;
        for (auto c: sentence) s.insert(c);
        return s.size() == 26;
    }
};
```

感谢[@伊泽瑞尔](/u/herestars)、[@阿尼亚](/u/coco-e1) 小伙伴儿们提供的其他语言版本
