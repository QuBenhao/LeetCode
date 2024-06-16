package problem522

import (
	"encoding/json"
	"log"
	"strings"
)

func findLUSlength(strs []string) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var strs []string

	if err := json.Unmarshal([]byte(values[0]), &strs); err != nil {
		log.Fatal(err)
	}

	return findLUSlength(strs)
}
