package problemLCR_100

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumTotal(triangle [][]int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var triangle [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &triangle); err != nil {
		log.Fatal(err)
	}

	return minimumTotal(triangle)
}
