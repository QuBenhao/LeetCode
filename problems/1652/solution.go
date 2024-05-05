package problem1652

import (
	"encoding/json"
	"log"
	"strings"
)

func Solve(input string) []int {
	values := strings.Split(input, "\n")
	var code []int
	var k int

	if err := json.Unmarshal([]byte(values[0]), &code); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &k); err != nil {
		log.Fatal(err)
	}

	return decrypt(code, k)
}

func sum(arr []int) (ans int) {
    for _, v := range arr {
        ans += v
    }
    return
}

func decrypt(code []int, k int) []int {
    n := len(code)
    ans := make([]int, n)
    if k == 0 {
        return ans
    }
    var s int
    if k > 0 {
        s = sum(code[1:k+1]) 
    } else {
        s = sum(code[n + k:])
    }
    for i := 0; i < n; i++ {
        ans[i] = s
        if k > 0 {
            s += code[(i + k + 1) % n] - code[(i + 1) % n]
        } else {
            s += code[i % n] - code[(i + k + n) % n]
        }
    }
    return ans
}