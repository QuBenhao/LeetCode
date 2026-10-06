# [Python/Java/TypeScript/Go] Exhaustive enumeration

> Author: Benhao
> Date: 2022-09-14
> Upvotes: 36
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
There are only four operations, and each matters only modulo two: pressing the same button twice cancels out.
1. With two bulbs, operation 4 equals operation 3, so handle this separately.
2. With one bulb, operation 4 equals operation 3, and operation 2 does nothing, so handle this separately.
3. With more than two bulbs, all four operations differ. Analyze the number of presses to determine the choices.

### Code

```python3
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        if n > 2:
            if presses == 1:
                return 4
            if presses == 2:
                return comb(4, 2) + 1 # Choose two of the four operations, plus no net operation
            if presses == 3:
                return comb(4, 3) + 4 # Choose three of the four operations, or two canceling presses plus one operation
            if presses == 4:
                return comb(4, 2) + 2 # Choose two operations plus two canceling presses, no net operation, or all four operations
            return comb(4, 2) + 2 # Reduce odd press counts to 3 and even counts to 4
        elif n == 2:
            if presses == 1:
                return 3 
            if presses == 2:
                return comb(3, 2) + 1
            if presses == 3:
                return comb(3, 1) + 1
            return 4 # Reduce odd press counts to 3 and even counts to 2
        return 2
```
The code above simplifies to
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
