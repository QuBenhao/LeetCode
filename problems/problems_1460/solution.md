# [Python/Java/TypeScript/Go] Brain teaser

> slug: pythonjavatypescriptgo-mo-ni-by-himymben-yc9h
> date: 2022-08-24
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Make Two Arrays Equal by Reversing Subarrays (make-two-arrays-equal-by-reversing-subarrays)
> url: https://leetcode.cn/problems/make-two-arrays-equal-by-reversing-subarrays/solutions/8nlLy2/pythonjavatypescriptgo-mo-ni-by-himymben-yc9h/

---
### Approach
Reverse [i:j], then [i:j+1], to move j to position i while shifting the other positions.
This can move any number to any position.

### Code

```Python3 []
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)
```
```Java []
class Solution {
    public boolean canBeEqual(int[] target, int[] arr) {
        int[] counts = new int[1005];
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if (++counts[target[i]] == 1) {
                count++;
            }
            if (--counts[arr[i]] == 0) {
                count--;
            }
        }
        return count == 0;
    }
}
```
```TypeScript []
function canBeEqual(target: number[], arr: number[]): boolean {
    const counts: Array<number> = new Array<number>(1005).fill(0)
    let count: number = 0
    for (let i = 0; i < arr.length; i++) {
        if (++counts[target[i]] == 1) {
            count++
        }
        if (--counts[arr[i]] == 0) {
            count--
        }
    }
    return count == 0
};
```
```Go []
func canBeEqual(target []int, arr []int) bool {
    counts, count := make([]int, 1005), 0
    for i, num := range arr {
        counts[target[i]]++
        if counts[target[i]] == 1 {
            count++
        }
        counts[num]--
        if counts[num] == 0 {
            count--
        }
    }
    return count == 0
}
```
