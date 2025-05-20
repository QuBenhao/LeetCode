package problem2779

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumBeauty(nums []int, k int) (ans int) {
	m := 0
	for _, num := range nums {
		m = max(m, num)
	}
	diff := make([]int, m+2)
	for _, num := range nums {
		diff[max(0, num-k)]++
		diff[min(m+1, num+k+1)]--
	}
	cur := 0
	for _, v := range diff {
		cur += v
		ans = max(ans, cur)
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maximumBeauty(nums, k)
}
