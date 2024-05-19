# 227. Basic Calculator II

Given a string `s` which represents an expression, *evaluate this expression and return its value*. 

The integer division should truncate toward zero.

 

**Example 1:**

```
Input: s = "3+2*2"
Output: 7
```

**Example 2:**

```
Input: s = " 3/2 "
Output: 1
```

**Example 3:**

```
Input: s = " 3+5 / 2 "
Output: 5
```

 

**Constraints:**

- 1 <= s.length <= 3 * 10<sup>5</sup>
- `s` consists of integers and operators `('+', '-', '*', '/')` separated by some number of spaces.
- `s` represents **a valid expression**.
- All the integers in the expression are non-negative integers in the range [0, 2<sup>31</sup> - 1].
- The answer is **guaranteed** to fit in a **32-bit integer**.

