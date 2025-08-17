package problem3654

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minArraySum(nums []int, k int) (cur int64) {
	g := make([]int64, k)
	for i := range g {
		g[i] = math.MaxInt64
	}
	g[0] = 0
	mod := 0
	for _, num := range nums {
		mod = (mod + num) % k
		cur = min(cur+int64(num), g[mod])
		g[mod] = cur
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

	return minArraySum(nums, k)
}
