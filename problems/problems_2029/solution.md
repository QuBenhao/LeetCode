# [Python/Java/JavaScript/Go/C] 博弈 - Alice获胜的策略分析

> slug: pythonjavajavascriptgoc-bo-yi-fen-xi-by-2024o
> date: 2022-01-19
> tags: C, Go, Java, JavaScript, Python, Python3
> question: Stone Game IX (stone-game-ix)
> url: https://leetcode.cn/problems/stone-game-ix/solutions/YdJcFD/pythonjavajavascriptgoc-bo-yi-fen-xi-by-2024o/

---
### 解题思路
分析题目：
> 1. 石子按模3区分，原来的大小在同一个余数堆里没有区别
> 2. 模3余0的石子成对出现等于没出现，因为对方被迫选了模3余0，我们再选模3余0还会让他面对刚刚的局面
> 3. 先手拿1，整体的选择只能为 1 1 2 1 2 1 2 ...
> 4. 先手拿2，整体的选择只能为 2 2 1 2 1 2 1 ...
> 5. 如果没有模3余0的石子（成对出现了），Alice先手取更少的那边的石子是必胜态，会逼对方必须从更少的石子中拿石子，他会先拿光
> 6. 如果没有模3余0的石子（成对出现了），且有一堆余1或余2的石子没有，那么Alice要么在第三回合输，要么拿光也没有出现模3余0，Bob必胜
> 7. 如果有模3余0的石子（奇数个），由于出现了一个反制的选择，如果拿更少的石子，对方拿模3余0的石子会导致自己永远要选更少的石子而先输掉游戏，
>    所以必须拿更多的那一边，只多一个或两个还不行，因为那样Bob总有拿光也没有出现模3余0的策略，Bob必胜。
>    只有当有一堆石子更多且多至少3个时候，Alice才有逼对方在这堆石子取到模3余0的策略（先拿更多的那边，后面对方拿0我们取这堆，对方拿这堆里的我们取0）

总结：
偶数个整除3的石子下，Alice的策略为拿1或2更少的那边，如果1或2里有一堆没有，Alice无法获胜。
奇数个整除3的石子下，Alice的策略为拿1或2更多的那边，如果更多的那边不比另一堆多至少3个，Alice无法获胜。

### 代码

```Python3 []
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # 1 1 2 1 2 1 2 1 2 ...
        # 2 2 1 2 1 2 1 2 1 ...
        cnts = [0] * 3
        for num in stones:
            if not (m := num % 3):
                cnts[m] ^= 1
            else:
                cnts[m] += 1
        if not cnts[0]:
            # Alice获胜的策略必然是先取1或2中更少的那个，如果有一个没得可取，
            # 那么Alice必然是拿到第一个模3余0（第三次为Alice取），要么石子全拿光也不会是0（比如两个1）
            return min(cnts[1], cnts[2]) > 0
        else:
            # 拥有了一个先手反制的选择（再非第一回合选择模3余0的数，会导致本来该自己必须选某堆石子变为对方必须先选）
            # 那么Alice第一回合必须拿更多的那边的石子（更少会导致对方拿模3余0，我们面对上面分析的必输态）
            # 如果拿走一个以后，更多的石子和另一堆一样多 或者 只多一个，那么Bob总有永远和不为3且取光所有石子的选择。
            return abs(cnts[1] - cnts[2]) > 2
```
```Java []
class Solution {
    public boolean stoneGameIX(int[] stones) {
        int[] cnts = new int[3];
        for(int num: stones){
            int m = num % 3;
            if(m == 0)
                cnts[m] ^= 1;
            else
                cnts[m]++;
        }
        if(cnts[0] == 0)
            return Math.min(cnts[1], cnts[2]) > 0;
        else
            return Math.abs(cnts[1] - cnts[2]) > 2;
    }
}
```
```JavaScript []
/**
 * @param {number[]} stones
 * @return {boolean}
 */
var stoneGameIX = function(stones) {
    const cnts = new Array(3)
    cnts.fill(0)
    for(const num of stones){
        const m = num % 3
        if(m == 0)
            cnts[m] ^= 1
        else
            cnts[m]++
    }
    if(cnts[0] == 0)
        return Math.min(cnts[1], cnts[2]) > 0
    else
        return Math.abs(cnts[1] - cnts[2]) > 2
};
```
```Go []
func stoneGameIX(stones []int) bool {
    cnts := make([]int, 3)
    for _, num := range stones{
        if m := num % 3; m == 0 {
            cnts[m] ^= 1
        } else {
            cnts[m]++
        }
    }
    if cnts[0] == 0{
        return cnts[1] > 0 && cnts[2] > 0
    } else {
        return cnts[1] - cnts[2] > 2 || cnts[2] - cnts[1] > 2
    }
}
```
```C []
bool stoneGameIX(int* stones, int stonesSize){
    int zero = 0, one = 0, two = 0;
    for(int i = 0; i < stonesSize; i++){
        int m = stones[i] % 3;
        if(m == 0)
            zero ^= 1;
        else if(m == 1)
            one++;
        else
            two++;
    }
    if(zero == 0)
        return one > 0 && two > 0;
    else
        return one - two > 2 || two - one > 2;
}
```