package problem3145

import (
	"encoding/json"
	"log"
	"strings"
)

func findProductsOfElements(queries [][]int64) []int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var queries [][]int64

	if err := json.Unmarshal([]byte(inputValues[0]), &queries); err != nil {
		log.Fatal(err)
	}

	return findProductsOfElements(queries)
}
