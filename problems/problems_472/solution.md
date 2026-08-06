# [Python/Java/JavaScript/Go] 字典树 + 深度优先搜索

> slug: pythonjavajavascriptgo-zi-dian-shu-shen-3fuzq
> date: 2021-12-27
> tags: Go, Java, JavaScript, Python, Python3
> question: Concatenated Words (concatenated-words)
> url: https://leetcode.cn/problems/concatenated-words/solutions/Zg5SCe/pythonjavajavascriptgo-zi-dian-shu-shen-3fuzq/

---
### 解题思路
这题蛮难的。
首先要掌握字典树、Trie树，不了解的同学可以先看看[叶总的这篇](https://leetcode.cn/problems/implement-trie-prefix-tree/solution/gong-shui-san-xie-yi-ti-shuang-jie-er-we-esm9/)。
有了字典树的前缀树知识我们可以根据前缀匹配字符串，当我们匹配到任意遍历过的子串结尾时，我们可以暂时认定该子串是组成我们当前连接词的一部分，剩余的字符串我们进行递归，
如果剩余的字符串也是连接词或在字典树中存在，我们知道它必然是合格的连接词了。如果当前子串分割后后面不能构成连接词，我们要放弃刚刚的假定，继续往后面尝试分割。

要先查找匹配，后决定是否添加到字典树中。如果先添加，会导致自己表示自己，必然为True。这里还有个原因是原数组没有重复单词，所以我们必然不会因为相同单词匹配结果为True。
结果为True不需要添加到字典树中，根据缓存即可知道再遇到它永远是连接词了。

【各语言的Trie树模板，我自己写的，欢迎探讨和提供更好的模板】

帖子还能被吞了？吞完还不让评论？过分了

### 代码

```Python3 []
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie, ans = Trie(), []
        for word in sorted(words, key=len):
            if word == "":
                continue
            if trie.find(word):
                ans.append(word)
            else:
                trie.insert(word)
        return ans

class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        node = self.root
        for w in word + "#":
            if w not in node:
                node[w] = {}
            node = node[w]
    
    def find(self, word):
        node = self.root
        for i in range(len(word)):
            if "#" in node:
                if self.find(word[i:]):
                    return True
            if word[i] in node:
                node = node[word[i]]
            else:
                return False
        return "#" in node
```
```Java []
class Solution {
    private Trie root;
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        root = new Trie();
        Arrays.sort(words, (a, b) -> a.length() - b.length());
        List<String> ans = new ArrayList<>();
        for(String word: words){
            if(word.length() == 0)
                continue;
            if(find(root, word)){
                ans.add(word);
            }else{
                insert(root, word);
            }
        }
        return ans;
    }

    private void insert(Trie node, String word){
        for(int i=0;i<word.length();i++){
            int idx = word.charAt(i) - 'a';
            if(node.children[idx] == null)
                node.children[idx] = new Trie();
            node = node.children[idx];
        }
        node.isEnd = true;
    }

    private boolean find(Trie root, String word){
        Trie node = root;
        for(int i=0;i<word.length();i++){
            if(node.isEnd)
                if(find(root, word.substring(i, word.length())))
                    return true;
            int idx = word.charAt(i) - 'a';
            if(node.children[idx] == null)
                return false;
            node = node.children[idx];
        }
        return node.isEnd;
    }

    private class Trie {
        public Trie[] children;
        public Boolean isEnd;
        public Trie(){
            children = new Trie[26];
            isEnd = false;
        }
    }
}
```
```JavaScript []
/**
 * @param {string[]} words
 * @return {string[]}
 */
var findAllConcatenatedWordsInADict = function(words) {
    const root = new Trie(), ans = new Array()
    words.sort((a,b)=>(a.length - b.length))
    for(const word of words){
        if(word.length == 0)
            continue
        if(root.find(root, word))
            ans.push(word)
        else
            root.insert(word)
    }
    return ans
};

class Trie{
    constructor(){
        this.children = new Array(26)
        this.isEnd = false
    }

    insert(word){
        let node = this
        for(let i=0;i<word.length;i++){
            const idx = word.charCodeAt(i) - 'a'.charCodeAt(0)
            if(node.children[idx] === undefined)
                node.children[idx] = new Trie()
            node = node.children[idx]
        }
        node.isEnd = true
    };

    find(root, word){
        let node = root
        for(let i=0;i<word.length;i++){
            if(node.isEnd)
                if(this.find(root, word.substring(i, word.length)))
                    return true
            const idx = word.charCodeAt(i) - 'a'.charCodeAt(0)
            if(node.children[idx] === undefined)
                return false
            node = node.children[idx]
        }
        return node.isEnd
    }
}
```
```Go []
func findAllConcatenatedWordsInADict(words []string) []string {
    root, ans := trie{}, []string{}
    sort.Slice(words, func(i, j int) bool { return len(words[i]) < len(words[j]) })
    for _, word := range words {
        if len(word) == 0{
            continue
        }
        if root.find(word) {
            ans = append(ans, word)
        }else{
            root.insert(word)
        }
    }
    return ans
}

type trie struct {
    children [26]*trie
    isEnd    bool
}

func (root *trie) insert(word string) {
    node := root
    for i := 0; i < len(word); i++{
        idx := word[i] - byte('a')
        if node.children[idx] == nil {
            node.children[idx] = &trie{}
        }
        node = node.children[idx]
    }
    node.isEnd = true
}

func (root *trie) find(word string) bool {
    node := root
    for i := 0; i < len(word); i++ {
        if node.isEnd {
            if root.find(word[i:]){
                return true
            }
        }
        idx := word[i] - byte('a')
        if node.children[idx] == nil {
            return false
        }
        node = node.children[idx]
    }
    return node.isEnd
}
```