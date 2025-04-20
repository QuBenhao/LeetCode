package problem2145

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfArrays(differences []int, lower int, upper int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var differences []int
	var lower int
	var upper int

	if err := json.Unmarshal([]byte(inputValues[0]), &differences); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &lower); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &upper); err != nil {
		log.Fatal(err)
	}

	return numberOfArrays(differences, lower, upper)
}
