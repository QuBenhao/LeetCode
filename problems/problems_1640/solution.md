# [Python/Java/TypeScript/Go] 模拟

> Author: Benhao
> Date: 2022-09-22
> Upvotes: 15
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
使用哈希表记录数字头，判断是否可以顺着走完

### 代码

```Python3 []
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {p[0]: i for i, p in enumerate(pieces)}
        idx = 0
        while idx < len(arr):
            if arr[idx] not in mp:
                return False
            for num in pieces[mp[arr[idx]]]:
                if num != arr[idx]:
                    return False
                idx += 1
        return True
```
```Java []
class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < pieces.length; i++) {
            map.put(pieces[i][0], i);
        }
        for (int idx = 0; idx < arr.length; ) {
            if (!map.containsKey(arr[idx])) {
                return false;
            }
            for (int num: pieces[map.get(arr[idx])]) {
                if (num != arr[idx++]) {
                    return false;
                }
            }
        }
        return true;
    }
}
```
```TypeScript []
function canFormArray(arr: number[], pieces: number[][]): boolean {
    const mp: Map<number, number> = new Map<number, number>()
    for (const [i, p] of pieces.entries()) {
        mp.set(p[0], i)
    }
    for (let idx = 0; idx < arr.length; ) {
        if (!mp.has(arr[idx])) {
            return false
        }
        for (const num of pieces[mp.get(arr[idx])]) {
            if (num != arr[idx++]) {
                return false
            }
        }
    }
    return true
};
```
```Go []
func canFormArray(arr []int, pieces [][]int) bool {
    mp := map[int]int{}
    for i, p := range pieces {
        mp[p[0]] = i
    }
    for idx := 0; idx < len(arr); {
        if v, ok := mp[arr[idx]]; !ok {
            return false
        } else {
            for _, num := range pieces[v] {
                if num != arr[idx] {
                    return false
                }
                idx++
            }
        }
    }
    return true
}
```