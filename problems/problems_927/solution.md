# [Python/Java/TypeScript/Go] 脑筋急转弯

> slug: pythonjavatypescriptgo-by-himymben-hnh7
> date: 2022-10-06
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Three Equal Parts (three-equal-parts)
> url: https://leetcode.cn/problems/three-equal-parts/solutions/T2a17L/pythonjavatypescriptgo-by-himymben-hnh7/

---
### 解题思路
我们将数组中的1三等分，按第三组1到末尾来确定整个二进制数的大小（不在乎前导零，但后面的零一定都算）。
我们判断三组1从第一个1开始是否构成同样的01分布即可。

### 代码

```Python3 []
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones = sum(arr)
        if ones % 3:
            return [-1, -1]
        if not ones:
            return [0, 2]
        each, a, b, c, cnts = ones // 3, -1, -1, -1, 0
        for idx, v in enumerate(arr):
            if v:
                cnts += 1
            if a == -1 and cnts:
                a = idx
            if b == -1 and cnts > each:
                b = idx
            if cnts > each * 2:
                c = idx
                break
        if (length := len(arr) - c) and arr[c:] == arr[a:a+length] == arr[b:b+length]:
            return [a + length - 1, b + length]
        return [-1, -1]
```
```Java []
class Solution {
    public int[] threeEqualParts(int[] arr) {
        int sum = 0;
        for (int num: arr) {
            sum += num;
        }
        if (sum % 3 != 0) {
            return new int[]{-1, -1};
        } else if (sum == 0) {
            return new int[]{0, 2};
        }
        int each = sum / 3, a = -1, b = -1, c = -1, n = arr.length, cnts = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == 1) {
                cnts++;
            }
            if (a == -1 && cnts > 0) {
                a = i;
            } else if (b == -1 && cnts > each) {
                b = i;
            } else if (cnts > each * 2) {
                c = i;
                break;
            }
        }
        for (int idx1 = a, idx2 = b, idx3 = c; idx3 < n; idx1++, idx2++, idx3++) {
            if (arr[idx1] != arr[idx3] || arr[idx2] != arr[idx3]) {
                return new int[]{-1, -1};
            }
        }
        return new int[]{a + n - c - 1, b + n - c};
    }
}
```
```TypeScript []
function threeEqualParts(arr: number[]): number[] {
    const sum: number = arr.reduce((a, b) => a + b)
    if (sum % 3 != 0) {
        return [-1, -1]
    } else if (sum == 0) {
        return [0, 2]
    }
    const each: number = Math.floor(sum / 3), n: number = arr.length
    let a: number = -1, b: number = -1, c: number = -1, cnts: number = 0
    for (let i = 0; i < n; i++) {
        cnts += arr[i]
        if (a == -1 && cnts > 0) {
            a = i
        } else if (b == -1 && cnts > each) {
            b = i
        } else if (cnts > each * 2) {
            c = i
            break
        }
    }
    for (let [idx1, idx2, idx3] = [a, b, c]; idx3 < n; idx1++, idx2++, idx3++) {
        if (arr[idx3] != arr[idx1] || arr[idx3] != arr[idx2]) {
            return [-1, -1]
        }
    }
    return [a + n - c - 1, b + n - c]
};
```
```Go []
func threeEqualParts(arr []int) []int {
    sum := 0
    for _, num := range arr {
        sum += num
    }
    if sum % 3 != 0 {
        return []int{-1, -1}
    } else if sum == 0 {
        return []int{0, 2}
    }
    each, cnts, a, b, c, n := sum / 3, 0, -1, -1, -1, len(arr)
    for i, num := range arr {
        cnts += num
        if a == -1 && cnts > 0 {
            a = i
        } else if b == -1 && cnts > each {
            b = i
        } else if cnts > each * 2 {
            c = i
            break
        }
    }
    for i1, i2, i3 := a, b, c; i3 < n; i3++ {
        if arr[i3] != arr[i1] || arr[i3] != arr[i2] {
            return []int{-1, -1}
        }
        i1++
        i2++
    }
    return []int{a + n - c - 1, b + n - c}
}
```