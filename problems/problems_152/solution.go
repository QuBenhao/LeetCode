package problem152

import (
	"encoding/json"
	"log"
	"strings"
)

func maxProduct(nums []int) int {
	ans := nums[0]
	maxF, minF := nums[0], nums[0]
	for i := 1; i < len(nums); i++ {
		maxF, minF = max(max(maxF*nums[i], minF*nums[i]), nums[i]), min(min(maxF*nums[i], minF*nums[i]), nums[i])
		ans = max(ans, maxF)
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maxProduct(nums)
}
