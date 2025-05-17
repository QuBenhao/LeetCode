package problemLCR_057

import (
	"encoding/json"
	"log"
	"strings"
)

func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {
	size := int64(t) + 1
	getBucket := func(v int) int64 {
		if v < 0 {
			return int64(v+1)/size - 1
		}
		return int64(v) / size
	}

	buckets := make(map[int64]int)
	for i, num := range nums {
		bucket := getBucket(num)
		if _, ok := buckets[bucket]; ok {
			return true
		}
		if _, ok := buckets[bucket-1]; ok && int64(num)-int64(buckets[bucket-1]) <= int64(t) {
			return true
		}
		if _, ok := buckets[bucket+1]; ok && int64(buckets[bucket+1])-int64(num) <= int64(t) {
			return true
		}
		buckets[bucket] = num
		if i >= k {
			delete(buckets, getBucket(nums[i-k]))
		}
	}
	return false
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int
	var t int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &t); err != nil {
		log.Fatal(err)
	}

	return containsNearbyAlmostDuplicate(nums, k, t)
}
