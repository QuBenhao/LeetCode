package problem1235

import (
	"encoding/json"
	"log"
	"slices"
	"sort"
	"strings"
)

func jobScheduling(startTime, endTime, profit []int) int {
	n := len(startTime)
	type job struct{ start, end, profit int }
	jobs := make([]job, n)
	for i, start := range startTime {
		jobs[i] = job{start, endTime[i], profit[i]}
	}
	slices.SortFunc(jobs, func(a, b job) int { return a.end - b.end }) // 按照结束时间排序

	f := make([]int, n+1)
	for i, job := range jobs {
		j := sort.Search(i, func(j int) bool { return jobs[j].end > job.start })
		// 状态转移中，为什么是 j 不是 j+1：上面算的是 > start，-1 后得到 <= start，但由于还要 +1，抵消了
		f[i+1] = max(f[i], f[j]+job.profit)
	}
	return f[n]
}

func Solve(input string) any {
	arrays := strings.Split(input, "\n")
	arr1, arr2, arr3 := make([]int, 0), make([]int, 0), make([]int, 0)
	if err := json.Unmarshal([]byte(arrays[0]), &arr1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(arrays[1]), &arr2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(arrays[2]), &arr3); err != nil {
		log.Fatal(err)
	}
	return jobScheduling(arr1, arr2, arr3)
}
