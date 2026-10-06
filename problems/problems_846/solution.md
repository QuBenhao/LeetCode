# [Python/Java/JavaScript/Go] Greedy

> slug: pythonjavajavascriptgo-tan-xin-by-himymb-oi3i
> date: 2021-12-29
> tags: Go, Java, JavaScript, Python, Python3
> question: Hand of Straights (hand-of-straights)
> url: https://leetcode.cn/problems/hand-of-straights/solutions/saNSPi/pythonjavajavascriptgo-tan-xin-by-himymb-oi3i/

---
### Approach
Every straight has a smallest and largest card, and the remaining hand always has a smallest card. That card must belong to a straight for all cards to be grouped into straights. Remove its straight, then repeat with the new smallest card until none remain.

Folks, it has been two days: either I cannot see your comments, or I reply and it seems you cannot see mine 😭 Unbelievable


### Code

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

[@meteordream](/u/meteordream/) A small optimization is to subtract the smallest card's count directly, reducing the number of iterations
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
