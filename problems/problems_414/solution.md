# [Python/Java/JavaScript] Min-/max-heap for the kth largest/smallest value

> slug: pythonjavajavascript-zui-xiao-zui-da-dui-at7l
> date: 2021-10-05
> tags: Java, JavaScript, Python, Python3
> question: Third Maximum Number (third-maximum-number)
> url: https://leetcode.cn/problems/third-maximum-number/solutions/h22kID/pythonjavajavascript-zui-xiao-zui-da-dui-at7l/

---
### Approach
Scan once with a min-heap. Whenever its size exceeds 3, remove the minimum, which cannot be the third largest. Return the resulting answer.

### Code

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
    // If writing a JavaScript min-heap is unfamiliar, use three variables for the same idea
    let first, second, third;
    for(const num of nums){
        if(first === undefined || num > first){
            third = second;
            second = first;
            first = num;
        // Exclude equal values; duplicates do not count
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
