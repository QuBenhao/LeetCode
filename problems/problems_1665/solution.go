package problem1665

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumEffort(tasks [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var tasks [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &tasks); err != nil {
		log.Fatal(err)
	}

	return minimumEffort(tasks)
}
