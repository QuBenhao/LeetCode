package problem2708

import (
	"encoding/json"
	"log"
	"strings"
)

func maxStrength(nums []int) int64 {
	mx, mn := int64(nums[0]), int64(nums[0])
	for i := 1; i < len(nums); i++ {
		tmp, num := mx, int64(nums[i])
		mx = max(max(max(num, num*mx), num*mn), mx)
		mn = min(min(min(num, num*tmp), num*mn), mn)
	}
	return mx
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maxStrength(nums)
}
