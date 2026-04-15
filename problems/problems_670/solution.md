# [Python/Java/TypeScript/Go] 单调栈

> Author: Benhao
> Date: 2022-09-12
> Upvotes: 38
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
我们想找到左边第一个比右边某个大数小的，左边尽可能靠左，右边尽可能大且尽可能靠右。
我们维护被交换的坐标，当出现可以交换更左边的时候(单调栈弹出)，左边变为弹出坐标。
当出现更大的数将右边交换的坐标弹出时，右边坐标变为新坐标。
当出现与右边坐标一样大的但更靠右时，右边坐标变为新坐标。

### 代码

```Python3 []
class Solution:
    def maximumSwap(self, num: int) -> int:
        s, stack, left, right = str(num), [], None, None
        for i, c in enumerate(s):
            while stack and s[stack[-1]] < c:
                idx = stack.pop()
                if left is None or idx < left:
                    left, right = idx, i
                if idx == right:
                    right = i
            if right is not None and c == s[right]:
                right = i
            stack.append(i)
        return int(s[:left] + s[right] + s[left+1:right] + s[left] + s[right+1:]) if left is not None else num
```
```Java []
class Solution {
    public int maximumSwap(int num) {
        char[] chars = String.valueOf(num).toCharArray();
        int n = chars.length;
        int left = n, right = n;
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && chars[stack.peekLast()] < chars[i]) {
                int idx = stack.removeLast();
                if (idx < left) {
                    left = idx;
                    right = i;
                }
                if (idx == right) {
                    right = i;
                }
            }
            if (right < n && chars[right] == chars[i]) {
                right = i;
            }
            stack.addLast(i);
        }
        if (left < n) {
            char tmp = chars[left];
            chars[left] = chars[right];
            chars[right] = tmp;
            return Integer.parseInt(new String(chars));
        }
        return num;
    }
}
```
```TypeScript []
function maximumSwap(num: number): number {
    const chars: Array<string> = [..."" + num], stack: Array<number> = new Array<number>()
    const n: number = chars.length
    let left: number = n, right: number = n
    for (let i = 0; i < n; i++) {
        while (stack.length > 0 && chars[stack[stack.length - 1]] < chars[i]) {
            const idx: number = stack.pop()
            if (idx < left) {
                left = idx
                right = i
            }
            if (idx == right) {
                right = i
            }
        }
        if (right < n && chars[right] == chars[i]) {
            right = i
        }
        stack.push(i)
    }
    if (left < n) {
        [chars[left], chars[right]] = [chars[right], chars[left]]
        return parseInt(chars.join(''))
    }
    return num
};
```
```Go []
func maximumSwap(num int) int {
    chars, stack := []byte(strconv.Itoa(num)), []int{}
    n := len(chars)
    left, right := n, n
    for i, c := range chars {
        for len(stack) > 0 && chars[stack[len(stack) - 1]] < c {
            idx := stack[len(stack) - 1]
            stack = stack[:len(stack) - 1]
            if idx < left {
                left, right = idx, i
            }
            if idx == right {
                right = i
            }
        }
        if right < n && chars[right] == c {
            right = i
        }
        stack = append(stack, i)
    }
    if left < n {
        chars[left], chars[right] = chars[right], chars[left]
        ans, _ := strconv.Atoi(string(chars))
        return ans
    }
    return num
}
```