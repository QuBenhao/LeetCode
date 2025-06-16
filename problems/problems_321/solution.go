package problem321

import (
	"encoding/json"
	"log"
	"strings"
)

func pickArr(nums []int, length int) (ans []int) {
	drop := len(nums) - length
	for _, num := range nums {
		for drop > 0 && len(ans) > 0 && ans[len(ans)-1] < num {
			ans = ans[:len(ans)-1]
			drop--
		}
		ans = append(ans, num)
	}
	ans = ans[:length]
	return
}

func greater(nums1, nums2 []int) bool {
	for i := range min(len(nums1), len(nums2)) {
		if nums1[i] != nums2[i] {
			return nums1[i] > nums2[i]
		}
	}
	return len(nums1) > len(nums2)
}

func merge(nums1, nums2 []int) (ans []int) {
	for len(nums1) > 0 || len(nums2) > 0 {
		if greater(nums1, nums2) {
			ans = append(ans, nums1[0])
			nums1 = nums1[1:]
		} else {
			ans = append(ans, nums2[0])
			nums2 = nums2[1:]
		}
	}
	return
}

func maxNumber(nums1 []int, nums2 []int, k int) (ans []int) {
	m, n := len(nums1), len(nums2)
	if m > n {
		m, n = n, m
		nums1, nums2 = nums2, nums1
	}
	for i := max(0, k-n); i <= min(m, k); i++ {
		arr1 := pickArr(nums1, i)
		arr2 := pickArr(nums2, k-i)
		merged := merge(arr1, arr2)
		if greater(merged, ans) {
			ans = merged
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums1 []int
	var nums2 []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &nums2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return maxNumber(nums1, nums2, k)
}
