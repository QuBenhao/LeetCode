# [Python/Java/TypeScript/Go] 哈希表 

> slug: pythonjavatypescriptgo-ha-xi-biao-by-him-bbph
> date: 2022-08-18
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Maximum Equal Frequency (maximum-equal-frequency)
> url: https://leetcode.cn/problems/maximum-equal-frequency/solutions/bJ4Tvg/pythonjavatypescriptgo-ha-xi-biao-by-him-bbph/

---
### 解题思路
哈希表维护个数，以及个数的个数。
然后讨论每个位置是否在几种满足题意的条件中。

### 代码

```Python3 []
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        """
        删除一个元素后频次相同有以下几种情况:
        1. 每个数只出现一次
        2. 只有一个数比其他数出现多一次，其他数一样多 (删掉多一次的一个数)
        3. 大家都出现的一样多，只有一个数出现了一次 (删掉一次的这个数)
        那么怎么维护从头开始的个数，方便统计这三个条件呢？
        哈希表记录次数是肯定的
        1. 都是一个数，说明最大长度是1
        2. 需要统计出现的个数的个数才好确定后两种情况
        """
        counter, counter_counter, max_counts, ans = Counter(), Counter(), 0, 0
        for i, num in enumerate(nums):
            if counter[num]:
                counter_counter[counter[num]] -= 1
            counter[num] += 1
            counter_counter[counter[num]] += 1
            if counter[num] > max_counts:
                max_counts = counter[num]
            if max_counts == 1 or (counter_counter[max_counts - 1] + 1) * (max_counts - 1) == i or max_counts * counter_counter[max_counts] == i:
                ans = i + 1
        return ans
```
```Java []
class Solution {
    public int maxEqualFreq(int[] nums) {
        Map<Integer, Integer> counter = new HashMap<>(), counterCounter = new HashMap<>();
        int max = 0, ans = 0;
        for (int i = 0; i < nums.length; i++) {
            Integer old = counter.get(nums[i]);
            if (old != null) {
                counterCounter.put(old, counterCounter.get(old) - 1);
            } else {
                old = 0;
            }
            counter.put(nums[i], ++old);
            counterCounter.put(old, counterCounter.getOrDefault(old, 0) + 1);
            if (old > max) {
                max = old;
            }
            if (max == 1 || (counterCounter.getOrDefault(max - 1, 0) + 1) * (max - 1) == i || max * counterCounter.get(max) == i) {
                ans = i + 1;
            }
        }
        return ans;
    }
}
```
```TypeScript []
function maxEqualFreq(nums: number[]): number {
    const counter: Map<number, number> = new Map<number, number>(), counterCounter: Map<number, number> = new Map<number, number>()
    let max: number = 0, ans: number = 0
    for (const [i, num] of nums.entries()) {
        let val: number
        if (counter.has(num)) {
            val = counter.get(num)
            counterCounter.set(val, counterCounter.get(val) - 1)
        } else {
            val = 0
        }
        counter.set(num, ++val)
        if (counterCounter.has(val)) {
            counterCounter.set(val, counterCounter.get(val) + 1)
        } else {
            counterCounter.set(val, 1)
        }
        if (val > max) {
            max = val
        }
        if (max == 1 || (counterCounter.has(max - 1) && (counterCounter.get(max - 1) + 1) * (max - 1) == i) || max * counterCounter.get(max) == i) {
            ans = i + 1
        } 
    }
    return ans
};
```
```Go []
func maxEqualFreq(nums []int) (ans int) {
    counter, counter_counter, max := map[int]int{}, map[int]int{}, 0
    for i, num := range nums {
        v := counter[num]
        if v > 0 {
            counter_counter[v] -= 1
        }
        v++
        counter[num] = v
        counter_counter[v] += 1
        if v > max {
            max = v
        }
        if max == 1 || (counter_counter[max - 1] + 1) * (max - 1) == i || max * counter_counter[max] == i {
            ans = i + 1
        }
    }
    return
}
```