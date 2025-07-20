package problem3618

import (
	"encoding/json"
	"log"
	"strings"
)

var FLAG []bool

func init() {
	N := int(1e5)
	FLAG = make([]bool, N+1)
	FLAG[0] = true
	FLAG[1] = true
	for i := 2; i*i <= N; i++ {
		if !FLAG[i] {
			for j := i * 2; j <= N; j += i {
				FLAG[j] = true
			}
		}
	}
}

func splitArray(nums []int) (ans int64) {
	for i, num := range nums {
		if FLAG[i] {
			ans += int64(num)
		} else {
			ans -= int64(num)
		}
	}
	if ans < 0 {
		ans *= -1
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return splitArray(nums)
}
