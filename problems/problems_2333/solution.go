package problem2333

import (
	"encoding/json"
	"log"
	"strings"
)

func minSumSquareDiff(nums1 []int, nums2 []int, k1 int, k2 int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums1 []int
	var nums2 []int
	var k1 int
	var k2 int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &nums2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &k2); err != nil {
		log.Fatal(err)
	}

	return minSumSquareDiff(nums1, nums2, k1, k2)
}
