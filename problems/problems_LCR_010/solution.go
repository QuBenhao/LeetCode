package problemLCR_010

import (
	"encoding/json"
	"log"
	"strings"
)

func subarraySum(nums []int, k int) (ans int) {
	counter := map[int]int{0: 1}
	sum := 0
	for _, num := range nums {
		sum += num
		ans += counter[sum-k]
		counter[sum]++
	}
	return
}

func Solve(inputJsonValues string) interface{} {
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
