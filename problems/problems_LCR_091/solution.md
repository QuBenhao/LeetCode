# [Python/Java/TypeScript/Go] 动态规划

> slug: pythonjavatypescriptgo-dong-tai-gui-hua-77g3a
> date: 2022-06-25
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: 粉刷房子 (JEj789)
> url: https://leetcode.cn/problems/JEj789/solutions/Vr6qrV/pythonjavatypescriptgo-dong-tai-gui-hua-77g3a/

---
### 解题思路
当前最小花费由当前刷红、刷蓝、刷绿中最小的花费决定。
当前刷红，上一个只能是蓝或绿，所以由上一次蓝绿最小值加上当前红的代价得到。
以此类推。

### 代码

```Python3 []
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        red, blue, green = 0, 0, 0
        for r, b, g in costs:
            red, blue, green = min(blue, green) + r, min(red, green) + b, min(red, blue) + g
        return min(red, blue, green)
```
```Java []
class Solution {
    public int minCost(int[][] costs) {
        int red = 0, blue = 0, green = 0;
        for (int[] cost: costs) {
            int r = Math.min(blue, green) + cost[0], b = Math.min(red, green) + cost[1], g = Math.min(red, blue) + cost[2];
            red = r;
            blue = b;
            green = g;
        }
        return Math.min(red, Math.min(blue, green));
    }
}
```
```TypeScript []
function minCost(costs: number[][]): number {
    let red = 0, blue = 0, green = 0
    for (const [r, b, g] of costs) {
        [red, blue, green] = [Math.min(blue, green) + r, Math.min(red, green) + b, Math.min(red, blue) + g]
    }
    return Math.min(red, blue, green)
};
```
```Go []
func minCost(costs [][]int) int {
    red, blue, green := 0, 0, 0
    for _, cost := range costs {
        red, blue, green = min(blue, green) + cost[0], min(red, green) + cost[1], min(red, blue) + cost[2]
    }
    return min(red, blue, green)
}

func min(values ...int) int {
    res := values[0]
    for _, v := range values {
        if v < res {
            res = v
        }
    }
    return res
}
```