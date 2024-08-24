package problemLCR_089

import (
	"encoding/json"
	"log"
	"strings"
)

func rob(nums []int) int {
	dpNotRob, dpRob := 0, nums[0]
	for i := 1; i < len(nums); i++ {
		dpNotRob, dpRob = max(dpNotRob, dpRob), dpNotRob+nums[i]
	}
	return max(dpNotRob, dpRob)
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return rob(nums)
}
