# [Python/Java/TypeScript/Go] 数学

> Author: Benhao
> Date: 2022-09-06
> Upvotes: 23
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
设字符c位于[left, right]中的idx且c唯一, 那么c出现的次数为它左边包含它的个数乘它右边包含它的个数 [即(idx + 1 - left) * (right + 1 - left)]。
所以我们只需要统计每个字符出现的所有间隔坐标即可。

### 代码

```Python3 []
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        ans = 0
        for v in d.values():
            cur = [-1] + v + [len(s)]
            for i in range(1, len(cur) - 1):
                ans += (cur[i] - cur[i - 1]) * (cur[i + 1] - cur[i])
        return ans
```
```Java []
class Solution {
    public int uniqueLetterString(String s) {
        Map<Character, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            List<Integer> list = map.getOrDefault(c, new ArrayList<>(){{add(-1);}});
            list.add(i);
            map.put(c, list);
        }
        int ans = 0;
        for (List<Integer> list: map.values()) {
            list.add(s.length());
            for (int i = 1; i < list.size() - 1; i++) {
                ans += (list.get(i) - list.get(i - 1)) * (list.get(i + 1) - list.get(i));
            }   
        }
        return ans;
    }
}
```
```TypeScript []
function uniqueLetterString(s: string): number {
    const dict: Map<string, Array<number>> = new Map<string, Array<number>>()
    for (let i = 0; i < s.length; i++) {
        const key: string = s.substr(i, 1)
        if (dict.has(key)) {
            dict.get(key).push(i)
        } else {
            dict.set(key, [-1, i])
        }
    }
    let ans: number = 0
    dict.forEach((value: number[]) => {
        value.push(s.length)
        for (let i = 1; i < value.length - 1; i++) {
            ans += (value[i] - value[i - 1]) * (value[i + 1] - value[i])
        }
    })
    return ans
};
```
```Go []
func uniqueLetterString(s string) (ans int) {
    dict := map[rune][]int{}
    for i, c := range s {
        if v, ok := dict[c]; ok {
            dict[c] = append(v, i)
        } else {
            dict[c] = []int{-1, i}
        }
    }
    for _, v := range dict {
        v = append(v, len(s))
        for i := 1; i < len(v) - 1; i++ {
            ans += (v[i] - v[i - 1]) * (v[i + 1] - v[i])
        }
    }
    return
}
```