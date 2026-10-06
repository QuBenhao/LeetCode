# [Python/Java/TypeScript/Go] Monotonic stack

> Author: Benhao
> Date: 2022-09-12
> Upvotes: 38
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
Find the earliest digit that is smaller than some digit to its right. The left digit should be as far left as possible; the right digit should be as large, and as far right, as possible.
Track the indices to swap. When the monotonic stack pops an index farther left that can be swapped, update the left index to it.
If a larger digit pops the current right swap index, replace the right index with the new one.
If an equally large digit appears farther right, update the right index to the new position.

### Code

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
