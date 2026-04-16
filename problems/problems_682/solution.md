# [Python/Java/JavaScript/Go] 模拟

> Author: Benhao
> Date: 2022-03-26
> Upvotes: 19
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
像在写业务代码

### 代码

```Python3 []
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        records = []
        for op in ops:
            match op:
                case "D":
                    records.append(records[-1] * 2)
                case "C":
                    records.pop()
                case "+":
                    records.append(records[-2] + records[-1])
                case _:
                    records.append(int(op))
        return sum(records)
```
```Java []
class Solution {
    public int calPoints(String[] ops) {
        List<Integer> records = new ArrayList<>();
        for(String op: ops) {
            int curSize = records.size();
            switch(op) {
                case "+":
                    records.add(records.get(curSize - 2) + records.get(curSize - 1));
                    break;
                case "D":
                    records.add(records.get(curSize - 1) * 2);
                    break;
                case "C":
                    records.remove(curSize - 1);
                    break;
                default:
                    records.add(Integer.parseInt(op));
            }
        }
        int ans = 0;
        for(int r: records)
            ans += r;
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {string[]} ops
 * @return {number}
 */
var calPoints = function(ops) {
    const records = new Array()
    for(const op of ops) {
        const length = records.length
        switch(op) {
            case "+":
                records.push(records[length - 2] + records[length - 1])
                break
            case "D":
                records.push(records[length - 1] * 2)
                break
            case "C":
                records.pop()
                break
            default:
                records.push(parseInt(op))
        }
    }
    let ans = 0
    for(const r of records)
        ans += r
    return ans
};
```
```Go []
func calPoints(ops []string) (ans int) {
    records := []int{}
    for _, op := range ops {
        if l := len(records); op == "+" {
            records = append(records, records[l - 2] + records[l - 1])
        } else if op == "D" {
            records = append(records, records[l - 1] * 2)
        } else if op == "C" {
            records = records[:l-1]
        } else {
            v, _ := strconv.Atoi(op)
            records = append(records, v)
        }
    }
    for _, r := range records {
        ans += r
    }
    return
}
```