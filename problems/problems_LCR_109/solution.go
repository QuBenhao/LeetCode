package problemLCR_109

import (
	"encoding/json"
	"log"
	"strings"
)

func openLock(deadends []string, target string) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var deadends []string
	var target string

	if err := json.Unmarshal([]byte(inputValues[0]), &deadends); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return openLock(deadends, target)
}
