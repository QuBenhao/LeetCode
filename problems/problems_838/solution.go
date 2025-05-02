package problem838

import (
	"encoding/json"
	"log"
	"strings"
)

func pushDominoes(dominoes string) string {
	n := len(dominoes)
	right := make([]int, n)
	for i := n - 1; i >= 0; i-- {
		if dominoes[i] == 'R' {
			right[i] = n
		} else if dominoes[i] == 'L' {
			right[i] = i
		} else {
			if i < n-1 && right[i+1] != n {
				right[i] = right[i+1]
			} else {
				right[i] = n
			}
		}
	}
	var ans []byte
	prev := -1
	for i := 0; i < n; i++ {
		if dominoes[i] == 'R' {
			prev = i
			ans = append(ans, 'R')
		} else if dominoes[i] == 'L' {
			prev = -1
			ans = append(ans, 'L')
		} else {
			if prev == -1 {
				if right[i] != n {
					ans = append(ans, 'L')
				} else {
					ans = append(ans, '.')
				}
			} else if right[i] == n {
				ans = append(ans, 'R')
			} else {
				if d := right[i] + prev - 2*i; d > 0 {
					ans = append(ans, 'R')
				} else if d < 0 {
					ans = append(ans, 'L')
				} else {
					ans = append(ans, '.')
				}
			}
		}
	}
	return string(ans)
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var dominoes string

	if err := json.Unmarshal([]byte(inputValues[0]), &dominoes); err != nil {
		log.Fatal(err)
	}

	return pushDominoes(dominoes)
}
