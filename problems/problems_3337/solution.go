package problem3337

import (
	"encoding/json"
	"log"
	"strings"
)

const MOD = 1000000007

func multiply(a, b [][]int) [][]int {
	n := len(a)
	m := len(b[0])
	p := len(b)
	res := make([][]int, n)
	for i := range res {
		res[i] = make([]int, m)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			for k := 0; k < p; k++ {
				res[i][j] = (res[i][j] + a[i][k]*b[k][j]) % MOD
			}
		}
	}
	return res
}

func matrixPower(matrix [][]int, n int, res [][]int) [][]int {
	for n > 0 {
		if n%2 == 1 {
			res = multiply(matrix, res)
		}
		matrix = multiply(matrix, matrix)
		n /= 2
	}
	return res
}

func lengthAfterTransformations(s string, t int, nums []int) (ans int) {
	matrix := make([][]int, 26)
	for i := range matrix {
		matrix[i] = make([]int, 26)
	}
	for i, c := range nums {
		for j := i + 1; j < i+c+1; j++ {
			matrix[j%26][i]++
		}
	}
	f0 := make([][]int, 26)
	for i := range f0 {
		f0[i] = make([]int, 1)
	}
	for _, r := range s {
		f0[r-'a'][0]++
	}
	res := matrixPower(matrix, t, f0)
	for i := range 26 {
		ans = (ans + res[i][0]) % MOD
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var t int
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &t); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &nums); err != nil {
		log.Fatal(err)
	}

	return lengthAfterTransformations(s, t, nums)
}
