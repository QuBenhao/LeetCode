package problem1092

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func shortestCommonSupersequence(str1 string, str2 string) string {
	m, n := len(str1), len(str2)
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}

	for i := range m {
		for j := range n {
			if str1[i] == str2[j] {
				dp[i+1][j+1] = dp[i][j] + 1
			} else {
				dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
			}
		}
	}

	var result []byte
	for i, j := m-1, n-1; i >= 0 || j >= 0; {
		if i < 0 {
			result = append(result, str2[j])
			j--
			continue
		}
		if j < 0 {
			result = append(result, str1[i])
			i--
			continue
		}
		if str1[i] == str2[j] {
			result = append(result, str1[i])
			i--
			j--
		} else if dp[i+1][j] <= dp[i][j+1] {
			result = append(result, str1[i])
			i--
		} else {
			result = append(result, str2[j])
			j--
		}
	}
	slices.Reverse(result)
	return string(result)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var str1 string
	var str2 string

	if err := json.Unmarshal([]byte(inputValues[0]), &str1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &str2); err != nil {
		log.Fatal(err)
	}

	return shortestCommonSupersequence(str1, str2)
}
