package problem3040

import (
	"encoding/json"
	"log"
	"strings"
)

func maxOperations(nums []int) int {
	n := len(nums)
	res1, done := helper(nums[2:], nums[0]+nums[1]) // Remove the first two numbers
	if done {
		return n / 2
	}
	res2, done := helper(nums[:n-2], nums[n-2]+nums[n-1]) // Remove the last two numbers
	if done {
		return n / 2
	}
	res3, done := helper(nums[1:n-1], nums[0]+nums[n-1]) // Remove the first and last numbers
	if done {
		return n / 2
	}
	return max(res1, res2, res3) + 1 // Include the first operation
}

func helper(a []int, target int) (res int, done bool) {
	n := len(a)
	memo := make([][]int, n)
	for i := range memo {
		memo[i] = make([]int, n)
		for j := range memo[i] {
			memo[i][j] = -1 // -1 means not yet computed
		}
	}
	var dfs func(int, int) int
	dfs = func(i, j int) (res int) {
		if done {
			return
		}
		if i >= j {
			done = true
			return
		}
		p := &memo[i][j]
		if *p != -1 { // Already computed
			return *p
		}
		if a[i]+a[i+1] == target { // Remove the first two numbers
			res = max(res, dfs(i+2, j)+1)
		}
		if a[j-1]+a[j] == target { // Remove the last two numbers
			res = max(res, dfs(i, j-2)+1)
		}
		if a[i]+a[j] == target { // Remove the first and last numbers
			res = max(res, dfs(i+1, j-1)+1)
		}
		*p = res // Memoization
		return
	}
	res = dfs(0, n-1)
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maxOperations(nums)
}
