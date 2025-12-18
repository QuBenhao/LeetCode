package problem2092

import (
	"encoding/json"
	"log"
	"strings"
)

func findAllPeople(n int, meetings [][]int, firstPerson int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var meetings [][]int
	var firstPerson int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &meetings); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &firstPerson); err != nil {
		log.Fatal(err)
	}

	return findAllPeople(n, meetings, firstPerson)
}
