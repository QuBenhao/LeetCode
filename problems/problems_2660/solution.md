# [Python/C/Java/Go/TypeScript] 简洁循环比较

> slug: pythoncjavago-jian-ji-xun-huan-bi-jiao-b-92uo
> date: 2023-12-26
> tags: C, Go, Java, Python3, TypeScript
> question: Determine the Winner of a Bowling Game (determine-the-winner-of-a-bowling-game)
> url: https://leetcode.cn/problems/determine-the-winner-of-a-bowling-game/solutions/jY0hC4/pythoncjavago-jian-ji-xun-huan-bi-jiao-b-92uo/

---
> Problem: [https://leetcode.cn/problems/determine-the-winner-of-a-bowling-game/description/](https://leetcode.cn/problems/determine-the-winner-of-a-bowling-game/description/ "https://leetcode.cn/problems/determine-the-winner-of-a-bowling-game/description/")

\[TOC]

# 思路

> 循环遍历时记录10的出现

# 解题方法

> 因为是比较两个和的大小，故在循环中一加一减即可

# 复杂度

时间复杂度:

> $O(n)$

空间复杂度:

> $O(1)$

# Code

```Python3 []
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        s, last_x1, last_last_x1, last_x2, last_last_x2 = 0, 0, 0, 0, 0
        for i, (x1, x2) in enumerate(zip(player1, player2)):
            if last_x1 == 10 or last_last_x1 == 10:
                s += 2 * x1
            else:
                s += x1
            if last_x2 == 10 or last_last_x2 == 10:
                s -= 2 * x2
            else:
                s -= x2
            last_x1, last_last_x1, last_x2, last_last_x2 = x1, last_x1, x2, last_x2
        return 0 if not s else 1 if s > 0 else 2
```
```C []
int isWinner(int* player1, int player1Size, int* player2, int player2Size){
    int s = 0, last_x1 = 0, last_last_x1 = 0, last_x2 = 0, last_last_x2 = 0;
    for (int i = 0; i < player1Size; i++) {
        if (last_x1 == 10 || last_last_x1 == 10) {
            s += 2 * player1[i];
        } else {
            s += player1[i];
        }
        if (last_x2 == 10 || last_last_x2 == 10) {
            s -= 2 * player2[i];
        } else {
            s -= player2[i];
        }
        last_last_x1 = last_x1, last_last_x2 = last_x2;
        last_x1 = player1[i], last_x2 = player2[i];
    }
    return s == 0 ? 0 : (s > 0 ? 1 : 2);
}
```
```Java []
class Solution {
    public int isWinner(int[] player1, int[] player2) {
        int s = 0, lastX1 = 0, lastLastX1 = 0, lastX2 = 0, lastLastX2 = 0;
        for (int i = 0; i < player1.length; i++) {
            if (lastX1 == 10 || lastLastX1 == 10) {
                s += player1[i] * 2;
            } else {
                s += player1[i];
            }
            if (lastX2 == 10 || lastLastX2 == 10) {
                s -= player2[i] * 2;
            } else {
                s -= player2[i];
            }
            lastLastX1 = lastX1; lastLastX2 = lastX2; lastX1 = player1[i]; lastX2 = player2[i];
        }
        return s == 0 ? 0 : (s > 0 ? 1 : 2);
    }
}
```
```Go []
func isWinner(player1 []int, player2 []int) int {
    s, last_x1, last_last_x1, last_x2, last_last_x2 := 0, 0, 0, 0, 0
    for i, x1 := range player1 {
        if last_x1 == 10 || last_last_x1 == 10 {
            s += 2 * x1
        } else {
            s += x1
        }
        if last_x2 == 10 || last_last_x2 == 10 {
            s -= 2 * player2[i]
        } else {
            s -= player2[i]
        }
        last_last_x1, last_x1, last_last_x2, last_x2  = last_x1, x1, last_x2, player2[i]
    }
    if s == 0 {
        return 0
    } else if s > 0 {
        return 1
    }
    return 2
}
```
```TypeScript []
function isWinner(player1: number[], player2: number[]): number {
    let s: number = 0, lastX1: number = 0, lastLastX1: number = 0, lastX2: number = 0, lastLastX2: number = 0
    for(let i = 0; i < player1.length; i++) {
        if (lastX1 == 10 || lastLastX1 == 10) {
            s += player1[i] * 2
        } else {
            s += player1[i]
        }
        if (lastX2 == 10 || lastLastX2 == 10) {
            s -= player2[i] * 2
        } else {
            s -= player2[i]
        }
        lastLastX1 = lastX1, lastLastX2 = lastX2, lastX1 = player1[i], lastX2 = player2[i]
    } 
    return s == 0 ? 0 : (s > 0 ? 1 : 2)
};
```

通用写法

```Python3 []
LAST = 2
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        s = 0
        for i, (x1, x2) in enumerate(zip(player1, player2)):
            if 10 in player1[max(0, i - LAST) : i]:
                s += 2 * x1
            else:
                s += x1
            if 10 in player2[max(0, i - LAST) : i]:
                s -= 2 * x2
            else:
                s -= x2
        return 0 if not s else 1 if s > 0 else 2
```
