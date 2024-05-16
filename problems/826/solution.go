package problem826

import (
	"encoding/json"
	"log"
	"strings"
)

func maxProfitAssignment(difficulty []int, profit []int, worker []int) int {

}

func Solve(input string) interface{} {
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
