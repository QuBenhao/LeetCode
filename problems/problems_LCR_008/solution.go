package problemLCR_008

import (
	"encoding/json"
	"log"
	"strings"
)

func minSubArrayLen(target int, nums []int) int {
	n := len(nums)
	ans := n + 1
	var queue []int
	curSum := 0
	for _, num := range nums {
		queue = append(queue, num)
		curSum += num
		for curSum >= target {
			ans = min(ans, len(queue))
			curSum -= queue[0]
			queue = queue[1:]
		}
	}
	if ans == n+1 {
		return 0
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var target int
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &target); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &nums); err != nil {
		log.Fatal(err)
	}

	return minSubArrayLen(target, nums)
}
