package problem3584

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func maximumProduct(nums []int, m int) (ans int64) {
	n := len(nums)
	preMin := make([]int, n)
	preMax := make([]int, n)
	preMin[0] = nums[0]
	preMax[0] = nums[0]
	ans = math.MinInt64
	for i, num := range nums {
		if i > 0 {
			preMin[i] = min(preMin[i-1], num)
			preMax[i] = max(preMax[i-1], num)
		}
		if i >= m-1 {
			ans = max(ans, int64(preMax[i+1-m])*int64(num), int64(preMin[i+1-m])*int64(num))
		}
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var m int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &m); err != nil {
		log.Fatal(err)
	}

	return maximumProduct(nums, m)
}
