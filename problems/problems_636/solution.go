package problem636

import (
	"encoding/json"
	"log"
	"strconv"
	"strings"
)

func exclusiveTime(n int, logs []string) []int {
    ans, stack, total := make([]int, n), [][]int{}, 0
    for _, log := range logs {
        splits := strings.Split(log, ":")
        idx, _ := strconv.Atoi(splits[0])
        time, _ := strconv.Atoi(splits[2])
        if splits[1] == "start" {
            stack = append(stack, []int{time, total})
        } else {
            last := stack[len(stack) - 1]
            stack = stack[:len(stack) - 1]
            diff := (time + 1 - last[0]) - (total - last[1])
            ans[idx] += diff
            total += diff
        }
    }
    return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var logs []string

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &logs); err != nil {
		log.Fatal(err)
	}

	return exclusiveTime(n, logs)
}
