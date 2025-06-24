package problem2040

import (
	"encoding/json"
	"log"
	"strings"
)

func kthSmallestProduct(nums1 []int, nums2 []int, k int64) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums1 []int
	var nums2 []int
	var k int64

	if err := json.Unmarshal([]byte(inputValues[0]), &nums1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &nums2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return kthSmallestProduct(nums1, nums2, k)
}
