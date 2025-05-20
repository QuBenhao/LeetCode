package problem80

import (
	"encoding/json"
	"log"
	"strings"
)

func removeDuplicates(nums []int) (idx int) {
	n := len(nums)
	for i, j := 0, 0; j < n; {
		for j < n && nums[i] == nums[j] {
			j++
		}
		for k := 0; k < min(j-i, 2); k++ {
			nums[idx] = nums[i]
			idx++
		}
		i = j
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return nums[:removeDuplicates(nums)]
}
