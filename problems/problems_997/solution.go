package problem997

import (
	"encoding/json"
	"log"
	"strings"
)

func findJudge(n int, trust [][]int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var trust [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &trust); err != nil {
		log.Fatal(err)
	}

	return findJudge(n, trust)
}
