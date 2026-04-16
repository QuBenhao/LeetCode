# [Python/Java/TypeScript/Go] 双指针滑窗

> Author: Benhao
> Date: 2022-10-17
> Upvotes: 21
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
本题要找最长的子数组，使得其中只有两个不同的元素。
我们遍历时维护两个不同元素的最左和最右的位置，当遇到第三个元素时做处理，剔除左边的那个元素即可。

### 代码

```Python3 []
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans, left_a, left_b, right_a, right_b = 0, -1, -1, -1, -1
        for i, val in enumerate(fruits):
            if left_a == -1:
                left_a = right_a = i
            elif fruits[left_a] == val:
                right_a = i
            elif left_b == -1:
                left_b = right_b = i
            elif fruits[left_b] == val:
                right_b = i
            else:
                # 遇到了第三个元素，统计答案并更新新的两个元素
                ans = max(ans, i - left_a)
                if right_a < right_b:
                    left_a, right_a, left_b, right_b = right_a + 1, right_b, i, i
                else:
                    left_a, right_a, left_b, right_b = right_b + 1, right_a, i, i
        # 处理一些只有一个元素、最大值在最后等特殊情况
        return max(ans, len(fruits) - left_a)
```
```Java []
class Solution {
    public int totalFruit(int[] fruits) {
        int ans = 0, leftA = -1, leftB = -1, rightA = -1, rightB = -1;
        for (int i = 0; i < fruits.length; i++) {
            if (leftA == -1) {
                leftA = rightA = i;
            } else if (fruits[i] == fruits[leftA]) {
                rightA = i;
            } else if (leftB == -1) {
                leftB = rightB = i;
            } else if (fruits[i] == fruits[leftB]) {
                rightB = i;
            } else {
                ans = Math.max(ans, i - leftA);
                if (rightA < rightB) {
                    leftA = rightA + 1;
                    rightA = rightB;
                } else {
                    leftA = rightB + 1;
                }
                leftB = rightB = i;
            }
        }
        return Math.max(ans, fruits.length - leftA);
    }
}
```
```TypeScript []
function totalFruit(fruits: number[]): number {
    let ans: number = 0, leftA: number = -1, leftB: number = -1, rightA: number = -1, rightB: number = -1
    for (let i = 0; i < fruits.length; i++) {
        if (leftA == -1) {
            leftA = rightA = i
        } else if (fruits[i] == fruits[leftA]) {
            rightA = i
        } else if (leftB == -1) {
            leftB = rightB = i
        } else if (fruits[i] == fruits[leftB]) {
            rightB = i
        } else {
            ans = Math.max(ans, i - leftA)
            if (rightA < rightB) {
                leftA = rightA + 1
                rightA = rightB
            } else {
                leftA = rightB + 1
            }
            leftB = rightB = i
        }
    }
    return Math.max(ans, fruits.length - leftA)
};
```
```Go []
func totalFruit(fruits []int) (ans int) {
    leftA, leftB, rightA, rightB := -1, -1, -1, -1
    for i, val := range fruits {
        if leftA == -1 {
            leftA = i
            rightA = i
        } else if val == fruits[leftA] {
            rightA = i
        } else if leftB == -1 {
            leftB = i
            rightB = i
        } else if val == fruits[leftB] {
            rightB = i
        } else {
            ans = max(ans, i - leftA)
            if rightA < rightB {
                leftA, rightA = rightA + 1, rightB
            } else {
                leftA = rightB + 1
            }
            leftB = i
            rightB = i
        }
    } 
    return max(ans, len(fruits) - leftA)
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```