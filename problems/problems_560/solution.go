package problem560

import (
	"encoding/json"
	"log"
	"strings"
)

func subarraySum(nums []int, k int) (ans int) {
	counter := map[int]int{0: 1}
	s := 0
	for _, num := range nums {
		s += num
		ans += counter[s-k]
		counter[s]++
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return subarraySum(nums, k)
}
