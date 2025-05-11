package problemLCR_040

import (
	"encoding/json"
	"log"
	"strings"
)

func maximalRectangle(matrix []string) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var matrix []string

	if err := json.Unmarshal([]byte(inputValues[0]), &matrix); err != nil {
		log.Fatal(err)
	}

	return maximalRectangle(matrix)
}
