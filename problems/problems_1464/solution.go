package problem1464

import (
	"encoding/json"
	"log"
	"strings"
)

func maxProduct(nums []int) int {
	max1, max2 := 0, 0
	for _, num := range nums {
		if num > max1 {
			max2 = max1
			max1 = num
		} else if num > max2 {
			max2 = num
		}
	}
	return (max1 - 1) * (max2 - 1)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maxProduct(nums)
}
