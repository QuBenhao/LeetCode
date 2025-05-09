package problemLCR_117

import (
	"encoding/json"
	"log"
	"strings"
)

func numSimilarGroups(strs []string) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var strs []string

	if err := json.Unmarshal([]byte(inputValues[0]), &strs); err != nil {
		log.Fatal(err)
	}

	return numSimilarGroups(strs)
}
