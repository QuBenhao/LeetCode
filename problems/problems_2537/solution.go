package problem2537

import (
	"encoding/json"
	"log"
	"strings"
)

func countGood(nums []int, k int) (ans int64) {
	counter := map[int]int{}
	left, pairs := 0, 0
	for _, num := range nums {
		pairs += counter[num]
		counter[num]++
		for pairs >= k {
			counter[nums[left]]--
			pairs -= counter[nums[left]]
			left++
		}
		// 以当前num为右端点，0~left为左端点的子数组均满足条件
		ans += int64(left)
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

	return countGood(nums, k)
}
