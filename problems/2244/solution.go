package problem2244

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumRounds(tasks []int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var tasks []int

	if err := json.Unmarshal([]byte(values[0]), &tasks); err != nil {
		log.Fatal(err)
	}

	return minimumRounds(tasks)
}
