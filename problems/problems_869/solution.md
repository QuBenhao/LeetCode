# [Python/Java/JavaScript] 两个字符串判断是否打乱顺序后一样

> Author: Benhao
> Date: 2021-10-27
> Upvotes: 22
> Tags: Java, JavaScript, Python, Python3

---

### 代码
```Python3 []
NUMS = [Counter(str(1<<i)) for i in range(30)]

class Solution: 
    def reorderedPowerOf2(self, n: int) -> bool:
        return any(Counter(str(n)) == s for s in NUMS)
```
```Java []
class Solution {
    private static final Set<String> NUMS = new HashSet<>();
    static{
        for(int i=0;i<30;i++)
            NUMS.add(hash(1<<i));
    }
    public boolean reorderedPowerOf2(int n) {
        return NUMS.contains(hash(n));
    }

    private static String hash(int n){
        StringBuilder sb = new StringBuilder();
        int[] cnts = new int[10];
        Arrays.fill(cnts, 0);
        while(n > 0){
            cnts[n%10]++;
            n/=10;
        }
        for(int i=0;i<10;i++){
            sb.append(cnts[i]);
            sb.append("#");
        }
        return sb.toString();
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {boolean}
 */
const hash = (n) => {
    const cnt = new Array(10).fill(0);
    while (n) {
        cnt[n % 10]++;
        n = Math.floor(n / 10);
    }
    return cnt.join('#');
}
const NUMS = new Set();

for (let n = 1; n <= 1e9; n <<= 1) {
    NUMS.add(hash(n));
}
var reorderedPowerOf2 = function(n) {
    return NUMS.has(hash(n));
};

```

```Python3
NUMS = set(str(sorted(str(1<<i))) for i in range(30))

class Solution: 
    def reorderedPowerOf2(self, n: int) -> bool:
        return str(sorted(str(n))) in NUMS
```