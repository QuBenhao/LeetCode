# [Python/Java/TypeScript/Go] Stack simulation

> Author: Benhao
> Date: 2022-07-13
> Upvotes: 15
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
Use a stack to represent the asteroids remaining after collisions.
A collision first involves the last right-moving asteroid and the current left-moving asteroid.
The current asteroid may continue left, repeatedly colliding with and popping the stack top. This follows last-in, first-out order.
Other cases do not collide yet, so push them directly onto the stack.

### Code

```Python3 []
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            add = True
            # Only a new left-moving asteroid can collide with earlier ones; a new right-moving asteroid cannot
            if ast < 0:
                # Process right-moving asteroids at the stack top; any smaller than the current asteroid are destroyed
                while stack and stack[-1] > 0 and stack[-1] < -ast:
                    stack.pop()
                # If a right-moving asteroid remains, the current asteroid cannot destroy it
                if stack and stack[-1] > 0:
                    add = False
                    # Equal-sized asteroids both disappear
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
