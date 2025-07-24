package problem3487

import (
	"encoding/json"
	"log"
	"strings"
)

func maxSum(nums []int) int {
	explored := make(map[int]bool)
	sum := 0
	mx := -101
	for _, num := range nums {
		if !explored[num] {
			explored[num] = true
			if num > mx {
				mx = num
			}
			if num > 0 {
				sum += num
			}
		}
	}
	if mx > 0 {
		return sum
	}
	return mx
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maxSum(nums)
}
