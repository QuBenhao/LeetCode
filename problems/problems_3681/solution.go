package problem3681

import (
	"encoding/json"
	"log"
	"strings"
)

func maxXorSubsequences(nums []int) (ans int) {
	base := make([]int, 32)
	for _, x := range nums {
		for i := 31; i >= 0; i-- {
			if ((x >> i) & 1) == 1 {
				if base[i] != 0 {
					x ^= base[i]
				} else {
					base[i] = x
					break
				}
			}
		}
	}
	for i := 31; i >= 0; i-- {
		if base[i] != 0 && ((ans>>i)&1) == 0 {
			ans ^= base[i]
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maxXorSubsequences(nums)
}
