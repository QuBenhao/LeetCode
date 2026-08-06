# [Python/Java/TypeScript/Go] 字典树应用题

> slug: pythonjavatypescriptgo-zi-dian-shu-ying-pjwyp
> date: 2022-07-06
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Replace Words (replace-words)
> url: https://leetcode.cn/problems/replace-words/solutions/31ZzS4/pythonjavatypescriptgo-zi-dian-shu-ying-pjwyp/

---
### 解题思路
前置知识: [Trie字典树](https://leetcode.cn/problems/implement-trie-prefix-tree/solution/gong-shui-san-xie-yi-ti-shuang-jie-er-we-esm9/)

根据题目给的前缀(词根)创建字典树，遍历句子中的每个单词，替换为第一个与字典树匹配的前缀。
与其他题目的Trie树的搜索用法不同的是，我们不需要保证整个单词属于字典树中或整个单词可以拆解成字典树中的单词，只需要找到第一次匹配到的前缀即可，所以这里写了一个新的查询方法。

### 代码

```Python3 []
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for d in dictionary:
            trie.insert(d)
        words = sentence.split(" ")
        return " ".join(trie.find_sp(word) for word in words)

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
    
    def find_sp(self, word: str) -> str:
        node = self.root
        for i in range(len(word)):
            if "#" in node:
                return word[:i]
            if word[i] in node:
                node = node[word[i]]
            else:
                break
        return word
```
```Java []
class Solution {
    private Trie root;

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

    private String findSp(Trie root, String word) {
        Trie node = root;
        for(int i = 0; i < word.length(); i++){
            if(node.isEnd) {
                return word.substring(0, i);
            }
            int idx = word.charAt(i) - 'a';
            if(node.children[idx] == null)
                break;
            node = node.children[idx];
        }
        return word;
    }

    private class Trie {
        public Trie[] children;
        public Boolean isEnd;
        public Trie(){
            children = new Trie[26];
            isEnd = false;
        }
    }

    public String replaceWords(List<String> dictionary, String sentence) {
        root = new Trie();
        for (String dict: dictionary) {
            insert(root, dict);
        }
        StringBuilder sb = new StringBuilder();
        String[] splits = sentence.split(" ");
        for (int i = 0; i < splits.length; i++) {
            sb.append(findSp(root, splits[i]));
            if (i < splits.length - 1) {
                sb.append(" ");
            }
        }
        return sb.toString();
    }
}
```
```TypeScript []
function replaceWords(dictionary: string[], sentence: string): string {
    const root = new Trie()
    for(const dict of dictionary) {
        root.insert(dict)
    }
    const words = sentence.split(" ").map((word) => root.findSp(root, word))
    return words.join(" ")
};

class Trie{
    children: Array<Trie>
    isEnd: boolean
    trans: Function
    constructor(){
        this.children = new Array<Trie>(26)
        this.isEnd = false
    }

    insert(word: string): void{
        let node: Trie = this
        for(let i=0;i<word.length;i++){
            const idx = word.charCodeAt(i) - 'a'.charCodeAt(0)
            if(node.children[idx] === undefined)
                node.children[idx] = new Trie()
            node = node.children[idx]
        }
        node.isEnd = true
    };

    find(root: Trie, word: string): boolean{
        let node: Trie = root
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

    findSp(root: Trie, word: string): string{
        let node: Trie = root
        for(let i = 0; i < word.length; i++){
            if(node.isEnd)
                return word.substring(0, i)
            const idx = word.charCodeAt(i) - 'a'.charCodeAt(0)
            if(node.children[idx] === undefined)
                break
            node = node.children[idx]
        }
        return word
    }
}
```
```Go []
func replaceWords(dictionary []string, sentence string) string {
    root := &trie{}
    for _, d := range dictionary {
        root.insert(d)
    }
    words := strings.Split(sentence, " ")
    for i, w := range words {
        words[i] = root.findSp(w)
    }
    return strings.Join(words, " ")
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

func (root *trie) findSp(word string) string {
    node := root
    for i := 0; i < len(word); i++ {
        if node.isEnd {
            return word[:i]
        }
        idx := word[i] - byte('a')
        if node.children[idx] == nil {
            break
        }
        node = node.children[idx]
    }
    return word
}
```