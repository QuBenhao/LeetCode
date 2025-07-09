package problem670

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumSwap(num int) int {
	var digits []int
	idxes := make(map[int]int)
	n := 0
	for x := num; x > 0; x /= 10 {
		cur := x % 10
		digits = append(digits, cur)
		if _, ok := idxes[cur]; !ok {
			idxes[cur] = n
		}
		n++
	}
	for i := n - 1; i > 0; i-- {
		for j := 9; j > digits[i]; j-- {
			if idx, ok := idxes[j]; ok && idx < i {
				digits[idx], digits[i] = digits[i], digits[idx]
				res := 0
				for k := n - 1; k >= 0; k-- {
					res = res*10 + digits[k]
				}
				return res
			}
		}
	}
	return num
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num int

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}

	return maximumSwap(num)
}
