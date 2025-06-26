package problem799

import (
	"encoding/json"
	"log"
	"strings"
)

func champagneTower(poured int, query_row int, query_glass int) float64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var poured int
	var query_row int
	var query_glass int

	if err := json.Unmarshal([]byte(inputValues[0]), &poured); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &query_row); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &query_glass); err != nil {
		log.Fatal(err)
	}

	return champagneTower(poured, query_row, query_glass)
}
