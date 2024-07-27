package problem2740

import (
	"encoding/json"
	"log"
	"math"
	"sort"
	"strings"
)

func findValueOfPartition(nums []int) int {
	sort.Ints(nums)
	ans := math.MaxInt
	for i := 1; i < len(nums); i++ {
		ans = min(ans, nums[i]-nums[i-1])
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return findValueOfPartition(nums)
}
