package golang

import (
	problem "leetCode/problems/problems_856"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "856", "problems", problem.Solve)
}
