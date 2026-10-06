# [Python/Java/JavaScript/Go] Trie + depth-first search

> slug: pythonjavajavascriptgo-zi-dian-shu-shen-3fuzq
> date: 2021-12-27
> tags: Go, Java, JavaScript, Python, Python3
> question: Concatenated Words (concatenated-words)
> url: https://leetcode.cn/problems/concatenated-words/solutions/Zg5SCe/pythonjavajavascriptgo-zi-dian-shu-shen-3fuzq/

---
### Approach
This problem is quite difficult.
First, understand prefix trees, or Tries. If unfamiliar, read [this explanation by 叶总](https://leetcode.cn/problems/implement-trie-prefix-tree/solution/gong-shui-san-xie-yi-ti-shuang-jie-er-we-esm9/).
Use the Trie to match prefixes. Whenever a match reaches the end of a previously stored word, tentatively treat that prefix as part of the current concatenated word and recurse on the remaining string.
If the remainder is itself a concatenated word or exists in the Trie, the current word is valid. Otherwise, abandon that split and keep searching farther along for another split.

Check for a match before deciding whether to insert into the Trie. Inserting first would let a word match itself and always return True. The input contains no duplicate words, so identical-word matches cannot otherwise cause True.
When the result is True, insertion into the Trie is unnecessary: the cache records that the word is concatenated whenever it appears again.

[I wrote the Trie templates for each language; discussion and improved templates are welcome.]

The post disappeared, and then comments were disabled? That is too much.

### Code

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
