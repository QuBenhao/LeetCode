# [Python/Java/JavaScript/Go] Simulation

> slug: pythonjavajavascriptgo-mo-ni-by-himymben-06fd
> date: 2022-01-17
> tags: Go, Java, JavaScript, Python, Python3
> question: Minimum Time Difference (minimum-time-difference)
> url: https://leetcode.cn/problems/minimum-time-difference/solutions/kKpSR9/pythonjavajavascriptgo-mo-ni-by-himymben-06fd/

---
### Approach
There are $24$ hours in a day and $60$ minutes in an hour, giving $24*60=1440$ minutes per day. We can restate the problem as follows:

> There are 1440 seats arranged in a circle, numbered from 0 to 1439.
> Seat 0 is adjacent to 1 and 1439; seat 1 is adjacent to 0 and 2; and so on.
> There are n people with seat numbers that may be the same or different. Find the smallest distance between any two people once seated.

If there are more people than seats, the pigeonhole principle guarantees that at least two people share a seat, so the minimum distance is 0.
Otherwise, going around the circle in order is enough to find the closest pair.

### Code

```Python3 []
TOTAL = 24 * 60
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        return 0 if len(timePoints) > TOTAL or not (s:=sorted(int(t[:2]) * 60 + int(t[-2:]) for t in timePoints)) else min((s[i] - s[i-1]) % TOTAL for i in range(len(s)))
```
```Java []
class Solution {
    private static final int TOTAL = 24 * 60;
    public int findMinDifference(List<String> timePoints) {
        if(timePoints.size() > TOTAL)
            return 0;
        int[] nums = new int[timePoints.size()];
        int minTime = TOTAL * 2;
        for(int i=0;i<nums.length;i++){
            String time = timePoints.get(i);
            int h = Integer.parseInt(time.substring(0, 2)), m = Integer.parseInt(time.substring(3, 5));
            nums[i] = h * 60 + m;
            minTime = Math.min(minTime, nums[i] + TOTAL);
        }
        Arrays.sort(nums);
        int ans = minTime - nums[nums.length - 1];
        for(int i=0;i<nums.length - 1;i++)
            ans = Math.min(ans, nums[i+1] - nums[i]);
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {string[]} timePoints
 * @return {number}
 */
const TOTAL = 24 * 60
var findMinDifference = function(timePoints) {
    if(timePoints.length > TOTAL)
        return 0
    const nums = new Array(timePoints.length)
    for(let i=0;i<nums.length;i++){
        const h = parseInt(timePoints[i].substring(0, 2)), m = parseInt(timePoints[i].substring(3, 5))
        nums[i] = h * 60 + m
    }
    nums.sort((a, b) => a - b)
    let ans = nums[0] + TOTAL - nums[nums.length - 1];
    for(let i=0;i<nums.length-1;i++)
        ans = Math.min(ans, nums[i+1] - nums[i])
    return ans
};
```
```Go []
const total int = 24 * 60
func findMinDifference(timePoints []string) int {
    if len(timePoints) > total {
        return 0
    }
    nums := make([]int, len(timePoints))
    for i := 0; i < len(timePoints); i++ {
        h, _ := strconv.Atoi(timePoints[i][:2])
        m, _ := strconv.Atoi(timePoints[i][3:])
        nums[i] = h * 60 + m
    }
    sort.Ints(nums)
    ans := nums[0] + total - nums[len(nums) - 1]
    for i := 0; i < len(nums) - 1; i++ {
        if v := nums[i+1] - nums[i]; v < ans {
            ans = v
        }
    }
    return ans
}
```

Here is Python code that traverses the circle without sorting.
```Python3 
TOTAL = 24 * 60
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > TOTAL:
            return 0
        seats = [0] * TOTAL
        for t in timePoints:
            seats[int(t[:2]) * 60 + int(t[-2:])] += 1
        first, last, ans = None, None, TOTAL
        for i in range(TOTAL):
            if seats[i] > 1:
                return 0
            elif seats[i]:
                if first is None:
                    first = last = i
                else:
                    ans = min(ans, i - last)
                last = i
        return min(ans, first - last + TOTAL)
```
