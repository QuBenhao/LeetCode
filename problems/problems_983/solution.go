package problem983

import (
	"encoding/json"
	"log"
	"strings"
)

func mincostTickets(days []int, costs []int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var days []int
	var costs []int

	if err := json.Unmarshal([]byte(inputValues[0]), &days); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &costs); err != nil {
		log.Fatal(err)
	}

	return mincostTickets(days, costs)
}
