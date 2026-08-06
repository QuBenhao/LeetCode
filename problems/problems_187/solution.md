# [Python/Java/JavaScript] 哈希

> slug: pythonjavajavascript-ha-xi-by-himymben-wcr9
> date: 2021-10-07
> tags: Java, JavaScript, Python, Python3
> question: Repeated DNA Sequences (repeated-dna-sequences)
> url: https://leetcode.cn/problems/repeated-dna-sequences/solutions/3hNzmM/pythonjavajavascript-ha-xi-by-himymben-wcr9/

---
### 解题思路
遍历所有长度为10的子串，统计哈希个数

### 代码

```Python3 []
LEN = 10
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        return [k for k,v in Counter(s[i:i+LEN] for i in range(len(s) - LEN + 1)).items() if v > 1]
```
```Java []
class Solution {
    private static final int LEN = 10;
    public List<String> findRepeatedDnaSequences(String s) {
        Map<String, Integer> cnts = new HashMap<>();
        List<String> ans = new ArrayList<>();
        int n = s.length();
        for(int i=0;i<n-LEN+1;i++){
            String sub = s.substring(i,i+LEN);
            if(cnts.containsKey(sub)){
                int cnt = cnts.get(sub);
                if(cnt == 1){
                    ans.add(sub);
                    cnts.put(sub, cnt+1);
                }
            }else
                cnts.put(sub, 1);
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @return {string[]}
 */
const LEN = 10;
var findRepeatedDnaSequences = function(s) {
    const cnts = new Map(), ans = [];
    for(let i=0;i<s.length-LEN+1;i++){
        let sub = s.substring(i, i+LEN);
        if(cnts.has(sub)){
            if(cnts.get(sub) == 1){
                ans.push(sub);
                cnts.set(sub, 2);
            }
        } else
            cnts.set(sub, 1);
    }
    return ans;
};
```