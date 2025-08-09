package problem869

import (
	"encoding/json"
	"log"
	"reflect"
	"strings"
)

var powerOf2Digits [31]map[int]int
var inited bool

func init() {
	if inited {
		return
	}
	for i := range 31 {
		num := 1 << i
		digitCount := make(map[int]int)
		for num > 0 {
			digitCount[num%10]++
			num /= 10
		}
		powerOf2Digits[i] = digitCount
	}
	inited = true
}

func reorderedPowerOf2(n int) bool {
	digitCount := make(map[int]int)
	for n > 0 {
		digitCount[n%10]++
		n /= 10
	}
	for _, powerDigits := range powerOf2Digits {
		if reflect.DeepEqual(powerDigits, digitCount) {
			return true
		}
	}
	return false
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return reorderedPowerOf2(n)
}
