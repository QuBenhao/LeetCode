package problemLCR_113

import (
	"encoding/json"
	"log"
	"strings"
)

func findOrder(numCourses int, prerequisites [][]int) []int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var numCourses int
	var prerequisites [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &numCourses); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &prerequisites); err != nil {
		log.Fatal(err)
	}

	return findOrder(numCourses, prerequisites)
}
