package problem1953

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfWeeks(milestones []int) int64 {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var milestones []int

	if err := json.Unmarshal([]byte(values[0]), &milestones); err != nil {
		log.Fatal(err)
	}

	return numberOfWeeks(milestones)
}
