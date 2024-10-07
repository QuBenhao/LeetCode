package problem2187

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func minimumTime(time []int, totalTrips int) int64 {
	minT := slices.Min(time)
	maxT := slices.Max(time)
	avg := (totalTrips-1)/len(time) + 1
	// 循环不变量：check(left) 恒为 false
	left := minT*avg - 1
	// 循环不变量：check(right) 恒为 true
	right := min(maxT*avg, minT*totalTrips)
	for left+1 < right { // 开区间 (left, right) 不为空
		mid := (left + right) / 2
		sum := 0
		for _, t := range time {
			sum += mid / t
		}
		if sum >= totalTrips {
			right = mid // 缩小二分区间为 (left, mid)
		} else {
			left = mid // 缩小二分区间为 (mid, right)
		}
	}
	// 此时 left 等于 right-1
	// check(left) = false 且 check(right) = true，所以答案是 right
	return int64(right) // 最小的 true
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var time []int
	var totalTrips int

	if err := json.Unmarshal([]byte(inputValues[0]), &time); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &totalTrips); err != nil {
		log.Fatal(err)
	}

	return minimumTime(time, totalTrips)
}
