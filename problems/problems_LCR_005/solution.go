package problemLCR_005

import (
	"encoding/json"
	"log"
	"strings"
)

func maxProduct(words []string) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}

	return maxProduct(words)
}
