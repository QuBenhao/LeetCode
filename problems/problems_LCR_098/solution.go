package problemLCR_098

import (
	"encoding/json"
	"log"
	"strings"
)

func uniquePaths(m int, n int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var m int
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &m); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &n); err != nil {
		log.Fatal(err)
	}

	return uniquePaths(m, n)
}
