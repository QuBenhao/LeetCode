package problem2578

import (
	"encoding/json"
	"log"
	"strings"
)

func splitNum(num int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num int

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}

	return splitNum(num)
}
