# [Python/Java/JavaScript/Go] 模拟

> Author: Benhao
> Date: 2022-02-17
> Upvotes: 7
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
每条边里都会有中心点，而其他点只出现一次。
从前两个找公共点即可

### 代码
```Python3
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()
```
```Python3 []
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return a if (a := edges[0][0]) == edges[1][0] or a == edges[1][1] else edges[0][1]
```
```Java []
class Solution {
    public int findCenter(int[][] edges) {
        return edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1] ? edges[0][0] : edges[0][1];
    }
}
```
```JavaScript []
/**
 * @param {number[][]} edges
 * @return {number}
 */
var findCenter = function(edges) {
    return edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1] ? edges[0][0] : edges[0][1]
};
```
```Go []
func findCenter(edges [][]int) int {
    if a := edges[0][0]; a == edges[1][0] || a == edges[1][1] {
        return a
    }
    return edges[0][1]
}
```