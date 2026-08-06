# [Python/Java/JavaScript] 模拟

> slug: pythonjavajavascript-mo-ni-by-himymben-f3vx
> date: 2021-10-30
> tags: Java, JavaScript, Python, Python3
> question: Keyboard Row (keyboard-row)
> url: https://leetcode.cn/problems/keyboard-row/solutions/SrScWa/pythonjavajavascript-mo-ni-by-himymben-f3vx/

---
```Python3 []
LINES = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return [word for word in words if any(set(word.lower()).issubset(LINE) for LINE in LINES)]
```
```Java []
class Solution {
    private static final Map<Character, Integer> map = new HashMap<>();
    static{
        String[] strs = new String[]{"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        for(int i=0;i<strs.length;i++){
            String cur = strs[i];
            for(int j=0;j<cur.length();j++){
                map.put(cur.charAt(j), i);
                map.put(Character.toUpperCase(cur.charAt(j)), i);
            }
        }
    }
    public String[] findWords(String[] words) {
        List<String> ans = new ArrayList<>();
        for(String word: words){
            boolean check = true;            
            Set<Integer> lines = new HashSet<>();
            for(int i=0;i<word.length();i++){
                lines.add(map.get(word.charAt(i)));
                if(lines.size() > 1){
                    check = false;
                    break;
                }
            }
            if(check)
                ans.add(word);
        }
        String[] res = new String[ans.size()];
        for(int i=0;i<ans.size();i++)
            res[i] = ans.get(i);
        return res;
    }
}
```
```JavaScript []
/**
 * @param {string[]} words
 * @return {string[]}
 */
const strs = ["qwertyuiop", "asdfghjkl", "zxcvbnm"];
const map = new Array(26);
for(let i=0;i<strs.length;i++)
    for(let j=0;j<strs[i].length;j++)
        map[strs[i].charAt(j).charCodeAt() - 'a'.charCodeAt()] = i;

var findWords = function(words) {
    const res = [];
    for(const word of words){
        const lowerword = word.toLowerCase();
        const check = new Set();
        for(let j=0;j<word.length;j++){
            check.add(map[lowerword.charAt(j).charCodeAt() - 'a'.charCodeAt()]);
            if(check.size > 1)
                break;
        }
        if(check.size<=1)
            res.push(word);
    }
    return res;
};
```