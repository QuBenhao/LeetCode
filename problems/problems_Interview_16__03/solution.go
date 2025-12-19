package problemInterview_16__03

import (
	"encoding/json"
	"log"
	"strings"
)

func intersection(start1 []int, end1 []int, start2 []int, end2 []int) []float64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var start1 []int
	var end1 []int
	var start2 []int
	var end2 []int

	if err := json.Unmarshal([]byte(inputValues[0]), &start1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &end1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &start2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &end2); err != nil {
		log.Fatal(err)
	}

	return intersection(start1, end1, start2, end2)
}
