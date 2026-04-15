# [Python/Java/TypeScript/Go] 前K大模板

> Author: Benhao
> Date: 2022-08-25
> Upvotes: 14
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
一次遍历维护前k大、前k小也是老生常谈了，
这里给出一份模板代码。

### 代码

```Python3 []
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx, second_mx = 0, 0
        for num in nums:
            if num > mx:
                mx, second_mx = num, mx
            elif num > second_mx:
                second_mx = num
        return (mx - 1) * (second_mx - 1)
```
```Java []
class Solution {
    public int maxProduct(int[] nums) {
        int max = 0, secondMax = 0;
        for (int num: nums) {
            if (num > max) {
                secondMax = max;
                max = num;
            } else if (num > secondMax) {
                secondMax = num;
            }
        }
        return (max - 1) * (secondMax - 1);
    }
}
```
```TypeScript []
function maxProduct(nums: number[]): number {
    let max: number = 0, secondMax: number = 0
    for (const num of nums) {
        if (num > max) {
            secondMax = max
            max = num
        } else if (num > secondMax) {
            secondMax = num
        }
    }
    return (max - 1) * (secondMax - 1)
};
```
```Go []
func maxProduct(nums []int) int {
    max, second := 0, 0
    for _, num := range nums {
        if num > max {
            max, second = num, max
        } else if num > second {
            second = num
        }
    }
    return (max - 1) * (second - 1)
}
```
```Python3
# 前k小去掉这里面的所有负号
def find_k_max(arr: List[int], k: int) -> List[int]:
    ans = []
    for num in arr:
        idx = bisect_left(ans, -num)
        if idx < k:
            if idx == len(ans):
                ans.append(-num)
            else:
                ans = ans[:idx] + [-num] + ans[idx:]
                if len(ans) > k:
                    ans.pop()
    return [-num for num in ans]

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (ans[-1] - 1) * (ans[-2] - 1) if (ans := find_k_max(nums, 2)) else 0
```