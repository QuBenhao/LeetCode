package problem1882

import (
	"encoding/json"
	"log"
	"strings"
)

func assignTasks(servers []int, tasks []int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var servers []int
	var tasks []int

	if err := json.Unmarshal([]byte(inputValues[0]), &servers); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &tasks); err != nil {
		log.Fatal(err)
	}

	return assignTasks(servers, tasks)
}
