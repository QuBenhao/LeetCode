package problemLCR_112

import (
	"encoding/json"
	"log"
	"strings"
)

func longestIncreasingPath(matrix [][]int) int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var matrix [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &matrix); err != nil {
		log.Fatal(err)
	}

	return longestIncreasingPath(matrix)
}
