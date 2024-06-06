package problem1041

import (
	"encoding/json"
	"log"
	"strings"
)

func isRobotBounded(instructions string) bool {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var instructions string

	if err := json.Unmarshal([]byte(values[0]), &instructions); err != nil {
		log.Fatal(err)
	}

	return isRobotBounded(instructions)
}
