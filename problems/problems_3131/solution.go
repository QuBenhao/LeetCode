package problem3131

import (
	"encoding/json"
	"log"
	"strings"
)

func addedInteger(nums1 []int, nums2 []int) int {
	m1, m2 := nums1[0], nums2[0]
	for _, v := range nums1 {
		m1 = min(m1, v)
	}
	for _, v := range nums2 {
		m2 = min(m2, v)
	}
	return m2 - m1
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

	return addedInteger(nums1, nums2)
}
