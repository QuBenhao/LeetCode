package problem3533

import (
	"encoding/json"
	"log"
	"slices"
	"sort"
	"strings"
)

func concatenatedDivisibility(nums []int, k int) []int {
	n := len(nums)
	sort.Ints(nums)
	pow10 := make([]int, n)
	for i := range n {
		pow10[i] = 1
		for num := nums[i]; num > 0; num /= 10 {
			pow10[i] *= 10
		}
	}
	mask := 1 << n
	cache := make([]map[int]bool, k)
	for i := range cache {
		cache[i] = make(map[int]bool, mask)
	}
	var ans []int
	var dfs func(s int, x int) bool
	dfs = func(s int, x int) bool {
		if res, ok := cache[x][s]; ok {
			return res
		}
		if s == 0 {
			cache[x][s] = x == 0
			return cache[x][s]
		}
		for i := range n {
			if ((s>>i)&1 == 1) && dfs(s^(1<<i), (x*pow10[i]+nums[i])%k) {
				cache[x][s] = true
				ans = append(ans, nums[i])
				return true
			}
		}
		cache[x][s] = false
		return false
	}
	if dfs(mask-1, 0) {
		slices.Reverse(ans)
		return ans
	}
	return []int{}
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return concatenatedDivisibility(nums, k)
}
