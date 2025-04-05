package golang

import (
	problem "leetCode/problems/problems_368"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "368", "problems", problem.Solve)
}
