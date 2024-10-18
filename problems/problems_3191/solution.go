package problem3191

import (
	"encoding/json"
	"log"
	"strings"
)

func minOperations(nums []int) (ans int) {
	n := len(nums)
	for i := 0; i < n-2; i++ {
		if nums[i] == 0 {
			ans++
			nums[i+1] ^= 1
			nums[i+2] ^= 1
		}
	}
	if nums[n-2] == 1 && nums[n-1] == 1 {
		return ans
	}
	return -1
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return minOperations(nums)
}
