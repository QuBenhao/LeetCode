package problem119

import (
	"encoding/json"
	"log"
	"strings"
)

func getRow(rowIndex int) []int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var rowIndex int

	if err := json.Unmarshal([]byte(inputValues[0]), &rowIndex); err != nil {
		log.Fatal(err)
	}

	return getRow(rowIndex)
}
