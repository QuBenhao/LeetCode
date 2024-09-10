package problem2555

import (
	"encoding/json"
	"log"
	"strings"
)

func maximizeWin(prizePositions []int, k int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var prizePositions []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &prizePositions); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maximizeWin(prizePositions, k)
}
