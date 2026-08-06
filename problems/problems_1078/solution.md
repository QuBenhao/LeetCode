# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-mo-ni-by-himymben-fwz9
> date: 2021-12-26
> tags: Go, Java, JavaScript, Python, Python3
> question: Occurrences After Bigram (occurrences-after-bigram)
> url: https://leetcode.cn/problems/occurrences-after-bigram/solutions/hjk9em/pythonjavajavascriptgo-mo-ni-by-himymben-fwz9/

---
```Python3 []
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        for i, w in enumerate((words:=text.split(" "))):
            if i < len(words) - 2 and w == first and words[i+1] == second:
                ans.append(words[i+2])
        return ans
```
```Java []
class Solution {
    public String[] findOcurrences(String text, String first, String second) {
        String[] words = text.split(" ");
        List<String> ans = new ArrayList<>();
        for(int i=0;i<words.length-2;i++)
            if(words[i].compareTo(first) == 0 && words[i+1].compareTo(second) == 0)
                ans.add(words[i+2]);
        return ans.toArray(new String[ans.size()]);
    }
}
```
```JavaScript []
/**
 * @param {string} text
 * @param {string} first
 * @param {string} second
 * @return {string[]}
 */
var findOcurrences = function(text, first, second) {
    const words = text.split(" "), ans = new Array()
    for(let i=0;i<words.length-2;i++)
        if(words[i] === first && words[i+1] === second)
            ans.push(words[i+2])
    return ans
};
```
```Go []
func findOcurrences(text string, first string, second string)(ans []string) {
    words := strings.Split(text, " ")
    for i:=0;i<len(words)-2;i++{
        if words[i] == first && words[i+1] == second{
            ans = append(ans, words[i+2])
        }
    }
    return
}
```
