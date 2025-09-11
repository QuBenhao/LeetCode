# 排列组合

## 全排列

```python3
def permute(nums):
    ans = []

    def dfs(x):
        if x == len(nums) - 1:
            ans.append(list(nums))
            return
        for i in range(x, len(nums)):
            nums[i], nums[x] = nums[x], nums[i]
            dfs(x + 1)
            nums[i], nums[x] = nums[x], nums[i]

    dfs(0)
    return ans
```

```go
package main

func permute(nums []int) (ans [][]int) {
	var backtrack func(int)
	backtrack = func(idx int) {
		if idx == len(nums) {
			tmp := make([]int, len(nums))
			copy(tmp, nums)
			ans = append(ans, tmp)
			return
		}
		for i := idx; i < len(nums); i++ {
			nums[i], nums[idx] = nums[idx], nums[i]
			backtrack(idx + 1)
			nums[i], nums[idx] = nums[idx], nums[i]
		}
	}
	backtrack(0)
	return
}
```

### 重复元素全排列

```python3
def next_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    left, right = i + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    if i < 0:
        return
    j = i + 1
    while j < n and arr[j] <= arr[i]:
        j += 1
    arr[i], arr[j] = arr[j], arr[i]
```

```go
package main

func NextPermutation(nums []int) {
	n := len(nums)
	i := n - 2
	for i >= 0 && nums[i] >= nums[i+1] {
		i--
	}
	for l, r := i+1, n-1; l < r; l, r = l+1, r-1 {
		nums[l], nums[r] = nums[r], nums[l]
	}
	if i < 0 {
		return
	}
	j := i + 1
	for j < n && nums[j] <= nums[i] {
		j++
	}
	nums[i], nums[j] = nums[j], nums[i]
}
```

## 组合

```python3
def combination_sum(candidates, target: int):
    candidates.sort()
    ans = []
    path = []

    def dfs(x, s):
        if s == 0:
            ans.append(list(path))
            return
        if x < 0 or s < 0:
            return
        # 不选当前
        dfs(x - 1, s)
        # 选当前
        path.append(candidates[x])
        dfs(x, s - candidates[x])
        path.pop()

    dfs(len(candidates) - 1, target)
    return ans
```

```go
func combinationSum(candidates []int, target int) (ans [][]int) {
	var dfs func([]int, int, int)
	dfs = func(path []int, idx int, s int) {
		if s == 0 {
			ans = append(ans, append([]int(nil), path...))
			return
		}
		if idx == len(candidates) {
			return
		}
		if candidates[idx] <= s {
			path = append(path, candidates[idx])
			dfs(path, idx, s-candidates[idx])
			path = path[:len(path)-1]
		}
		dfs(path, idx+1, s)
	}

	dfs([]int{}, 0, target)
	return
}
```

### 重复元素组合

```python3
def combination_sum2(candidates, target: int):
    ans = []
    path = []
    candidates.sort()
    n = len(candidates)

    def backtrack(idx, remain):
        if remain < 0:
            return
        if not remain:
            ans.append(list(path))
            return
        if idx == n:
            return
        path.append(candidates[idx])
        backtrack(idx + 1, remain - candidates[idx])
        path.pop()
        nxt = idx + 1
        while nxt < n and candidates[nxt] == candidates[nxt - 1]:
            nxt += 1
        backtrack(nxt, remain)

    backtrack(0, target)
    return ans
```

```go
func combinationSum2(candidates []int, target int) (ans [][]int) {
	sort.Ints(candidates)
	n := len(candidates)
	var backtrack func(idx int, remain int, path []int)
	backtrack = func(idx, remain int, path []int) {
		if remain < 0 {
			return
		}
		if remain == 0 {
			cp := make([]int, len(path))
			copy(cp, path)
			ans = append(ans, cp)
			return
		}
		if idx == n {
			return
		}
		path = append(path, candidates[idx])
		backtrack(idx+1, remain-candidates[idx], path)
		path = path[:len(path)-1]
		nxt := idx + 1
		for nxt < n && candidates[nxt] == candidates[nxt-1] {
			nxt++
		}
		backtrack(nxt, remain, path)
	}
	backtrack(0, target, make([]int, 0))
	return
}
```

### 重复元素子集

```go
func subsetsWithDup(nums []int) (ans [][]int) {
	sort.Ints(nums)
	n := len(nums)
	path := []int{}

	var backtrack func(idx int)
	backtrack = func(idx int) {
		if idx == n {
			cp := make([]int, len(path))
			copy(cp, path)
			ans = append(ans, cp)
			return
		}
		path = append(path, nums[idx])
		backtrack(idx + 1)
		path = path[:len(path)-1]
		nxt := idx + 1
		for nxt < n && nums[nxt] == nums[idx] {
			nxt++
		}
		backtrack(nxt)
	}
	backtrack(0)
	return
}
```
