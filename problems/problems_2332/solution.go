package problem2332

import (
	"encoding/json"
	"log"
	"strings"
)

func latestTimeCatchTheBus(buses []int, passengers []int, capacity int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var buses []int
	var passengers []int
	var capacity int

	if err := json.Unmarshal([]byte(inputValues[0]), &buses); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &passengers); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &capacity); err != nil {
		log.Fatal(err)
	}

	return latestTimeCatchTheBus(buses, passengers, capacity)
}
