package problem3194

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func minimumAverage(nums []int) float64 {
	sort.Ints(nums)
	n := len(nums)
	ans := nums[0] + nums[n-1]
	for i := 1; i < n/2; i++ {
		ans = min(ans, nums[n-1-i]+nums[i])
	}
	return float64(ans) / 2
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return minimumAverage(nums)
}
