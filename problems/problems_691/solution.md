# [Python/Java/JavaScript/Go] BFS

> Author: Benhao
> Date: 2022-05-14
> Upvotes: 56
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
Start from target [initial state]. Each sticker removes its matching character counts [state transition]. Check whether the empty string can eventually be reached [goal state].
Optimization: remove the current state's characters from left to right to reduce equivalent selection orders.
For example, applying stickers[0] once and stickers[1] once gives the same result in either order. Removing a then b is equivalent to removing b then a; we care about selecting ab, not their permutation.


### Code

```Python3 []
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def trans(s):
            cnts = Counter()
            for c in s:
                if c in target:
                    cnts[c] += 1
            return cnts

        availables = [c for st in stickers if (c:=trans(st))]
        queue = deque([(target, 0)])
        explored = {target}
        while queue:
            cur, step = queue.popleft()
            if not cur:
                return step
            for avl in availables:
                if cur[0] in avl:
                    nxt = cur
                    for k, v in avl.items():
                        nxt = nxt.replace(k, '', v)
                    if nxt not in explored:
                        explored.add(nxt)
                        queue.append((nxt, step + 1))
        return -1
```
```Java []
class Solution {
    public int minStickers(String[] stickers, String target) {
        Set<Character> targetSet = new HashSet<Character>();
        for(int i = 0; i < target.length(); i++)
            targetSet.add(target.charAt(i));
        List<Map<Character, Integer>> availables = new ArrayList<>();
        for(String s: stickers) {
            Map<Character, Integer> map = getCounter(s, targetSet);
            if(map != null) {
                availables.add(map);
            }
        }
        Deque<String> queue = new ArrayDeque<>();
        queue.addLast(target);
        Map<String, Integer> cost = new HashMap<>();
        cost.put(target, 0);
        while(!queue.isEmpty()) {
            String cur = queue.pollFirst(); 
            for(Map<Character, Integer> map: availables) {
                if(map.containsKey(cur.charAt(0))) {
                    String nxt = nextState(cur, new HashMap<>(map));
                    if(nxt.length() == 0) {
                        return cost.get(cur) + 1;
                    } else if(!cost.containsKey(nxt)) {
                        cost.put(nxt, cost.get(cur) + 1);
                        queue.addLast(nxt);
                    }
                }
            }
        }
        return -1;
    }

    private Map<Character, Integer> getCounter(String s, Set<Character> chars) {
        Map<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(chars.contains(c)) {
                map.put(c, map.getOrDefault(c, 0) + 1);
            }
        }
        return map.size() > 0 ? map : null;
    }

    private String nextState(String s, Map<Character, Integer> map) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(map.getOrDefault(c, 0) > 0) {
                map.put(c, map.get(c) - 1);
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
```
```JavaScript []
/**
 * @param {string[]} stickers
 * @param {string} target
 * @return {number}
 */
var minStickers = function(stickers, target) {
    const set = new Set(target), availables = new Array(), queue = new Queue(), explored = new Set()
    const getCounter = (s) => {
        const map = new Map()
        for(const c of s) {
            if(set.has(c)) {
                if(map.has(c)) {
                    map.set(c, map.get(c) + 1)
                } else {
                    map.set(c, 1)
                }
            }
        }
        return map.size > 0 ? map : null
    }, transfer = (s, map) => {
        const copy = new Map(map), res = []
        for(const c of s) {
            if(copy.has(c) && copy.get(c) > 0) {
                copy.set(c, copy.get(c) - 1)
            } else {
                res.push(c)
            }
        }
        return res.join("")
    }
    for(const s of stickers) {
        const mp = getCounter(s)
        if(mp != null) {
            availables.push(mp)
        }
    }
    queue.enqueue([target, 0])
    explored.add(target)
    while(!queue.isEmpty()) {
        const [cur, step] = queue.dequeue()
        if(cur.length == 0) {
            return step
        }
        for(const mp of availables) {
            if(mp.has(cur.charAt(0))) {
                const nxt = transfer(cur, mp)
                if(!explored.has(nxt)) {
                    explored.add(nxt)
                    queue.enqueue([nxt, step + 1])
                }
            }
        }
    }
    return -1
};
```
```Go []
func minStickers(stickers []string, target string) int {
    targetSet := map[rune]bool{}
    for _, r := range target {
        targetSet[r] = true
    }
    availables := []map[rune]int{}
    for _, s := range stickers {
        if c := getCounter(s, targetSet); c != nil {
            availables = append(availables, c)
        }
    }
    queue, explored := []string{target}, map[string]int{target:0}
    for len(queue) > 0 {
        cur := queue[0]
        queue = queue[1:]
        for _, avl := range availables {
            if avl[rune(cur[0])] > 0 {
                nxt := transfer(cur, avl)
                if len(nxt) == 0 {
                    return explored[cur] + 1
                }
                if _, ok := explored[nxt]; !ok {
                    queue = append(queue, nxt)
                    explored[nxt] = explored[cur] + 1
                }
            }
        }
    }
    return -1
}

func getCounter(s string, chars map[rune]bool) map[rune]int {
    res := map[rune]int{}
    for _, r := range s {
        if chars[r] {
            res[r]++
        }
    }
    if len(res) == 0 {
        return nil
    }
    return res
}

func transfer(s string, mp map[rune]int) string {
    for k, v := range mp {
        s = strings.Replace(s, string(k), "", v)
    }
    return s
}
```
