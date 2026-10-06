# [Python/Java/TypeScript/Go] Stack simulation

> Author: Benhao
> Date: 2022-08-07
> Upvotes: 23
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
The CPU is single-threaded, so every task pushed onto the stack eventually ends with its matching pop.
When a task is popped, calculate the time elapsed since it was pushed.
Other tasks may have run in between, so their time must be excluded.
A simple approach is to maintain the total exclusive time of completed tasks and record that total when pushing a task.
When popping, subtract the exclusive time consumed by other tasks in between.

### Code

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
Simplifying the expression leaves only one value per stack entry.
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
