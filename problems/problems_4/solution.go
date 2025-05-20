package problem4

import (
	"encoding/json"
	"log"
	"strings"
)

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	var find func(nums1, nums2 []int, i, j, k int) int
	find = func(nums1, nums2 []int, i, j, k int) int {
		if len(nums1)-i > len(nums2)-j {
			return find(nums2, nums1, j, i, k)
		}
		if i >= len(nums1) {
			return nums2[j+k-1]
		}
		if k == 1 {
			return min(nums1[i], nums2[j])
		}
		if ni := min(i+k/2, len(nums1)); nums1[ni-1] > nums2[j+k/2-1] {
			return find(nums1, nums2, i, j+k/2, k-k/2)
		} else {
			return find(nums1, nums2, ni, j, k-(ni-i))
		}
	}
	if m, n := len(nums1), len(nums2); (m+n)%2 == 1 {
		return float64(find(nums1, nums2, 0, 0, (m+n)/2+1))
	} else {
		return float64(find(nums1, nums2, 0, 0, (m+n)/2)+find(nums1, nums2, 0, 0, (m+n)/2+1)) / 2
	}
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

	return findMedianSortedArrays(nums1, nums2)
}
