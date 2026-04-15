# [Python/Java/JavaScript/Go] 模拟

> Author: Benhao
> Date: 2022-04-04
> Upvotes: 25
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
新出的bit_count一直没机会用，不容易

### 代码

```Python3 []
PRIMES = {2, 3, 5, 7, 11, 13, 17, 19}
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(i.bit_count() in PRIMES for i in range(left, right + 1))
```
```Java []
class Solution {
    private static final Set<Integer> PRIMES = new HashSet<>();
    static {
        PRIMES.add(2); PRIMES.add(3); PRIMES.add(5); PRIMES.add(7); PRIMES.add(11); PRIMES.add(13); PRIMES.add(17); PRIMES.add(19);
    };
    public int countPrimeSetBits(int left, int right) {
        int ans = 0;
        for(int i = left; i <= right; i++) {
            int cur = 0, j = i;
            while(j > 0) {
                cur++;
                j -= j & (-j);
            }
            if(PRIMES.contains(cur))
                ans++;
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
const PRIMES = new Set()
PRIMES.add(2); PRIMES.add(3); PRIMES.add(5); PRIMES.add(7); PRIMES.add(11); PRIMES.add(13); PRIMES.add(17); PRIMES.add(19);
var countPrimeSetBits = function(left, right) {
    let ans = 0
    for(let i = left; i <= right; i++) {
        let cur = 0, j = i
        while(j > 0) {
            cur++
            j -= j & (-j)
        }
        if(PRIMES.has(cur))
            ans++
    }
    return ans
};
```
```Go []
func countPrimeSetBits(left int, right int) (ans int) {
    PRIMES := map[int]bool{2:true, 3:true, 5:true, 7:true, 11:true, 13:true, 17:true, 19:true}
    for i := left; i <= right; i++ {
        cur := 0
        for j := i; j > 0; j -= j & (-j) {
            cur++
        }
        if PRIMES[cur] {
            ans++
        }
    }
    return
}
```