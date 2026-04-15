# [Python/Java/TypeScript/Go] 模拟 -> 差分+二分

> Author: Benhao
> Date: 2022-08-19
> Upvotes: 18
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
只查一个时间遍历即可

进阶：如果要反复查任意时间点的做作业个数，可以用差分统计各个区间的情况，然后用二分查询返回。

### 代码

```Python3 []
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(start <= queryTime <= end for start, end in zip(startTime, endTime))
```
```Java []
class Solution {
    public int busyStudent(int[] startTime, int[] endTime, int queryTime) {
        int ans = 0;
        for (int i = 0; i < startTime.length; i++) {
            if (startTime[i] <= queryTime && queryTime <= endTime[i]) {
                ans++;
            }
        }
        return ans;
    }
}
```
```TypeScript []
function busyStudent(startTime: number[], endTime: number[], queryTime: number): number {
    let ans = 0
    for (let i = 0; i < startTime.length; i++) {
        if (startTime[i] <= queryTime && queryTime <= endTime[i]) {
            ans++
        }
    }
    return ans
};
```
```Go []
func busyStudent(startTime []int, endTime []int, queryTime int) (ans int) {
    for i := 0; i < len(startTime); i++ {
        if startTime[i] <= queryTime && queryTime <= endTime[i] {
            ans++
        }
    }
    return
}
```

```Python3 [v1-Py3 差分+二分]
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        n = len(startTime)
        diff = defaultdict(int)
        for i in range(n):
            diff[startTime[i]] += 1
            diff[endTime[i] + 1] -= 1
        ans, d = [], 0
        for k, v in sorted(diff.items()):
            if not v:
                continue
            d += v
            ans.append([k, d])
        # 感兴趣的朋友可以把ans打印出来看
        # print(ans)
        # 在第一个学生之前的时间和在最后一个学生之后的时间都会走最后的0
        return ans[bisect_right(ans, queryTime, key=lambda x:x[0]) - 1][1]
```
```Go [v1-Go 差分+二分]
func busyStudent(startTime []int, endTime []int, queryTime int) int {
    diff := map[int]int{}
    for i := 0; i < len(startTime); i++ {
        diff[startTime[i]] += 1
        diff[endTime[i] + 1] -= 1
    }
    d := 0
    var keys []int
	for k := range diff {
		keys = append(keys, k)
	}
	sort.Ints(keys)
    ans := [][]int{}
    ans = append(ans, []int{0, 0})
    for _, k := range keys {
        if diff[k] != 0 {
            d += diff[k]
            ans = append(ans, []int{k, d})
        }
    }
    left, right := 0, len(ans)
    for left < right {
        mid := (left + right) >> 1
        if ans[mid][0] <= queryTime {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return ans[left - 1][1]
}
```