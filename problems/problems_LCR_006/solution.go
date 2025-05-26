package problemLCR_006

import (
	"encoding/json"
	"log"
	"strings"
)

func twoSum(numbers []int, target int) []int {
	left, right := 0, len(numbers)-1
	for left < right {
		cur := numbers[left] + numbers[right]
		if cur == target {
			break
		} else if cur < target {
			left++
		} else {
			right--
		}
	}
	return []int{left, right}
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var numbers []int
	var target int

	if err := json.Unmarshal([]byte(inputValues[0]), &numbers); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return twoSum(numbers, target)
}
