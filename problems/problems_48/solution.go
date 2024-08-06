package problem48

import (
	"encoding/json"
	"log"
	"strings"
)

func rotate(matrix [][]int)  {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var matrix [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &matrix); err != nil {
		log.Fatal(err)
	}

	rotate(matrix)
	return matrix
}
