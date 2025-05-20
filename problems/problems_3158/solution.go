package problem3158

import (
	"encoding/json"
	"log"
	"strings"
)

func duplicateNumbersXOR(nums []int) (ans int) {
	explored := make(map[int]bool)
	for _, num := range nums {
		if explored[num] {
			ans ^= num
		} else {
			explored[num] = true
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return duplicateNumbersXOR(nums)
}
