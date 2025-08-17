package problem3649

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func perfectPairs(nums []int) (ans int64) {
	absNums := make([]int, len(nums))
	for i, num := range nums {
		if num < 0 {
			num = -num
		}
		absNums[i] = num
	}
	sort.Ints(absNums)
	n := len(absNums)
	l := 0
	for r := 1; r < n; r++ {
		for absNums[l]*2 < absNums[r] {
			l++
		}
		ans += int64(r - l)
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return perfectPairs(nums)
}
