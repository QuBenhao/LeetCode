# [Python/Java/TypeScript/Go] 栈模拟

> Author: Benhao
> Date: 2022-07-13
> Upvotes: 15
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
用栈模拟当前行星碰撞后的情况。
因为每次发生碰撞都是先讨论最后一个向右的和当前的向左的，
看当前的向左的能一直往左(栈顶依次弹出)碰到多少个，是符合后进先出的。
其他情况因为暂时不会发生碰撞，所以直接入栈。

### 代码

```Python3 []
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            add = True
            # 只有新来的向左的，才有可能和原来的发生碰撞 (想象最后一个是向右的话，没有人能和它相撞)
            if ast < 0:
                # 依次遍历栈顶全部向右的，它们会和当前的相撞，如果它们大小小于当前的大小，它们会被撞没
                while stack and stack[-1] > 0 and stack[-1] < -ast:
                    stack.pop()
                # 如果还存在向右的，说明当前的大小撞不过栈顶
                if stack and stack[-1] > 0:
                    add = False
                    # 两个一样大的都要消失
                    if stack[-1] == -ast:
                        stack.pop()
            if add:
                stack.append(ast)
        return stack
```
```Java []
class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> stack = new ArrayDeque<>();
        out:
        for (int ast: asteroids) {
            if (ast < 0) {
                while (!stack.isEmpty() && stack.peekLast() > 0 && stack.peekLast() < -ast) {
                    stack.pollLast();
                }
                if (!stack.isEmpty() && stack.peekLast() > 0) {
                    if (stack.peekLast() == -ast) {
                        stack.pollLast();
                    }
                    continue out;
                }
            }
            stack.addLast(ast);
        }
        int[] ans = new int[stack.size()];
        for (int i = 0, n = stack.size(); i < n; i++) {
            ans[i] = stack.pollFirst();
        }
        return ans;
    }
}
```
```TypeScript []
function asteroidCollision(asteroids: number[]): number[] {
    const stack = new Array<number>()
    out:
    for (const ast of asteroids) {
        if (ast < 0) {
            while (stack.length > 0 && stack[stack.length - 1] > 0 && stack[stack.length - 1] < -ast) {
                stack.pop()
            }
            if (stack.length > 0 && stack[stack.length - 1] > 0) {
                if (stack[stack.length - 1] == -ast) {
                    stack.pop()
                }
                continue out
            }
        }
        stack.push(ast)
    }
    return stack
};
```
```Go []
func asteroidCollision(asteroids []int) (ans []int) {
    out:
    for _, ast := range asteroids {
        if ast < 0 {
            for len(ans) > 0 && ans[len(ans) - 1] > 0 && ans[len(ans) - 1] < -ast {
                ans = ans[:len(ans) - 1]
            }
            if l := len(ans); l > 0 && ans[l - 1] > 0 {
                if ans[l - 1] == -ast {
                    ans = ans[:l - 1]
                }
                continue out
            }
        }
        ans = append(ans, ast)
    }
    return
}
```