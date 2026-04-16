# [Python/Java/JavaScript] 贪心

> Author: Benhao
> Date: 2021-10-31
> Upvotes: 18
> Tags: Java, JavaScript, Python, Python3

---

### 解题思路
首先最大的糖果种类数可以用集合的大小求出，然后根据平均分配，可能取不到最大种类数，取两者最小值。

### 代码

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