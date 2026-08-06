# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-mo-ni-by-himymben-06fd
> date: 2022-01-17
> tags: Go, Java, JavaScript, Python, Python3
> question: Minimum Time Difference (minimum-time-difference)
> url: https://leetcode.cn/problems/minimum-time-difference/solutions/kKpSR9/pythonjavajavascriptgo-mo-ni-by-himymben-06fd/

---
### 解题思路
一天有$24$小时，一小时有$60$分钟，一天一共有$24*60=1440$分钟，所以转换一下本题是：

> 有1440个座位排成一个圆圈，编号从0到1439
> 0与1和1439相邻，1与0和2相邻，依此类推。
> 有n个人拿着可能不同、可能相同的编号来落座，问最后挨得最近的人

显然如果人数比整个座位多，由抽屉原理可知，至少有一个座位坐了两个人，那么最小的距离必然是0。
其他时候我们只需要按顺序转完一圈，就知道谁是最近的了。

### 代码

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

这里给出不需要排序的遍历圈的Python代码
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