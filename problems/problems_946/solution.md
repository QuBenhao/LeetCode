# [Python/Java/TypeScript/Go/C++/C#/Js/PHP] 栈模拟

> Author: Benhao
> Date: 2022-08-30
> Upvotes: 26
> Tags: C++, C#, Go, Java, JavaScript, PHP, Python, Python3, TypeScript

---

### 解题思路
注意到本题的一个关键条件**值不重复**，
那么我们在添加元素时，直接根据当前弹出位置的值判断是否需要弹出，如果和栈顶元素一直需要一直弹出(因为如果再添加任何一个值，下一个弹出不可能再是这个值了)。
返回是否全部弹出即可。

### 代码

```Python3 []
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num)
            while stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return i == len(popped)
```
```Java []
class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        Deque<Integer> stack = new ArrayDeque<>();
        int i = 0;
        for (int num: pushed) {
            stack.addLast(num);
            while (!stack.isEmpty() && stack.peekLast() == popped[i]) {
                stack.removeLast();
                i++;
            }
        }
        return i == popped.length;
    }
}
```
```TypeScript []
function validateStackSequences(pushed: number[], popped: number[]): boolean {
    const stack: Array<number> = new Array<number>()
    let i: number = 0
    for (const num of pushed) {
        stack.push(num)
        while (stack.length > 0 && stack[stack.length - 1] == popped[i]) {
            stack.pop()
            i++
        }
    }
    return i == popped.length
};
```
```Go []
func validateStackSequences(pushed []int, popped []int) bool {
    stack, i := []int{}, 0
    for _, num := range pushed {
        stack = append(stack, num)
        for len(stack) > 0 && stack[len(stack) - 1] == popped[i] {
            stack = stack[:len(stack) - 1]
            i++
        }
    }
    return i == len(popped)
}
```
```C++ []
class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> st;
        int j = 0, n = pushed.size();
        for (int i = 0; i < n; i++) {
            st.emplace(pushed[i]);
            while (st.size() > 0 && st.top() == popped[j]) {
                st.pop();
                j++;
            }
        }
        return j == n;
    }
};
```
```C# []
public class Solution {
    public bool ValidateStackSequences(int[] pushed, int[] popped) {
        Stack<int> stack = new Stack<int>();
        int i = 0;
        foreach (int num in pushed) {
            stack.Push(num);
            while (stack.Count > 0 && stack.Peek() == popped[i]) {
                stack.Pop();
                i++;
            }
        }
        return i == popped.Length;
    }
}
```
```JavaScript []
/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function(pushed, popped) {
    const stack = new Array()
    let i = 0
    for (const num of pushed) {
        stack.push(num)
        while (stack.length > 0 && stack[stack.length - 1] === popped[i]) {
            stack.pop()
            i++
        }
    }
    return i === popped.length
};
```
```PHP []
class Solution {

    /**
     * @param Integer[] $pushed
     * @param Integer[] $popped
     * @return Boolean
     */
    function validateStackSequences($pushed, $popped) {
        $stack = [];
        for ($i = 0, $j = 0; $i < count($pushed); $i++) {
            array_push($stack, $pushed[$i]);
            while (count($stack) > 0 && $stack[count($stack) - 1] == $popped[$j]) {
                array_pop($stack);
                $j++;
            }
        }
        return count($stack) == 0;
    }
}
```
```Python []
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack, i = [], 0
        for num in pushed:
            stack.append(num)
            while stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return i == len(popped)
```