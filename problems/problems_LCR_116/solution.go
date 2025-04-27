package problemLCR_116

import (
	"encoding/json"
	"log"
	"strings"
)

func findCircleNum(isConnected [][]int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var isConnected [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &isConnected); err != nil {
		log.Fatal(err)
	}

	return findCircleNum(isConnected)
}
