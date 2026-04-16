# [Python/Java] 排序后暴力匹配

> Author: Benhao
> Date: 2021-09-13
> Upvotes: 6
> Tags: Java, Python, Python3

---

### 解题思路
按字符串长度、字典序排序后，匹配该字符串是否能由s组成，能的话就返回该字符串，否则继续往后找。

### 代码

```Python3 []
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        for word in sorted(dictionary, key = lambda x:(-len(x), x)):
            idx, mark = 0, True
            for c in word:
                idx = s.find(c, idx) + 1
                if not idx:
                    mark = False
                    break
            if mark:
                return word
        return ""
```
```Java []
class Solution {
    public String findLongestWord(String s, List<String> dictionary) {
        Collections.sort(dictionary, new Comparator<String>(){
            public int compare(String s1, String s2){
                if(s1.length() > s2.length())
                    return -1;
                else if(s1.length() < s2.length())
                    return 1;
                return s1.compareTo(s2);
            }
        });
        for(String word: dictionary){
            int idx = 0, i = 0;
            while(i < word.length() && idx < s.length()){
                if(word.charAt(i) == s.charAt(idx))
                    i++;
                idx++;
            }
            if(i == word.length())
                return word;
        }
        return "";
    }
}
```