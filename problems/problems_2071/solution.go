package problem2071

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func helper(tasks []int, workers []int, pills int, strength int, k int) bool {
	i := 0
	var validTasks []int
	for idx := len(workers) - k; idx < len(workers); idx++ {
		for i < k && tasks[i] <= workers[idx]+strength {
			validTasks = append(validTasks, tasks[i])
			i++
		}
		if len(validTasks) == 0 {
			return false
		}
		if validTasks[0] <= workers[idx] {
			validTasks = validTasks[1:]
			continue
		}
		if pills == 0 {
			return false
		}
		pills--
		validTasks = validTasks[:len(validTasks)-1]
	}
	return true
}

func maxTaskAssign(tasks []int, workers []int, pills int, strength int) int {
	sort.Ints(tasks)
	sort.Ints(workers)

	left, right := 0, min(len(tasks), len(workers))
	for left < right {
		mid := left + (right-left+1)/2
		if helper(tasks, workers, pills, strength, mid) {
			left = mid
		} else {
			right = mid - 1
		}
	}
	return left
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var tasks []int
	var workers []int
	var pills int
	var strength int

	if err := json.Unmarshal([]byte(inputValues[0]), &tasks); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &workers); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &pills); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &strength); err != nil {
		log.Fatal(err)
	}

	return maxTaskAssign(tasks, workers, pills, strength)
}
