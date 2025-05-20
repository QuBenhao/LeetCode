package problem2931

import (
	"encoding/json"
	"log"
	"strings"
)

func maxSpending(values [][]int) int64 {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var values [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &values); err != nil {
		log.Fatal(err)
	}

	return maxSpending(values)
}
