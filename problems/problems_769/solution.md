# [Python/Java/TypeScript/Go] 哈希

> slug: pythonjavatypescriptgo-ha-xi-by-himymben-gl19
> date: 2022-10-12
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Max Chunks To Make Sorted (max-chunks-to-make-sorted)
> url: https://leetcode.cn/problems/max-chunks-to-make-sorted/solutions/QwC7HI/pythonjavatypescriptgo-ha-xi-by-himymben-gl19/

---
### 解题思路
一个从0到n-1走的数组, 和输入数组, 只要任意时刻两者包含的数一致, 就是一组最小分块

### 代码

```Python3 []
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        s1, s2, ans = set(), set(), 0
        for i, num in enumerate(arr):
            s1.add(i)
            s2.add(num)
            if s1 == s2:
                ans += 1
                s1, s2 = set(), set()
        return ans
```
```Java []
class Solution {
    public int maxChunksToSorted(int[] arr) {
        int max = 0, ans = 0;
        for (int i = 0; i < arr.length; i++) {
            max = Math.max(arr[i], max);
            if (max == i) {
                ans++;
            }
        }
        return ans;
    }
}
```
```Typescript []
function maxChunksToSorted(arr: number[]): number {
    let ans: number = 0, max: number = 0
    for (const [i, num] of arr.entries()) {
        max = Math.max(num, max)
        if (max == i) {
            ans++
        }
    }
    return ans
};
```
```Go []
func maxChunksToSorted(arr []int) (ans int) {
    max := 0
    for i, num := range arr {
        if num > max {
            max = num
        }
        if max == i {
            ans++
        }
    }
    return
}
```