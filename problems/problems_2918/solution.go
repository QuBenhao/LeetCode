package problem2918

import (
	"encoding/json"
	"log"
	"strings"
)

func minSum(nums1 []int, nums2 []int) int64 {
	var s1, s2 int64
	var c1, c2 int
	for _, num := range nums1 {
		s1 += int64(num)
		if num == 0 {
			s1++
			c1++
		}
	}
	for _, num := range nums2 {
		s2 += int64(num)
		if num == 0 {
			s2++
			c2++
		}
	}
	if (s1 < s2 && c1 == 0) || (s1 > s2 && c2 == 0) {
		return -1
	}
	return max(s1, s2)
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

	return minSum(nums1, nums2)
}
