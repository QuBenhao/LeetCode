package problem887

import (
	"encoding/json"
	"log"
	"strings"
)

func superEggDrop(k int, n int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var k int
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &n); err != nil {
		log.Fatal(err)
	}

	return superEggDrop(k, n)
}
