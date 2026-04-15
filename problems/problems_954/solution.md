# [Python/Java/JavaScript/Go] 哈希表排序

> Author: Benhao
> Date: 2022-03-31
> Upvotes: 20
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
题目要求长度为$n$的数组是否能分为$\frac{n}{2}$组，每组都是一个数是另一个数的两倍。
想想数组中最大的数或者最小的数，会发现它们要配对的数是固定的，很容易检查。
我们将数组压缩为哈希表计数，并按序遍历键，依次抛去配对数，不能配对直接返回false。

### 代码

```Python3 []
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnts = Counter(arr)
        for k in sorted(cnts.keys()):
            # 正数和自己乘二配对
            if k > 0 and cnts[k * 2] < cnts[k]:
                return False
            elif k > 0:
                cnts[k * 2] -= cnts[k]
            # 负数要和自己除二配对，因为是除法要讨论奇偶
            elif k < 0 and cnts[k] and (k % 2 or cnts[k // 2] < cnts[k]):
                return False
            elif k < 0:
                cnts[k / 2] -= cnts[k]
            # 0本身要自己有偶数个，才能配对
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