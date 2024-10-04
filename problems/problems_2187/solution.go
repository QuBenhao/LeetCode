package problem2187

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumTime(time []int, totalTrips int) int64 {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var time []int
	var totalTrips int

	if err := json.Unmarshal([]byte(inputValues[0]), &time); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &totalTrips); err != nil {
		log.Fatal(err)
	}

	return minimumTime(time, totalTrips)
}
