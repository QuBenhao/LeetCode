package problem2578

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func splitNum(num int) int {
	var nums []int
	for num > 0 {
		if r := num % 10; r != 0 {
			nums = append(nums, r)
		}
		num /= 10
	}
	sort.Ints(nums)
	var a, b int
	for i, v := range nums {
		if i&1 == 1 {
			b = b*10 + v
		} else {
			a = a*10 + v
		}
	}
	return a + b
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num int

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}

	return splitNum(num)
}
