# [Python/JavaTypeScript/Go] Simulate a stack with two pointers

> slug: pythonjavatypescriptgo-by-himymben-1vsd
> date: 2022-06-16
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Duplicate Zeros (duplicate-zeros)
> url: https://leetcode.cn/problems/duplicate-zeros/solutions/GQaxcc/pythonjavatypescriptgo-by-himymben-1vsd/

---
### Approach
Traverse the array to count zeros and locate the final source position.
Imagine pushing each zero onto a stack twice. Stop once the stack is as long as the array, then pop elements from its top in order.

One pointer tracks the source position (the stack top); the other tracks the write position in the original array.

### Code

```Python3 []
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros, n, left, last_mark = 0, len(arr), -1, False
        for i, num in enumerate(arr):
            if not num:
                zeros += 1
            if i + 1 + zeros >= n:
                last_mark = i + 1 + zeros > n
                left = i
                break
        right = n - 1 if not last_mark else n - 2
        if last_mark:
            left -= 1
            arr[-1] = 0
        while left >= 0:
            arr[right] = arr[left]
            if not arr[left]:
                arr[right - 1] = 0
                right -= 1
            left -= 1
            right -= 1
```
```Java []
class Solution {
    public void duplicateZeros(int[] arr) {
        int zeros = 0, n = arr.length, data = -1;
        boolean mark = false;
        for(int i = 0; i < n; i++) {
            if (arr[i] == 0) {
                zeros++;
            }
            if (zeros + i + 1 >= n) {
                mark = zeros + i + 1 > n;
                data = i;
                break;
            }
        }
        int write = mark ? n - 2 : n - 1;
        if (mark) {
            arr[n - 1] = 0;
            data--;
        }
        while(data >= 0) {
            arr[write] = arr[data];
            if (arr[data] == 0) {
                arr[--write] = 0;
            }
            data--;
            write--;
        }
    }
}
```
```TypeScript []
/**
 Do not return anything, modify arr in-place instead.
 */
function duplicateZeros(arr: number[]): void {
    const n = arr.length
    let zeros = 0, data = -1, mark = false
    for (let i = 0; i < n; i++) {
        if (arr[i] == 0) {
            zeros++
        }
        if (i + 1 + zeros >= n) {
            mark = i + 1 + zeros > n
            data = i
            break
        }
    }
    let write = mark ? n - 2 : n - 1
    if (mark) {
        arr[n - 1] = 0
        data--
    }
    while (data >= 0) {
        arr[write] = arr[data]
        if (arr[data] == 0) {
            arr[--write] = 0
        }
        data--
        write--
    } 
};
```
```Go []
func duplicateZeros(arr []int)  {
    zeros, n, data, mark := 0, len(arr), -1, false
    for i, num := range arr {
        if num == 0 {
            zeros++
        }
        if i + 1 + zeros >= n {
            mark = i + 1 + zeros > n
            data = i
            break
        }
    }
    write := n - 1
    if mark {
        arr[write] = 0
        data--
        write--
    }
    for data >= 0 {
        arr[write] = arr[data]
        if arr[data] == 0 {
            write--
            arr[write] = 0
        }
        write--
        data--
    }
}
```
