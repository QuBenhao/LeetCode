package problem2040

import (
	"encoding/json"
	"log"
	"math"
	"sort"
	"strings"
)

func kthSmallestProduct(nums1 []int, nums2 []int, k int64) int64 {
	m, n := int64(len(nums1)), int64(len(nums2))
	zero1, zero2 := int64(sort.SearchInts(nums1, 0)), int64(sort.SearchInts(nums2, 0))
	left, right := int64(math.MaxInt64), int64(math.MinInt64)
	for _, v := range []int64{int64(nums1[0]) * int64(nums2[0]), int64(nums1[m-1]) * int64(nums2[n-1]),
		int64(nums1[0]) * int64(nums2[n-1]), int64(nums1[m-1]) * int64(nums2[0])} {
		left = min(left, v)
		right = max(right, v)
	}
	count := func(x int64) bool {
		var ans int64
		if x < 0 {
			ans = 0
			i, j := int64(0), zero2
			for i < zero1 && j < n {
				if int64(nums1[i])*int64(nums2[j]) > x {
					j++
				} else {
					ans += n - j
					i++
				}
			}
			i, j = zero1, int64(0)
			for i < m && j < zero2 {
				if int64(nums1[i])*int64(nums2[j]) > x {
					i++
				} else {
					ans += m - i
					j++
				}
			}
		} else {
			ans = zero1*(n-zero2) + zero2*(m-zero1)
			i, j := int64(0), zero2-1
			for i < zero1 && j >= 0 {
				if int64(nums1[i])*int64(nums2[j]) > x {
					i++
				} else {
					ans += zero1 - i
					j--
				}
			}
			i, j = zero1, n-1
			for i < m && j >= zero2 {
				if int64(nums1[i])*int64(nums2[j]) > x {
					j--
				} else {
					ans += j - zero2 + 1
					i++
				}
			}
		}
		return ans >= k
	}

	for left < right {
		mid := left + (right-left)/2
		if count(mid) {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return left
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
