package problem3700

import (
	"encoding/json"
	"log"
	"strings"
)

const MOD = 1000000007

// Matrix multiplication
func matMul(A, B [][]int) [][]int {
	n := len(A)
	C := make([][]int, n)
	for i := range C {
		C[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		for k := 0; k < n; k++ {
			if A[i][k] != 0 {
				for j := 0; j < n; j++ {
					C[i][j] = (C[i][j] + A[i][k]*B[k][j]) % MOD
				}
			}
		}
	}
	return C
}

// Matrix exponentiation: T^k
func matPow(T [][]int, k int) [][]int {
	n := len(T)
	// Identity matrix
	result := make([][]int, n)
	for i := range result {
		result[i] = make([]int, n)
		result[i][i] = 1
	}
	base := make([][]int, n)
	for i := range base {
		base[i] = make([]int, n)
		copy(base[i], T[i])
	}
	for k > 0 {
		if k&1 == 1 {
			result = matMul(result, base)
		}
		base = matMul(base, base)
		k >>= 1
	}
	return result
}

// Matrix-vector multiplication
func matVecMul(T [][]int, vec []int) []int {
	n := len(T)
	result := make([]int, n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if T[i][j] != 0 {
				result[i] = (result[i] + T[i][j]*vec[j]) % MOD
			}
		}
	}
	return result
}

func zigZagArrays(n int, l int, r int) int {
	m := r - l + 1 // number of possible values
	if n == 1 {
		return m
	}
	if n == 2 {
		return m * (m - 1) % MOD
	}

	// State: idx(v, d) where v in [l,r], d in {0: down, 1: up}
	stateSize := 2 * m

	idx := func(v, d int) int {
		return (v-l)*2 + d
	}

	// Build transition matrix T
	// T[i][j] = 1 means transition from state j to state i
	T := make([][]int, stateSize)
	for i := range T {
		T[i] = make([]int, stateSize)
	}
	for v := l; v <= r; v++ {
		for d := 0; d < 2; d++ {
			for w := l; w <= r; w++ {
				if w == v {
					continue
				}
				if d == 0 && w > v { // was down to v, now up to w
					T[idx(w, 1)][idx(v, 0)] = 1
				} else if d == 1 && w < v { // was up to v, now down to w
					T[idx(w, 0)][idx(v, 1)] = 1
				}
			}
		}
	}

	// Initial vector for position 2
	init := make([]int, stateSize)
	for v := l; v <= r; v++ {
		init[idx(v, 0)] = max(0, r-v) // prev in [v+1, r]
		init[idx(v, 1)] = max(0, v-l) // prev in [l, v-1]
	}

	// Compute T^(n-2) * init
	Tk := matPow(T, n-2)
	final := matVecMul(Tk, init)

	sum := 0
	for _, v := range final {
		sum = (sum + v) % MOD
	}
	return sum
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var l int
	var r int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &l); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &r); err != nil {
		log.Fatal(err)
	}

	return zigZagArrays(n, l, r)
}
