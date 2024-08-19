package problem3154

import (
	"encoding/json"
	"log"
	"strings"
)

func waysToReachStair(k int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &k); err != nil {
		log.Fatal(err)
	}

	return waysToReachStair(k)
}
