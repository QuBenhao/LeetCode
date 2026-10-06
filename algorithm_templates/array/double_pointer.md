# Two pointers

- The two-pointer technique is commonly used for array or linked-list problems, such as detecting cycles with **fast and slow pointers** and solving sorted-array problems with **left and right pointers**.

## Example: remove an element in place

```python
def remove_element(nums, val):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

```go
package main

func removeElement(nums []int, val int) int {
    slow := 0
    for fast := 0; fast < len(nums); fast++ {
        if nums[fast] != val {
            nums[slow] = nums[fast]
            slow++
        }
    }
    return slow
}
```

## Example: two sum in a sorted array

```python
def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left + 1, right + 1]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []
```

```go
package main

func twoSum(nums []int, target int) []int {
    left, right := 0, len(nums)-1
    for left < right {
        sum := nums[left] + nums[right]
        if sum == target {
            return []int{left+1, right+1}
        } else if sum < target {
            left++
        } else {
            right--
        }
    }
    return []int{}
}
```
