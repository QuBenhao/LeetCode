package problemLCR_095

import (
	"encoding/json"
	"log"
	"strings"
)

func longestCommonSubsequence(text1 string, text2 string) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var text1 string
	var text2 string

	if err := json.Unmarshal([]byte(inputValues[0]), &text1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &text2); err != nil {
		log.Fatal(err)
	}

	return longestCommonSubsequence(text1, text2)
}
