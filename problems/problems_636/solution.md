# [Python/Java/TypeScript/Go] 栈模拟

> Author: Benhao
> Date: 2022-08-07
> Upvotes: 23
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
由于本题是单线程CPU，一个任务进栈必然最终会由对应的该任务出栈结束。
我们只需要能在任务出栈的时候统计它和进栈的时候的时间差即可。
注意到期间可能在处理别的任务，所以我们需要排除掉其他任务的时间。
比较简单的做法是统计一个独立任务时间的总和，并在进栈的时候加入当时的总和。
那么出栈计算的时候减去中间被占用的独立时间就好了。

### 代码

```Python3 []
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        def helper(log):
            idx, mark, time = log.split(":")
            return int(idx), mark == "start", int(time)

        stack, ans, total = [], [0] * n, 0
        for lg in logs:
            idx, is_start, time = helper(lg)
            if is_start:
                stack.append((idx, time, total))
            else:
                _, t, s = stack.pop()
                diff = time + 1 - t - total + s
                ans[idx] += diff
                total += diff
        return ans
```
```Java []
class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        int[] ans = new int[n];
        Deque<int[]> stack = new ArrayDeque<>();
        int total = 0;
        for (String log: logs) {
            String[] splits = log.split(":");
            int idx = Integer.parseInt(splits[0]), time = Integer.parseInt(splits[2]);
            boolean isStart = "start".compareTo(splits[1]) == 0;
            if (isStart) {
                stack.addLast(new int[]{time, total});
            } else {
                int[] last = stack.removeLast();
                int diff = (time + 1 - last[0]) - (total - last[1]);
                ans[idx] += diff;
                total += diff;
            }
        }
        return ans;
    }
}
```
```TypeScript []
function exclusiveTime(n: number, logs: string[]): number[] {
    const ans = new Array<number>(n).fill(0), stack = new Array<number[]>()
    let total = 0
    for (const log of logs) {
        const [idxStr, start, timeStr] = log.split(":")
        const [idx, time] = [Number.parseInt(idxStr), Number.parseInt(timeStr)]
        if (start === "start") {
            stack.push([time, total])
        } else {
            const [t, s] = stack.pop()
            const diff = (time + 1 - t) - (total - s)
            ans[idx] += diff
            total += diff
        }
    }
    return ans
};
```
```Go []
func exclusiveTime(n int, logs []string) []int {
    ans, stack, total := make([]int, n), [][]int{}, 0
    for _, log := range logs {
        splits := strings.Split(log, ":")
        idx, _ := strconv.Atoi(splits[0])
        time, _ := strconv.Atoi(splits[2])
        if splits[1] == "start" {
            stack = append(stack, []int{time, total})
        } else {
            last := stack[len(stack) - 1]
            stack = stack[:len(stack) - 1]
            diff := (time + 1 - last[0]) - (total - last[1])
            ans[idx] += diff
            total += diff
        }
    }
    return ans
}
```
简化该表达式以后栈内只需要一个元素
```python3
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        def helper(log):
            idx, mark, time = log.split(":")
            return int(idx), mark == "start", int(time)

        stack, ans, total = [], [0] * n, 0
        for lg in logs:
            idx, is_start, time = helper(lg)
            if is_start:
                stack.append(total - time)
            else:
                d = stack.pop()
                diff = time + 1 + d - total
                ans[idx] += diff
                total += diff
        return ans
```