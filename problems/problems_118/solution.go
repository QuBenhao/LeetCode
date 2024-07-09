package problem118

import (
	"encoding/json"
	"log"
	"strings"
)

func generate(numRows int) [][]int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var numRows int

	if err := json.Unmarshal([]byte(inputValues[0]), &numRows); err != nil {
		log.Fatal(err)
	}

	return generate(numRows)
}
