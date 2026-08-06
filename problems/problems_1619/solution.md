# [Python/Java/TypeScript/Go] 排序模拟

> slug: pythonjavatypescriptgo-pai-xu-mo-ni-by-h-szvi
> date: 2022-09-13
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Mean of Array After Removing Some Elements (mean-of-array-after-removing-some-elements)
> url: https://leetcode.cn/problems/mean-of-array-after-removing-some-elements/solutions/e73ANg/pythonjavatypescriptgo-pai-xu-mo-ni-by-h-szvi/

---
### 解题思路
排序后求中间90%个数的平均值

### 代码

```Python3 []
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        return sum(sorted(arr)[n:-n]) / (n * 18) if (n := len(arr)//20) else 0.0
```
```Java []
class Solution {
    public double trimMean(int[] arr) {
        Arrays.sort(arr);
        int ans = 0, n = arr.length / 20;
        for (int i = n; i < n * 19; i++) {
            ans += arr[i];
        }
        return (0.0 + ans) / (n * 18);
    }
}
```
```TypeScript []
function trimMean(arr: number[]): number {
    return arr.sort((a, b) => a - b).slice(Math.floor(arr.length / 20), arr.length - Math.floor(arr.length / 20)).reduce((a, b) => a + b) * 10 / (arr.length * 9)
};
```
```Go []
func trimMean(arr []int) float64 {
    sort.Ints(arr)
    ans, n := 0, len(arr) / 20
    for i := n; i < n * 19; i++ {
        ans += arr[i]
    }
    return float64(ans) / float64(n * 18)
}
```