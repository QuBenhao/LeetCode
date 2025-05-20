package problem3340

import (
	"encoding/json"
	"log"
	"strings"
)

func isBalanced(num string) bool {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num string

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}

	return isBalanced(num)
}
