package problem2860

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func countWays(nums []int) (ans int) {
	sort.Ints(nums)
	ans = 1
	if nums[0] > 0 {
		ans++
	}
	for i, n := 1, len(nums); i < n; i++ {
		if nums[i-1] < i && nums[i] > i {
			ans++
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return countWays(nums)
}
