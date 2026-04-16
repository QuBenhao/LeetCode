# [Python/Java/TypeScript/Go] 二分 + 双指针

> Author: Benhao
> Date: 2022-08-25
> Upvotes: 21
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
arr本身有序，很容易想到用二分找x在arr中的位置，然后往左右根据谁更近扩充出k个即可。

### 代码

```Python3 []
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = bisect_left(arr, x)
        left = right - 1
        while k:
            if left < 0:
                right += 1
            elif right == len(arr):
                left -= 1
            else:
                if x - arr[left] <= arr[right] - x:
                    left -= 1
                else:
                    right += 1
            k -= 1
        return arr[left + 1:right]
```
```Java []
class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int mid = left + right >> 1;
            if (arr[mid] < x) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        left--;
        while (k-- > 0) {
            if (left < 0) {
                right++;
            } else if (right == arr.length) {
                left--;
            } else {
                if (x - arr[left] <= arr[right] - x) {
                    left--;
                } else {
                    right++;
                }
            }
        }
        List<Integer> ans = new ArrayList<>();
        for (int i = left + 1; i < right; i++) {
            ans.add(arr[i]);
        }
        return ans;
    }
}
```
```TypeScript []
function findClosestElements(arr: number[], k: number, x: number): number[] {
    let left: number = 0, right: number = arr.length - 1
    while (left < right) {
        const mid: number = (left + right) >> 1
        if (arr[mid] < x) {
            left = mid + 1
        } else {
            right = mid
        }
    }
    left--
    while (k-- > 0) {
        if (left < 0) {
            right++
        } else if (right == arr.length) {
            left--
        } else {
            if (x - arr[left] <= arr[right] - x) {
                left--
            } else {
                right++
            }
        }
    }
    return arr.slice(left + 1, right)
};
```
```Go []
func findClosestElements(arr []int, k int, x int) []int {
    left, right := 0, len(arr) - 1
    for left < right {
        mid := (left + right) >> 1
        if arr[mid] < x {
            left = mid + 1
        } else {
            right = mid
        }
    }
    left--
    for i := 0; i < k; i++ {
        if left < 0 {
            right++
        } else if right == len(arr) {
            left--
        } else {
            if x - arr[left] <= arr[right] - x {
                left--
            } else {
                right++
            }
        }
    }
    return arr[left + 1: right]
}
```