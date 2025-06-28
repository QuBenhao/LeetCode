package problem1498

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

const mod = 1e9 + 7

func numSubseq(nums []int, target int) (ans int) {
	sort.Ints(nums)
	n := len(nums)
	powers := make([]int, n)
	powers[0] = 1
	for i := 1; i < n; i++ {
		powers[i] = (powers[i-1] * 2) % mod
	}
	left, right := 0, n-1
	for left <= right {
		for right >= left && nums[left]+nums[right] > target {
			right--
		}
		if right < left {
			break
		}
		ans = (ans + powers[right-left]) % mod
		left++
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var target int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return numSubseq(nums, target)
}
