# [Python/Java/JavaScript/Go/C] Game theory - analyzing Alice's winning strategy

> slug: pythonjavajavascriptgoc-bo-yi-fen-xi-by-2024o
> date: 2022-01-19
> tags: C, Go, Java, JavaScript, Python, Python3
> question: Stone Game IX (stone-game-ix)
> url: https://leetcode.cn/problems/stone-game-ix/solutions/YdJcFD/pythonjavajavascriptgoc-bo-yi-fen-xi-by-2024o/

---
### Approach
Analyze the problem:
> 1. Group stones by their remainders modulo 3; the original values make no difference within a group.
> 2. Pairs of remainder-0 stones cancel out: if the opponent is forced to take one, we can take another and leave them facing the same position again.
> 3. If the first player takes a 1, the sequence of choices must be 1 1 2 1 2 1 2 ...
> 4. If the first player takes a 2, the sequence of choices must be 2 2 1 2 1 2 1 ...
> 5. With no remainder-0 stones left (after pairing them off), Alice wins by taking from the smaller group first. This forces the opponent to keep taking from that group and run out first.
> 6. With no remainder-0 stones left (after pairing them off), if either the remainder-1 or remainder-2 group is empty, Alice either loses on the third turn or exhausts all stones without making the sum divisible by 3. Bob wins in either case.
> 7. With an odd number of remainder-0 stones, the opponent has a counter: if Alice starts with the smaller group, the opponent can take a remainder-0 stone and force her to keep taking from the smaller group, so she loses first.
>    Alice must therefore start with the larger group. Having only one or two more stones is insufficient, because Bob can always arrange for all stones to be taken without making the sum divisible by 3, and win.
>    Only when one group has at least three more stones can Alice force the opponent to make the sum divisible by 3 (start with the larger group; afterward, take from that group when the opponent takes 0, and take 0 when the opponent takes from that group).

Summary:
With an even number of stones divisible by 3, Alice starts with the smaller of the remainder-1 and remainder-2 groups. If either group is empty, Alice cannot win.
With an odd number of stones divisible by 3, Alice starts with the larger of the remainder-1 and remainder-2 groups. Unless that group has at least three more stones, Alice cannot win.

### Code

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
            # Alice must start with the smaller of the remainder-1 and remainder-2 groups. If either group is empty,
            # Alice is the first to make the sum divisible by 3 (on her third-turn move), or all stones are exhausted without doing so (for example, two 1s)
            return min(cnts[1], cnts[2]) > 0
        else:
            # There is a counter to the first player's strategy: taking a remainder-0 stone after the first turn switches which player must take from a given group first
            # Alice must therefore start with the larger group (starting with the smaller group lets the opponent take 0 and leave us in the losing position analyzed above)
            # If, after taking one stone, the larger group has the same size as the other group or only one more stone, Bob can always exhaust the stones without making the sum divisible by 3
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
