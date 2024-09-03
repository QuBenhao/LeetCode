package problem4

import (
	"encoding/json"
	"log"
	"strings"
)

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {

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

	return findMedianSortedArrays(nums1, nums2)
}
