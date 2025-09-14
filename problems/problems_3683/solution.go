package problem3683

import (
	"encoding/json"
	"log"
	"strings"
)

func earliestTime(tasks [][]int) (ans int) {
	ans = 201
	for _, task := range tasks {
		ans = min(ans, task[0]+task[1])
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var tasks [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &tasks); err != nil {
		log.Fatal(err)
	}

	return earliestTime(tasks)
}
