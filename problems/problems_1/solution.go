package problem1

import (
	"encoding/json"
	"log"
	"strings"
)

func twoSum(nums []int, target int) []int {
	m := map[int]int{}
	for i, num := range nums {
		d := target - num
		if idx, ok := m[d]; ok {
			return []int{idx, i}
		}
		m[num] = i
	}
	return nil
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int
	var target int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &target); err != nil {
		log.Fatal(err)
	}

	return twoSum(nums, target)
}
