package problemLCR_085

import (
	"encoding/json"
	"log"
	"strings"
)

func generateParenthesis(n int) (ans []string) {
	var dfs func([]byte, int, int)
	dfs = func(arr []byte, left, right int) {
		if right == 0 {
			ans = append(ans, string(arr))
			return
		}
		if left > 0 {
			arr = append(arr, '(')
			dfs(arr, left-1, right)
			arr = arr[:len(arr)-1]
		}
		if right > left {
			arr = append(arr, ')')
			dfs(arr, left, right-1)
			arr = arr[:len(arr)-1]
		}
	}
	dfs(make([]byte, 0), n, n)
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return generateParenthesis(n)
}
