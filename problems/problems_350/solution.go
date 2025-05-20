package problem350

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func intersect(nums1 []int, nums2 []int) (ans []int) {
	// 解法一： 排序双指针
	sort.Ints(nums1)
	sort.Ints(nums2)
	n1, n2 := len(nums1), len(nums2)
	for idx1, idx2 := 0, 0; idx1 < n1 && idx2 < n2; {
		if d := nums1[idx1] - nums2[idx2]; d == 0 {
			ans = append(ans, nums1[idx1])
			idx1++
			idx2++
		} else if d > 0 {
			idx2++
		} else {
			idx1++
		}
	}
	return

	// // 解法二： 哈希
	// counter1, counter2 := map[int]int{}, map[int]int{}
	// for _, num := range nums1 {
	// 	counter1[num]++
	// }
	// for _, num := range nums2 {
	// 	counter2[num]++
	// }
	// for k, c1 := range counter1 {
	// 	if c2, ok := counter2[k]; ok {
	// 		for i := 0; i < min(c1, c2); i++ {
	// 			ans = append(ans, k)
	// 		}
	// 	}
	// }
	// return
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

	return intersect(nums1, nums2)
}
