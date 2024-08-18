package problem128

import (
	"encoding/json"
	"log"
	"strings"
)

func longestConsecutive(nums []int) (ans int) {
	lengthMap := map[int]int{}
	for _, num := range nums {
		if _, ok := lengthMap[num]; ok {
			continue
		}
		left, right := 0, 0
		if l, ok := lengthMap[num-1]; ok {
			left = l
		}
		if r, ok := lengthMap[num+1]; ok {
			right = r
		}
		length := left + right + 1
		ans = max(ans, length)
		lengthMap[num] = length
		lengthMap[num-left] = length
		lengthMap[num+right] = length
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return longestConsecutive(nums)
}
