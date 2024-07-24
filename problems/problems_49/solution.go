package problem49

import (
	"encoding/json"
	"log"
	"strings"
)

func groupAnagrams(strs []string) [][]string {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var strs []string

	if err := json.Unmarshal([]byte(inputValues[0]), &strs); err != nil {
		log.Fatal(err)
	}

	return groupAnagrams(strs)
}
