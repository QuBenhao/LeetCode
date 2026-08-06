# [Python/Java/JavaScript/Go] 栈应用

> slug: pythonjavajavascriptgo-by-himymben-os66
> date: 2022-04-15
> tags: Go, Java, JavaScript, Python, Python3
> question: Mini Parser (mini-parser)
> url: https://leetcode.cn/problems/mini-parser/solutions/RdMgHh/pythonjavajavascriptgo-by-himymben-os66/

---
### 解题思路
本题和实现计算器异曲同工，使用栈维护计算顺序。

### 代码

```Python3 []
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # 纯数字
        if s[0] != '[':
            return NestedInteger(int(s))
        stack, curVal, sign = [], 0, False
        for i, c in enumerate(s):
            match c:
                case '[':
                    # 递归嵌套
                    stack.append(NestedInteger())
                case '-':
                    # 数字符号
                    sign = True
                case ',':
                    # 只有上一个字符是数字才加入了新的数字，否则可能是 "],"
                    if s[i - 1].isdigit():
                        stack[-1].add(NestedInteger(-curVal if sign else curVal))
                    curVal, sign = 0, False
                case ']':
                    # 只有上一个字符是数字才加入了新的数字，否则可能是 "[]"
                    if s[i - 1].isdigit():
                        stack[-1].add(NestedInteger(-curVal if sign else curVal))
                    # 弹出栈，并将当前的对象加入嵌套的列表中
                    if len(stack) > 1:
                        cur = stack.pop()
                        stack[-1].add(cur)
                    curVal, sign = 0, False
                case _:
                    # 数字计算
                    curVal = curVal * 10 + int(c)
        return stack.pop()
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
```
```Java []
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
class Solution {
    public NestedInteger deserialize(String s) {
        if(s.charAt(0) != '[')
            return new NestedInteger(Integer.parseInt(s));
        Deque<NestedInteger> stack = new ArrayDeque<>();
        int curVal = 0, sign = 1;
        for(int i = 0; i < s.length(); i++) {
            switch(s.charAt(i)) {
                case '[':
                    stack.addLast(new NestedInteger());
                    break;
                case '-':
                    sign = -1;
                    break;
                case ',':
                case ']':
                    if('0' <= s.charAt(i - 1) && s.charAt(i - 1) <= '9') {
                        stack.peekLast().add(new NestedInteger(sign * curVal));
                        sign = 1;
                        curVal = 0;
                    }
                    if(s.charAt(i) == ']' && stack.size() > 1) {
                        NestedInteger ni = stack.pollLast();
                        stack.peekLast().add(ni);
                    }
                    break;
                default:
                    curVal = 10 * curVal + (s.charAt(i) - '0');
            }
        }
        return stack.pollLast();
    }
}
```
```JavaScript []
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * function NestedInteger() {
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     @return {boolean}
 *     this.isInteger = function() {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     @return {integer}
 *     this.getInteger = function() {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a single integer equal to value.
 *     @return {void}
 *     this.setInteger = function(value) {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
 *     @return {void}
 *     this.add = function(elem) {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds, if it holds a nested list
 *     Return null if this NestedInteger holds a single integer
 *     @return {NestedInteger[]}
 *     this.getList = function() {
 *         ...
 *     };
 * };
 */
/**
 * @param {string} s
 * @return {NestedInteger}
 */
var deserialize = function(s) {
    if(s.charCodeAt(0) != '['.charCodeAt(0)) {
        const ni = new NestedInteger()
        ni.setInteger(Number.parseInt(s))
        return ni
    }
    const stack = new Array()
    let curVal = 0, sign = 1
    for(let i = 0; i < s.length; i++) {
        switch(s.charCodeAt(i)) {
            case '['.charCodeAt(0):
                stack.push(new NestedInteger())
                break
            case ','.charCodeAt(0):
            case ']'.charCodeAt(0):
                if('0'.charCodeAt(0) <= s.charCodeAt(i - 1) && s.charCodeAt(i - 1) <= '9'.charCodeAt(0)) {
                    stack[stack.length - 1].add(new NestedInteger(sign * curVal))
                    curVal = 0
                    sign = 1
                }
                if(s.charCodeAt(i) == ']'.charCodeAt(0) && stack.length > 1) {
                    const cur = stack.pop()
                    stack[stack.length - 1].add(cur)
                }
                break
            case '-'.charCodeAt(0):
                sign = -1
                break
            default:
                curVal = 10 * curVal + s.charCodeAt(i) - '0'.charCodeAt(0)
        }
    }
    return stack.pop()
};
```
```Go []
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * type NestedInteger struct {
 * }
 *
 * // Return true if this NestedInteger holds a single integer, rather than a nested list.
 * func (n NestedInteger) IsInteger() bool {}
 *
 * // Return the single integer that this NestedInteger holds, if it holds a single integer
 * // The result is undefined if this NestedInteger holds a nested list
 * // So before calling this method, you should have a check
 * func (n NestedInteger) GetInteger() int {}
 *
 * // Set this NestedInteger to hold a single integer.
 * func (n *NestedInteger) SetInteger(value int) {}
 *
 * // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 * func (n *NestedInteger) Add(elem NestedInteger) {}
 *
 * // Return the nested list that this NestedInteger holds, if it holds a nested list
 * // The list length is zero if this NestedInteger holds a single integer
 * // You can access NestedInteger's List element directly if you want to modify it
 * func (n NestedInteger) GetList() []*NestedInteger {}
 */
func deserialize(s string) *NestedInteger {
    if s[0] != '[' {
        i, _ := strconv.Atoi(s)
        ni := &NestedInteger{}
        ni.SetInteger(i)
        return ni
    }
    stack, curVal, sign := []*NestedInteger{}, 0, 1
    for i := 0; i < len(s); i++ {
        if s[i] == '[' {
            stack = append(stack, &NestedInteger{})
        } else if s[i] == ',' || s[i] == ']' {
            if '0' <= s[i - 1] && s[i - 1] <= '9' {
                ni := &NestedInteger{}
                ni.SetInteger(curVal * sign)
                stack[len(stack)-1].Add(*ni)
                curVal, sign = 0, 1
            }
            if l := len(stack); s[i] == ']' && l > 1 {
                stack[l - 2].Add(*stack[l - 1])
                stack = stack[:l - 1]
            }
        } else if s[i] == '-' {
            sign = -1
        } else {
            curVal = curVal * 10 + int(s[i] - '0')
        }
    }
    return stack[0]
}
```