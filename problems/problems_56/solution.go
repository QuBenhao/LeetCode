package problem56

import (
	"encoding/json"
	"log"
	"strings"
)

func merge(intervals [][]int) [][]int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var intervals [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &intervals); err != nil {
		log.Fatal(err)
	}

	return merge(intervals)
}
