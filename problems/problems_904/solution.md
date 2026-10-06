# [Python/Java/TypeScript/Go] Two-pointer sliding window

> Author: Benhao
> Date: 2022-10-17
> Upvotes: 21
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
Find the longest subarray containing only two distinct elements.
Track the leftmost and rightmost positions of the two distinct elements while scanning. When a third appears, remove the element on the left.

### Code

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
                # A third distinct element appears; update the answer and the new pair of elements
                ans = max(ans, i - left_a)
                if right_a < right_b:
                    left_a, right_a, left_b, right_b = right_a + 1, right_b, i, i
                else:
                    left_a, right_a, left_b, right_b = right_b + 1, right_a, i, i
        # Handle cases such as only one distinct element or the longest window ending at the array's end
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
