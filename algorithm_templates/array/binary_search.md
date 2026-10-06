# Binary search

**Binary search relies on a two-part partition, not necessarily monotonic values. It applies when one part satisfies a property and the other does not.**

```python3
# bisect.bisect_left
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

```go
package main

func BinarySearch(arr []int, target int) int {
    left, right := 0, len(arr)-1
    for left <= right {
        mid := left + (right-left)/2
        if arr[mid] == target {
            return mid
        } else if arr[mid] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return -1
}
```

## Rotated array with duplicate elements

```go
package main

// One part satisfies < target, and the other does not
func binarySearch(nums []int, left, right, target int) int {
	l, r := left, right
	for l < r {
		mid := l + (r-l)/2
		if nums[mid] < target {
			l = mid + 1
		} else {
			r = mid
		}
	}
	if nums[r] == target {
		return r
	}
	return -1
}

func search(nums []int, target int) bool {
	n := len(nums)
	left, right := 0, n-1
	// Restore the two-part partition
	for left < right && nums[right] == nums[left] {
		right--
	}
	// One part satisfies >= nums[0], and the other does not
	for left < right {
		mid := left + (right-left+1)/2
		if nums[mid] >= nums[0] {
			left = mid
		} else {
			right = mid - 1
		}
	}
	idx := n
	if nums[right] >= nums[0] && right < n-1 {
		idx = right + 1
	}
	if target >= nums[0] {
		return binarySearch(nums, 0, idx-1, target) != -1
	} else {
		return binarySearch(nums, idx, n-1, target) != -1
	}
}
```
