package problem2956

import (
	"encoding/json"
	"log"
	"strings"
)

func findIntersectionValues(nums1 []int, nums2 []int) []int {
	ans := make([]int, 2)
	counter := make(map[int]int)
	for _, num := range nums2 {
		counter[num]++
	}
	for _, num := range nums1 {
		if v, ok := counter[num]; ok {
			ans[0]++
			ans[1] += v
			counter[num] = 0
		}
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums1 []int
	var nums2 []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &nums2); err != nil {
		log.Fatal(err)
	}

	return findIntersectionValues(nums1, nums2)
}
