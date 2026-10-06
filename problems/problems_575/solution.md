# [Python/Java/JavaScript] Greedy

> Author: Benhao
> Date: 2021-10-31
> Upvotes: 18
> Tags: Java, JavaScript, Python, Python3

---

### Approach
The number of distinct candy types is the size of the set. An equal split may prevent taking every type, so take the smaller of the number of types and the number of candies allowed.

### Code

```Python3 []
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType)//2)
```
```Java []
class Solution {
    public int distributeCandies(int[] candyType) {
        Set<Integer> kinds = new HashSet<>();
        for(int type:candyType)
            kinds.add(type);
        return Math.min(candyType.length/2, kinds.size());
    }
}
```
```JavaScript []
/**
 * @param {number[]} candyType
 * @return {number}
 */
var distributeCandies = function(candyType) {
    const kinds = new Set();
    for(const type of candyType)
        kinds.add(type);
    return Math.min(Math.floor(candyType.length/2),kinds.size);
};
```
