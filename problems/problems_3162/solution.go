package problem3162

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfPairs(nums1 []int, nums2 []int, k int) (ans int) {
	counter := map[int]int{}
	for _, num := range nums1 {
		if num%k != 0 {
			continue
		}
		num /= k
		for i := 1; i*i <= num; i++ {
			if num%i != 0 {
				continue
			}
			counter[i]++
			if i*i != num {
				counter[num/i]++
			}
		}
	}
	for _, num := range nums2 {
		ans += counter[num]
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

	return numberOfPairs(nums1, nums2, k)
}
