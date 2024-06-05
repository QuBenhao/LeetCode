package problem2938

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumSteps(s string) int64 {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var s string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}

	return minimumSteps(s)
}
