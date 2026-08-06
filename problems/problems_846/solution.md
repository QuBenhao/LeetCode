# [Python/Java/JavaScript/Go] 贪心

> slug: pythonjavajavascriptgo-tan-xin-by-himymb-oi3i
> date: 2021-12-29
> tags: Go, Java, JavaScript, Python, Python3
> question: Hand of Straights (hand-of-straights)
> url: https://leetcode.cn/problems/hand-of-straights/solutions/saNSPi/pythonjavajavascriptgo-tan-xin-by-himymb-oi3i/

---
### 解题思路
每个顺子一定有最小和最大的一张牌，每次一幅牌里也一定有最小的一张，这张牌必须有顺子是满足所有牌都在顺子里的充要条件。把它的顺子去掉以后，又会有一张新的最小的牌，如此反复，直到没有牌。

家人们，已经两天了，要么看不到你们的评论，要么回复了感觉你们看不到😭绝了


### 代码

```Python3 []
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        cnts = Counter(hand)
        for start in sorted(cnts.keys()):
            while cnts[start]:
                for end in range(start, start + groupSize):
                    if not cnts[end]:
                        return False
                    cnts[end] -= 1
        return True
```
```Java []
class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        if(hand.length % groupSize != 0)
            return false;
        Map<Integer, Integer> cnts = new HashMap<>();
        for(int h: hand)
            cnts.put(h, cnts.getOrDefault(h, 0) + 1);      
        Arrays.sort(hand);
        for(int h: hand)
            if(cnts.get(h) > 0)
                for(int i=h;i<h+groupSize;i++){
                    if(!cnts.containsKey(i) || cnts.get(i) == 0)
                        return false;
                    cnts.put(i, cnts.get(i) - 1);
                }
        return true;
    }
}
```
```JavaScript []
/**
 * @param {number[]} hand
 * @param {number} groupSize
 * @return {boolean}
 */
var isNStraightHand = function(hand, groupSize) {
    if(hand.length % groupSize > 0)
        return false
    const cnts = new Map()
    for(const h of hand)
        if(cnts.has(h))
            cnts.set(h, cnts.get(h) + 1)
        else
            cnts.set(h, 1)
    const keys = Array.from(cnts.keys())
    keys.sort((a,b)=>a-b)
    for(const l of keys)
        while(cnts.get(l) > 0)
            for(let i=0;i<groupSize;i++){
                if(!cnts.has(l + i) || cnts.get(l + i) == 0)
                    return false
                cnts.set(l + i, cnts.get(l + i) - 1)
            }
    return true
};
```
```Go []
func isNStraightHand(hand []int, groupSize int) bool {
    if len(hand) % groupSize > 0{
        return false
    }
    cnts := map[int]int{}
    for _, h := range hand {
        cnts[h]++
    }
    sort.Ints(hand)
    for _, h := range hand {
        for cnts[h] > 0 {
            for i := h; i < h + groupSize; i++ {
                if cnts[i] == 0 {
                    return false
                }
                cnts[i]--
            }
        }
    }
    return true
}
```

[@meteordream](/u/meteordream/) 以上方法的一点小优化是直接减去最小牌的次数，可以减少循环
```python3
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        cnts = Counter(hand)
        for start in sorted(cnts.keys()):
            if cnts[start]:
                c = cnts[start]
                for end in range(start, start + groupSize):
                    if cnts[end] < c:
                        return False
                    cnts[end] -= c
        return True
```