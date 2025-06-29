package problem594

import (
	"encoding/json"
	"log"
	"strings"
)

func findLHS(nums []int) (ans int) {
	counts := make(map[int]int)
	for _, num := range nums {
		counts[num]++
	}
	for num, count := range counts {
		if count2, ok := counts[num+1]; ok {
			if count+count2 > ans {
				ans = count + count2
			}
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

	return findLHS(nums)
}
