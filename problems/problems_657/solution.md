# [Python/Go/Java/Cpp] 模拟统计

> Author: Benhao
> Date: 2024-06-02
> Upvotes: 1
> Tags: C++, Go, Java, Python3

---


> Problem: [657. 机器人能否返回原点](https://leetcode.cn/problems/robot-return-to-origin/description/)

[TOC]

# 思路

> 校验LR的数量一样，UD的数量一样

# 解题方法

> 一正一负即可

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizontal, vertical = 0, 0
        for c in moves:
            match c:
                case 'U':
                    vertical += 1
                case 'D':
                    vertical -= 1
                case 'L':
                    horizontal -= 1
                case _:
                    horizontal += 1
        return horizontal == 0 and vertical == 0
```
```Golang []
func judgeCircle(moves string) bool {
	horizontal, vertical := 0, 0
	for _, c := range moves {
		switch c {
		case 'U':
			vertical++
		case 'D':
			vertical--
		case 'L':
			horizontal--
		case 'R':
			horizontal++
		}
	}
	return horizontal == 0 && vertical == 0
}
```
```Java []
class Solution {
    public boolean judgeCircle(String moves) {
        int horizontal = 0, vertical = 0;
        for (int i = 0; i < moves.length(); i++) {
            switch (moves.charAt(i)) {
                case 'L':
                    horizontal--;
                    break;
                case 'U':
                    vertical++;
                    break;
                case 'D':
                    vertical--;
                    break;
                default:
                    horizontal++;
            }
        }
        return horizontal == 0 && vertical == 0;
    }
}
```
```Cpp []
class Solution {
public:
    bool judgeCircle(string moves) {
        int horizontal = 0, vertical = 0;
        for (auto &c: moves) {
            switch (c) {
                case 'L':
                    horizontal--;
                    break;
                case 'R':
                    horizontal++;
                    break;
                case 'U':
                    vertical++;
                    break;
                default:
                    vertical--;
            }
        }
        return horizontal == 0 && vertical == 0;
    }
};
```
