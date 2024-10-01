package problem1870

import (
	"encoding/json"
	"log"
	"strings"
)

func minSpeedOnTime(dist []int, hour float64) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var dist []int
	var hour float64

	if err := json.Unmarshal([]byte(inputValues[0]), &dist); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &hour); err != nil {
		log.Fatal(err)
	}

	return minSpeedOnTime(dist, hour)
}
