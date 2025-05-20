package problem762

import (
	"encoding/json"
	"log"
	"strings"
)

func countPrimeSetBits(left int, right int) (ans int) {
	primeNumbers := []int{2, 3, 5, 7, 11, 13, 17, 19}

	for i := left; i <= right; i++ {
		bits := 0
		for n := i; n > 0; n >>= 1 {
			bits += n & 1
		}
		for _, prime := range primeNumbers {
			if bits == prime {
				ans++
				break
			}
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var left int
	var right int

	if err := json.Unmarshal([]byte(inputValues[0]), &left); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &right); err != nil {
		log.Fatal(err)
	}

	return countPrimeSetBits(left, right)
}
