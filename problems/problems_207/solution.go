package problem207

import (
	"encoding/json"
	"log"
	"strings"
)

func canFinish(numCourses int, prerequisites [][]int) bool {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var numCourses int
	var prerequisites [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &numCourses); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &prerequisites); err != nil {
		log.Fatal(err)
	}

	return canFinish(numCourses, prerequisites)
}
