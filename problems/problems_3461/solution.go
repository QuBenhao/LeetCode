package problem3461

import (
	"encoding/json"
	"log"
	"strings"
)

func hasSameDigits(s string) bool {
	nums := make([]int, len(s))
	for i, r := range s {
		nums[i] = int(r - '0')
	}
	for n := len(nums); n > 2; n = len(nums) {
		for i := range n - 1 {
			nums[i] = (nums[i] + nums[i+1]) % 10
		}
		nums = nums[:n-1]
	}
	return nums[0] == nums[1]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return hasSameDigits(s)
}
