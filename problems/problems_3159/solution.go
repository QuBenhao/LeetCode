package problem3159

import (
	"encoding/json"
	"log"
	"strings"
)

func occurrencesOfElement(nums []int, queries []int, x int) []int {
	var idxes []int
	for i, num := range nums {
		if num == x {
			idxes = append(idxes, i)
		}
	}
	ans := make([]int, len(queries))
	for i, query := range queries {
		if query > len(idxes) {
			ans[i] = -1
			continue
		}
		ans[i] = idxes[query-1]
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var queries []int
	var x int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &x); err != nil {
		log.Fatal(err)
	}

	return occurrencesOfElement(nums, queries, x)
}
