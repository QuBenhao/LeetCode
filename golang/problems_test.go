//go:build goexperiment.jsonv2

package golang

import (
	problem0 "leetCode/problems/problems_1752"
	problem1 "leetCode/problems/problems_3833"
	problem2 "leetCode/problems/problems_3834"
	problem3 "leetCode/problems/problems_3835"
	problem4 "leetCode/problems/problems_3836"
	"testing"
)

func TestProblems(t *testing.T) {
	t.Run("problems_1752", func(t *testing.T) {
		TestEach(t, "1752", "problems", problem0.Solve)
	})
	t.Run("problems_3833", func(t *testing.T) {
		TestEach(t, "3833", "problems", problem1.Solve)
	})
	t.Run("problems_3834", func(t *testing.T) {
		TestEach(t, "3834", "problems", problem2.Solve)
	})
	t.Run("problems_3835", func(t *testing.T) {
		TestEach(t, "3835", "problems", problem3.Solve)
	})
	t.Run("problems_3836", func(t *testing.T) {
		TestEach(t, "3836", "problems", problem4.Solve)
	})
}
