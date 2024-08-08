package problem3132

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumAddedInteger(nums1 []int, nums2 []int) int {

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

	return minimumAddedInteger(nums1, nums2)
}
