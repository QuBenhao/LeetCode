package problem2844

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumOperations(num string) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num string

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}

	return minimumOperations(num)
}
