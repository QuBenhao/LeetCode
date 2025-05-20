package problem826

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func maxProfitAssignment(difficulty []int, profit []int, worker []int) (ans int) {
	n := len(difficulty)
	type job struct{ d, p int }
	jobs := make([]job, n)
	for i, d := range difficulty {
		jobs[i] = job{d, profit[i]}
	}
	slices.SortFunc(jobs, func(a, b job) int { return a.d - b.d })
	slices.Sort(worker)
	j, maxProfit := 0, 0
	for _, w := range worker {
		for j < n && jobs[j].d <= w {
			maxProfit = max(maxProfit, jobs[j].p)
			j++
		}
		ans += maxProfit
	}
	return ans
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var difficulty []int
	var profit []int
	var worker []int

	if err := json.Unmarshal([]byte(values[0]), &difficulty); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &profit); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[2]), &worker); err != nil {
		log.Fatal(err)
	}

	return maxProfitAssignment(difficulty, profit, worker)
}
