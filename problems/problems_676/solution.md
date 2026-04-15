# [Python/Java/TypeScript/Go] 模拟

> Author: Benhao
> Date: 2022-07-10
> Upvotes: 18
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
看了眼数据范围，然后只能替换字母不能添加和删除，哈希表存按单词长度分类，然后搜索的时候遍历对应长度即可。

PS：
昨天早上起来就忙同学的婚礼，到飞回家已经晚上十一点了，所以昨天就连题目都没读用手机cv了一下

### 代码

```Python3 []
class MagicDictionary:

    def __init__(self):
        self.mp = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for d in dictionary:
            self.mp[len(d)].append(d)

    def search(self, searchWord: str) -> bool:
        for d in self.mp[len(searchWord)]:
            if sum(c0 != c1 for c0, c1 in zip(searchWord, d)) == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
```
```Java []
class MagicDictionary {
    private Map<Integer, List<String>> map;

    public MagicDictionary() {
        map = new HashMap<>();
    }
    
    public void buildDict(String[] dictionary) {
        for (String d: dictionary) {
            List<String> list = map.getOrDefault(d.length(), new ArrayList<>());
            list.add(d);
            map.put(d.length(), list);
        }
    }
    
    public boolean search(String searchWord) {
        if (map.containsKey(searchWord.length())) {
            out:
            for (String d: map.get(searchWord.length())) {
                int cnt = 0;
                for (int i = 0; i < d.length(); i++) {
                    if (searchWord.charAt(i) != d.charAt(i) && ++cnt > 1) {
                        continue out;
                    }
                }
                if (cnt == 1) {
                    return true;
                }
            }
        }
        return false;
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dictionary);
 * boolean param_2 = obj.search(searchWord);
 */
```
```TypeScript []
class MagicDictionary {
    map: Map<number, Array<string>> 
    constructor() {
        this.map = new Map<number, Array<string>>()
    }

    buildDict(dictionary: string[]): void {
        for (const d of dictionary) {
            let list: Array<string>
            if (this.map.has(d.length)) {
                list = this.map.get(d.length)
            } else {
                list = new Array<string>()
            }
            list.push(d)
            this.map.set(d.length, list)
        }
    }

    search(searchWord: string): boolean {
        if (this.map.has(searchWord.length)) {
            out:
            for (const d of this.map.get(searchWord.length)) {
                let cnt = 0
                for (let i = 0; i < d.length; i++) {
                    if (searchWord.charCodeAt(i) !== d.charCodeAt(i) && ++cnt > 1) {
                        continue out
                    }
                }
                if (cnt == 1) {
                    return true
                }
            }
        }
        return false
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * var obj = new MagicDictionary()
 * obj.buildDict(dictionary)
 * var param_2 = obj.search(searchWord)
 */
```
```Go []
type MagicDictionary struct {
    Map map[int][]string
}


func Constructor() MagicDictionary {
    return MagicDictionary{map[int][]string{}}
}


func (this *MagicDictionary) BuildDict(dictionary []string)  {
    for _, d := range dictionary {
        this.Map[len(d)] = append(this.Map[len(d)], d)
    }
}


func (this *MagicDictionary) Search(searchWord string) bool {
    out:
    for _, d := range this.Map[len(searchWord)] {
        cnt := 0
        for i := 0; i < len(d); i++ {
            if searchWord[i] != d[i] {
                cnt++
            }
            if cnt > 1 {
                continue out
            }
        }
        if cnt == 1 {
            return true
        }
    }
    return false
}


/**
 * Your MagicDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.BuildDict(dictionary);
 * param_2 := obj.Search(searchWord);
 */
```