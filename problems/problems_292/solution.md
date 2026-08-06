# [Python/Java] 博弈论

> slug: pythonjava-bo-yi-lun-by-himymben-ybrs
> date: 2021-09-17
> tags: Java, Python, Python3
> question: Nim Game (nim-game)
> url: https://leetcode.cn/problems/nim-game/solutions/gK224m/pythonjava-bo-yi-lun-by-himymben-ybrs/

---
### 解题思路
由于一个人每次只能取1-3个石头，那么第二个人总能通过取第一个人取法跟4的补数(比如对方取1他就取3)，而达到稳定取到4以及后面4的倍数的目的。也就是说，如果有4的倍数的石子，那么后手永远能取到。

那么如果有不是4的倍数个石子呢？石子的个数模4必然余1-3。而先手的人，可以通过取这个余数而达到让自己成为上述的稳定取到4的倍数的石子的“后手”，也就是稳定的获胜。

> 题外话: 这和小时候玩过的经典的报数抢21游戏一样。每个人可以报连续的一到三个数，从1报到21，谁报到21谁就能赢。这时候你就会想，你先手想赢，你必须不能报18(你报18他就能报到21了)。你想不报18你必须也不能报14(你报14他就能报到17，你只能报18了)。依次类推，你不想报的数其实是2。那么很显然，你先手第一次只报个1，你就能赢。

### 代码

```Python3 []
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
```
```Java []
class Solution {
    public boolean canWinNim(int n) {
        return n % 4 != 0;
    }
}
```