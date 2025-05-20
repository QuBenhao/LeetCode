package problem896

import (
	"encoding/json"
	"log"
	"strings"
)

func isMonotonic(nums []int) bool {
	for i, inc, dec := 0, false, false; i < len(nums)-1; i++ {
		if nums[i] < nums[i+1] {
			if dec {
				return false
			}
			inc = true
		} else if nums[i] > nums[i+1] {
			if inc {
				return false
			}
			dec = true
		}
	}
	return true
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return isMonotonic(nums)
}
