package problem3211

import (
	"encoding/json"
	"log"
	"strings"
)

func validStrings(n int) (ans []string) {
	path := make([]byte, n)
	var dfs func(int)
	dfs = func(u int) {
		if u == n {
			ans = append(ans, string(path))
			return
		}
		if u == 0 || path[u-1] == '1' {
			path[u] = '0'
			dfs(u + 1)
		}
		path[u] = '1'
		dfs(u + 1)
	}
	dfs(0)
	return
}


func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return validStrings(n)
}
