# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-mo-ni-by-himymben-kfqb
> date: 2021-12-20
> tags: Go, Java, JavaScript, Python, Python3
> question: Day of the Year (day-of-the-year)
> url: https://leetcode.cn/problems/day-of-the-year/solutions/AQJS8Z/pythonjavajavascriptgo-mo-ni-by-himymben-kfqb/

---
### 解题思路
考察了一下计算闰年的规则

### 代码

```python3 []
class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [0] + list(accumulate([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]))
        y, m, d = int(date[:4]), int(date[5:7]), int(date[-2:])
        if m > 2 and (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)):
            return days[m - 1] + d + 1
        return days[m - 1] + d
```
```Java []
class Solution {
    private static final int[] days = new int[]{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    static{
        for(int i=1;i<days.length;i++)
            days[i] += days[i-1];
    }
    public int dayOfYear(String date) {
        String[] sd = date.split("-");
        int y = Integer.parseInt(sd[0]), m = Integer.parseInt(sd[1]), d = Integer.parseInt(sd[2]);
        return days[m - 1] + d + ((m > 2 && (y % 400 == 0 || (y % 4 == 0 && y % 100 != 0))) ? 1 : 0);
    }
}
```
```JavaScript []
/**
 * @param {string} date
 * @return {number}
 */
var dayOfYear = function(date) {
    const days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    for(let i=1;i<days.length;i++)
        days[i] += days[i-1]
    const y = +date.substring(0, 4), m = +date.substring(5, 7), d = +date.substring(8, 10)
    return days[m - 1] + d + ((m > 2 && (y % 400 == 0 || (y % 4 == 0 && y % 100 != 0))) ? 1: 0)
};
```
```Go []
func dayOfYear(date string) int {
    days := []int{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
    for i := 1; i < len(days); i++{
        days[i] += days[i-1]
    }
    y, _ := strconv.Atoi(date[:4])
    m, _ := strconv.Atoi(date[5:7])
    d, _ := strconv.Atoi(date[8:])
    if m > 2 && (y % 400 == 0 || (y % 4 == 0 && y % 100 != 0)){
        return days[m-1] + d + 1
    }
    return days[m-1] + d
}
```

记录一些不需要记的时间模块用法
```python3 []
class Solution:
    def dayOfYear(self, date: str) -> int:
        return int((datetime.datetime.strptime(date, "%Y-%m-%d")).strftime('%j'))
```
```Java []
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
class Solution {
    private static final DateTimeFormatter FORMAT = DateTimeFormatter.ofPattern("yyyy-MM-dd");         
    public int dayOfYear(String date) {
        return LocalDate.parse(date, FORMAT).getDayOfYear();
    }
}
```
```JavaScript []
/**
 * @param {string} date
 * @return {number}
 */
var dayOfYear = function(date) {
    const d = new Date(date.replace(/-/,"/"))
    const first = new Date(d)
    first.setMonth(0)
    first.setDate(1)
    return Math.ceil((d - first) / (24 * 60 * 60 * 1000)) + 1
};
```
```Go []
import "time"
func dayOfYear(date string) int {
    t, _ := time.Parse("2006-01-02", date)
    s, _ := time.Parse("2006-01-02", date[:4] + "-01-01")
    return int((t.Sub(s).Hours())/24 + 1)
}
```