package problem496

import (
	"encoding/json"
	"log"
	"strings"
)

func nextGreaterElement(nums1 []int, nums2 []int) []int {
	ans := make([]int, len(nums1))
	idxMap := make(map[int]int)
	var stack []int
	for i, num := range nums1 {
		idxMap[num] = i
		ans[i] = -1
	}
	for _, num := range nums2 {
		for len(stack) > 0 && stack[len(stack)-1] < num {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if idx, exists := idxMap[top]; exists {
				ans[idx] = num
			}
		}
		stack = append(stack, num)
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums1 []int
	var nums2 []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &nums2); err != nil {
		log.Fatal(err)
	}

	return nextGreaterElement(nums1, nums2)
}
