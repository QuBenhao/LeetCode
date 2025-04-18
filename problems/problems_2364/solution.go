package problem2364

import (
	"encoding/json"
	"log"
	"strings"
)

func countBadPairs(nums []int) (ans int64) {
	n := len(nums)
	cnt := make(map[int]int)
	for i, num := range nums {
		cnt[num-i]++
	}
	for _, v := range cnt {
		ans += int64(v) * int64(n-v)
	}
	ans /= 2
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return countBadPairs(nums)
}
