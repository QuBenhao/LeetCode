package problem3542

import (
	"encoding/json"
	"log"
	"strings"
)

func minOperations(nums []int) (ans int) {
	var minStack []int
	for _, num := range nums {
		// 左边每个更大的元素都需要一次操作，因为当前为割点
		for len(minStack) > 0 && num < minStack[len(minStack)-1] {
			minStack = minStack[:len(minStack)-1]
			ans++
		}
		if len(minStack) > 0 && num == minStack[len(minStack)-1] {
			continue
		}
		minStack = append(minStack, num)
	}
	if minStack[0] == 0 {
		ans--
	}
	return ans + len(minStack)
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return minOperations(nums)
}
