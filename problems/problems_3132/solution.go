package problem3132

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func minimumAddedInteger(nums1 []int, nums2 []int) int {
	sort.Ints(nums1)
	sort.Ints(nums2)
	for i := 2; i >= 0; i-- {
		quota, diff, idx, valid := 2-i, nums2[0]-nums1[i], i+1, true
		for j := 1; j < len(nums2); j++ {
			for nums2[j]-nums1[idx] != diff {
				if quota == 0 {
					valid = false
					break
				}
				quota--
				idx++
			}
			if !valid {
				break
			}
			idx++
		}
		if valid {
			return diff
		}
	}
	return nums2[0] - nums1[0]
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
