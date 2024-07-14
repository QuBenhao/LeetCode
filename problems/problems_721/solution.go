package problem721

import (
	"encoding/json"
	"log"
	"strings"
)

func accountsMerge(accounts [][]string) [][]string {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var accounts [][]string

	if err := json.Unmarshal([]byte(inputValues[0]), &accounts); err != nil {
		log.Fatal(err)
	}

	return accountsMerge(accounts)
}
