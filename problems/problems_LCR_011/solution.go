package problemLCR_011

import (
	"encoding/json"
	"log"
	"strings"
)

func findMaxLength(nums []int) int {
	count := 0
	maxLength := 0
	table := map[int]int{0: -1}

	for i, num := range nums {
		if num == 0 {
			count--
		} else {
			count++
		}

		if index, ok := table[count]; ok {
			maxLength = max(maxLength, i-index)
		} else {
			table[count] = i
		}
	}

	return maxLength
}


func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return findMaxLength(nums)
}
