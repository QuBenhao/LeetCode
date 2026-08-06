# [Python/Java/JavaScript]  最小/最大堆 第K大/小的数

> slug: pythonjavajavascript-zui-xiao-zui-da-dui-at7l
> date: 2021-10-05
> tags: Java, JavaScript, Python, Python3
> question: Third Maximum Number (third-maximum-number)
> url: https://leetcode.cn/problems/third-maximum-number/solutions/h22kID/pythonjavajavascript-zui-xiao-zui-da-dui-at7l/

---
### 解题思路
以最小堆扫描一遍，如果大小超过3就提出一个最小的元素(必然不是第三大)，最终返回答案即可。

### 代码

```Python3 []
K = 3
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        pq = []
        for num in set(nums):
            heapq.heappush(pq, num)
            if len(pq) > K:
                heapq.heappop(pq)
        return heapq.heappop(pq) if len(pq) == K else pq[-1]
```
```Java []
class Solution {
    private static final int K = 3;
    public int thirdMax(int[] nums) {
        Set<Integer> explored = new HashSet<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int max = Integer.MIN_VALUE;
        for(int num: nums){
            if(explored.contains(num))
                continue;
            explored.add(num);
            pq.add(num);
            if(pq.size() > K)
                pq.poll();
            max = Math.max(num, max);
        }
        return pq.size() == K ? pq.poll() : max;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
const K = 3;
var thirdMax = function(nums) {
    const pq = new MinPriorityQueue();
    const myset = new Set();
    for(const num of nums){
        if(!myset.has(num)){
            myset.add(num);
            pq.enqueue(num, num);
            if(pq.size() > K){
                pq.dequeue();
            }
        }
    }
    return pq.size() == K ? pq.front()['element'] : pq.back()['element'];
};
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    // 不大了解JavaScript最小堆咋写的话，可以用仨变量的写法，意思一样
    let first, second, third;
    for(const num of nums){
        if(first === undefined || num > first){
            third = second;
            second = first;
            first = num;
        // 必须去除相等的情况，重复的数字不考虑
        } else if(first > num && (second === undefined || num > second)){
            third = second;
            second = num;
        } else if(second > num && (third === undefined || num > third)){
            third = num;
        }
    }
    return third !== undefined ? third : first;
};
```