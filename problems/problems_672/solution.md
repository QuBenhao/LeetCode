# [Python/Java/TypeScript/Go] 穷举

> Author: Benhao
> Date: 2022-09-14
> Upvotes: 36
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
一共就四种操作，且每个操作只有一次和零次的区别 (同一个操作按两次等于没按)
1. 当灯泡个数为2时，操作4等同于操作3，故特殊讨论。
2. 当灯泡个数为1时，操作4等同于操作3，操作2等同于空操作，故特殊讨论。
3. 当灯泡个数足够多(大于2)时，每个操作各不相同，我们讨论操作次数来确认我们的选择。

### 代码

```python3
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        if n > 2:
            if presses == 1:
                return 4
            if presses == 2:
                return comb(4, 2) + 1 # 4个操作里选两个的选法，加上空操作
            if presses == 3:
                return comb(4, 3) + 4 # 4个操作里选三个的选法，加上两个操作出空+选一个操作
            if presses == 4:
                return comb(4, 2) + 2 # 4个操作里选两个的选法加上两个操作出空，加上选出空操作以及四个都选
            return comb(4, 2) + 2 # 奇数可以退化到3，偶数可以退化到4
        elif n == 2:
            if presses == 1:
                return 3 
            if presses == 2:
                return comb(3, 2) + 1
            if presses == 3:
                return comb(3, 1) + 1
            return 4 # 奇数可以退化到3，偶数可以退化到2
        return 2
```
以上代码可以简化为
```Python3 []
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        return 1 if not presses else (2 if n == 1 else ((4 if presses == 1 else (7 if presses == 2 else 8)) if n > 2 else (3 if presses == 1 else 4)))
```
```Java []
class Solution {
    public int flipLights(int n, int presses) {
        if (presses == 0) {
            return 1;
        }
        if (n == 1) {
            return 2;
        }
        if (n == 2) {
            return presses == 1 ? 3 : 4;
        }
        if (presses == 1) {
            return 4;
        }
        return presses == 2 ? 7 : 8;
    }
}
```
```TypeScript []
function flipLights(n: number, presses: number): number {
    if (presses == 0) {
        return 1
    }
    if (n == 1) {
        return 2
    }
    if (n == 2) {
        return presses == 1 ? 3 : 4
    }
    if (presses == 1) {
        return 4
    }
    return presses == 2 ? 7 : 8
};
```
```Go []
func flipLights(n int, presses int) int {
    if presses == 0 {
        return 1
    }
    if n == 1 {
        return 2
    }
    if n == 2 {
        if presses == 1 {
            return 3
        }
        return 4
    }
    if presses == 1 {
        return 4
    }
    if presses == 2 {
        return 7
    }
    return 8
}
```