# [Python/Java/JavaScript/Go] Hash table and sorting

> Author: Benhao
> Date: 2022-03-31
> Upvotes: 20
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
Determine whether an array of length $n$ can be divided into $\frac{n}{2}$ pairs, each containing a number and its double.
Consider the largest or smallest number: its matching value is fixed and easy to check.
Compress the array into hash-table counts, iterate over the keys in order, and remove matched pairs. Return false immediately if a value cannot be paired.

### Code

```Python3 []
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnts = Counter(arr)
        for k in sorted(cnts.keys()):
            # Pair positive numbers with their doubles
            if k > 0 and cnts[k * 2] < cnts[k]:
                return False
            elif k > 0:
                cnts[k * 2] -= cnts[k]
            # Pair negative numbers with their halves; division requires checking parity
            elif k < 0 and cnts[k] and (k % 2 or cnts[k // 2] < cnts[k]):
                return False
            elif k < 0:
                cnts[k / 2] -= cnts[k]
            # Zeros must occur an even number of times to be paired
            elif cnts[k] % 2:
                return False
        return True
```
```Java []
class Solution {
    public boolean canReorderDoubled(int[] arr) {
        Map<Integer, Integer> cnts = new HashMap<>();
        for(int num: arr)
            cnts.put(num, cnts.getOrDefault(num, 0) + 1);
        List<Integer> list = new ArrayList<>(cnts.keySet());
        Collections.sort(list, (a, b) -> a - b);
        for(int key: list) {
            if(key > 0) {
                if(cnts.getOrDefault(key * 2, 0) < cnts.get(key))
                    return false;
                if(cnts.get(key) > 0)
                    cnts.put(key * 2, cnts.get(key * 2) - cnts.get(key));
            } else if(key == 0) {
                if(cnts.get(key) % 2 != 0)
                    return false;
            }
            else {
                if(cnts.get(key) > 0 && (key % 2 != 0 || cnts.getOrDefault(key/2, 0) < cnts.get(key)))
                    return false;
                if(cnts.get(key) > 0)
                    cnts.put(key / 2, cnts.get(key / 2) - cnts.get(key));
            }
        }
        return true;
    }
}
```
```JavaScript []
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var canReorderDoubled = function(arr) {
    const cnts = new Map()
    for(const num of arr) {
        if(cnts.has(num))
            cnts.set(num, cnts.get(num) + 1)
        else
            cnts.set(num, 1)
    }
    const keys = Array.from(cnts.keys())
    keys.sort((a, b) => a - b)
    for(const key of keys) {
        if(key > 0) {
            if(cnts.get(key) > 0) {
                if(!cnts.has(key * 2) || cnts.get(key * 2) < cnts.get(key))
                    return false
                cnts.set(key * 2, cnts.get(key * 2) - cnts.get(key))
            }
        } else if (key == 0) {
            if(cnts.get(key) % 2 == 1)
                return false
        } else {
            if(cnts.get(key) > 0 && (key % 2 != 0 || !cnts.has(key/2) || cnts.get(key/2) < cnts.get(key)))
                return false
            cnts.set(key / 2, cnts.get(key / 2) - cnts.get(key))
        }
    }
    return true
};
```
```Go []
func canReorderDoubled(arr []int) bool {
    cnts := map[int]int{}
    for _, num := range arr {
        cnts[num]++
    }
    keys := []int{}
    for k := range cnts {
        keys = append(keys, k)
    }
    sort.Ints(keys)
    for _, key := range keys {
        if key > 0 {
            if cnts[key * 2] < cnts[key] {
                return false
            }
            cnts[key * 2] -= cnts[key]
        } else if key == 0 {
            if cnts[key] % 2 == 1 {
                return false
            }
        } else {
            if cnts[key] > 0 && (key % 2 != 0 || cnts[key / 2] < cnts[key]) {
                return false
            }
            cnts[key / 2] -= cnts[key]
        }
    }
    return true
}
```
