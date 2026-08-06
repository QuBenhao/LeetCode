# [Python/Java/JavaScript/Go] 计算日期与今天的天数差

> slug: pythonjavajavascriptgo-ji-suan-ri-qi-yu-5lp2p
> date: 2022-01-03
> tags: Go, Java, JavaScript, Python, Python3
> question: Day of the Week (day-of-the-week)
> url: https://leetcode.cn/problems/day-of-the-week/solutions/6bpFFC/pythonjavajavascriptgo-ji-suan-ri-qi-yu-5lp2p/

---
### 解题思路
已知今天是星期一，只需要知道输入的日期与今天的天数差，再对七取余就可以算出该日期是星期几。

### 代码

```Python3 []
ANS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def helper(d, m, y):
            # 2022.1.3 星期一
            ans = 1 
            # 天数的偏移量
            ans = (ans + d - 3) % 7
            # 计算年的偏差量
            if y < 2022:
                for i in range(y, 2022):
                    ans = (ans - (366 if not i % 4 and (i % 100 or not i % 400) else 365)) % 7
            else:
                for i in range(2022, y):
                    ans = (ans + (366 if not i % 4 and (i % 100 or not i % 400) else 365)) % 7
            # 计算月的偏差量
            for i in range(m - 1):
                ans = (ans + DAYS[i]) % 7
                if i == 1 and not y % 4 and (y % 100 or not y % 400):
                    ans = (ans + 1) % 7
            return ans
        return ANS[helper(day, month, year)]
```
```Java []
class Solution {
    private static final String[] ANS = new String[]{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
    private static final int[] DAYS = new int[]{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    public String dayOfTheWeek(int day, int month, int year) {
        int ans = (day - 2) % 7;
        if(year < 2022)
            for(int i=year;i<2022;i++)
                ans = (ans - (i % 4 == 0 && (i % 100 != 0 || i % 400 == 0) ? 366:365)) % 7;
        else
            for(int i=2022;i<year;i++)
                ans = (ans + (i % 4 == 0 && (i % 100 != 0 || i % 400 == 0) ? 366:365)) % 7;
        for(int i=0;i<month-1;i++){
            ans = (ans + DAYS[i]) % 7;
            if(i == 1 && (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)))
                ans = (ans + 1) % 7;
        }
        return ANS[(ans + 7) % 7];
    }
}
```
```JavaScript []
/**
 * @param {number} day
 * @param {number} month
 * @param {number} year
 * @return {string}
 */
const ANS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
const DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
var dayOfTheWeek = function(day, month, year) {
    let ans = (day - 2) % 7
    if(year < 2022)
        for(let i=year;i<2022;i++)
            ans = (ans - (i % 4 == 0 && (i % 100 != 0 || i % 400 == 0) ? 366 : 365)) % 7
    else
        for(let i=2022;i<year;i++)
            ans = (ans + (i % 4 == 0 && (i % 100 != 0 || i % 400 == 0) ? 366 : 365)) % 7
    for(let i=0;i<month-1;i++){
        ans = (ans + DAYS[i]) % 7
        if(i == 1 && (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)))
            ans = (ans + 1) % 7
    }
    return ANS[(ans + 7) % 7]
};
```
```Go []
func dayOfTheWeek(day int, month int, year int) string {
    ANS := []string{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
    DAYS := []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
    ans := (day - 2) % 7
    if year < 2022 {
        for i := year; i < 2022; i++ {
            if (i % 4 == 0 && (i % 100 != 0 || i % 400 == 0)){
                ans = (ans - 366) % 7
            }else{
                ans = (ans - 365) % 7
            }
        }
    }else{
        for i := 2022; i < year; i++ {
            if (i % 4 == 0 && (i % 100 != 0 || i % 400 == 0)){
                ans = (ans + 366) % 7
            }else{
                ans = (ans + 365) % 7
            }
        }
    }
    for i:=0;i<month-1;i++{
        ans = (ans + DAYS[i]) % 7
        if i == 1 && (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)){
            ans = (ans + 1) % 7
        }
    }
    return ANS[(ans + 7)%7]
}
```