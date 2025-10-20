package problem3346

import (
	"encoding/json"
	"log"
	"maps"
	"slices"
	"strings"
)

func maxFrequency(nums []int, k, numOperations int) (ans int) {
	cnt := map[int]int{}
	diff := map[int]int{}
	for _, x := range nums {
		cnt[x]++
		diff[x] += 0 // 把 x 插入 diff，以保证下面能遍历到 x
		diff[x-k]++  // 把 [x-k, x+k] 中的每个整数的出现次数都加一
		diff[x+k+1]--
	}

	sumD := 0
	for _, x := range slices.Sorted(maps.Keys(diff)) {
		sumD += diff[x]
		ans = max(ans, min(sumD, cnt[x]+numOperations))
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int
	var numOperations int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &numOperations); err != nil {
		log.Fatal(err)
	}

	return maxFrequency(nums, k, numOperations)
}
