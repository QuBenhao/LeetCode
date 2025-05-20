package problem3285

import (
	"encoding/json"
	"log"
	"strings"
)

func stableMountains(height []int, threshold int) []int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var height []int
	var threshold int

	if err := json.Unmarshal([]byte(inputValues[0]), &height); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &threshold); err != nil {
		log.Fatal(err)
	}

	return stableMountains(height, threshold)
}
