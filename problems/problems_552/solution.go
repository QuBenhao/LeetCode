package problem552

import (
	"encoding/json"
	"log"
	"strings"
)

func modSum(args ...int) (sum int) {
	for _, v := range args {
		sum = (sum + v) % 1_000_000_007
	}
	return
}

func checkRecord(n int) int {
	const mod = 1_000_000_007
	lastA, lastAL, lastALL, last, lastL, lastLL := 1, 0, 0, 1, 1, 0
	for i := 1; i <= n; i++ {
		lastA, lastAL, lastALL, last, lastL, lastLL = modSum(lastA, lastAL, lastALL, last, lastL, lastLL), lastA, lastAL, modSum(last, lastL, lastLL), last, lastL
	}
	return lastA
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return checkRecord(n)
}
