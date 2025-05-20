package problem283

import (
	"encoding/json"
	"log"
	"strings"
)

func moveZeroes(nums []int) {
	for idx, i := 0, 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[idx], nums[i] = nums[i], nums[idx]
			idx++
		}
	}
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	moveZeroes(nums)
	return nums
}
