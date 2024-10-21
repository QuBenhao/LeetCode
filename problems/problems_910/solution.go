package problem910

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func smallestRangeII(nums []int, k int) int {
	slices.Sort(nums)
	n := len(nums)
	ans := nums[n-1] - nums[0]
	for i := 1; i < n; i++ {
		mx := max(nums[i-1]+k, nums[n-1]-k)
		mn := min(nums[0]+k, nums[i]-k)
		ans = min(ans, mx-mn)
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return smallestRangeII(nums, k)
}
