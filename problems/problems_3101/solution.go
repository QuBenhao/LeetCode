package problem3101

import (
	"encoding/json"
	"log"
	"strings"
)

func countAlternatingSubarrays(nums []int) (ans int64) {
	var cnt int64
	for i, num := range nums {
		if i == 0 || num != nums[i-1] {
			cnt++
		} else {
			cnt = 1
		}
		ans += cnt
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return countAlternatingSubarrays(nums)
}
