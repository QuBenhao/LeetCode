package problemLCR_111

import (
	"encoding/json"
	"log"
	"strings"
)

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var equations [][]string
	var values []float64
	var queries [][]string

	if err := json.Unmarshal([]byte(inputValues[0]), &equations); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &values); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &queries); err != nil {
		log.Fatal(err)
	}

	return calcEquation(equations, values, queries)
}
