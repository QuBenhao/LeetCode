package problem1535

import(
	"encoding/json"
	"log"
	"strings"
)

func getWinner(arr []int, k int) int {

}

func Solve(input string) interface{} {
    values := strings.Split(input, "\n")
	var arr []int
	var k int

	if err := json.Unmarshal([]byte(values[0]), &arr); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &k); err != nil {
		log.Fatal(err)
	}

    return getWinner(arr, k)
}
