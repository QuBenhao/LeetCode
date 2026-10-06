# Monotonic stack

## When to use a monotonic stack

A monotonic stack finds the first greater or smaller element to the left or right of each element in $`O(n)`$ time.

A monotonic stack is commonly used for the following problems:

- Find the first element to the left that is greater than the current element.
- Find the first element to the left that is smaller than the current element.
- Find the first element to the right that is greater than the current element.
- Find the first element to the right that is smaller than the current element.

```python3
def solve(nums):
    max_stack = []
    for i, num in enumerate(nums):
        while max_stack and num > nums[max_stack[-1]]:
            max_stack.pop()
        max_stack.append(i)
```

```go
package main

func subArrayRanges(nums []int) (ans int64) {
	n := len(nums)
	minStack, maxStack := make([]int, 0, n), make([]int, 0, n)
	for i := 0; i <= n; i++ {
		for len(maxStack) > 0 && (i == n || nums[i] > nums[maxStack[len(maxStack)-1]]) {
			j := maxStack[len(maxStack)-1]
			maxStack = maxStack[:len(maxStack)-1]
			left := -1
			if len(maxStack) > 0 {
				left = maxStack[len(maxStack)-1]
			}
			ans += int64(nums[j]) * int64(j-left) * int64(i-j)
		}
		maxStack = append(maxStack, i)
		for len(minStack) > 0 && (i == n || nums[i] < nums[minStack[len(minStack)-1]]) {
			j := minStack[len(minStack)-1]
			minStack = minStack[:len(minStack)-1]
			left := -1
			if len(minStack) > 0 {
				left = minStack[len(minStack)-1]
			}
			ans -= int64(nums[j]) * int64(j-left) * int64(i-j)
		}
		minStack = append(minStack, i)
	}
	return
}
```
