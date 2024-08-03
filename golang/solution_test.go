package golang

import (
	problem "leetCode/problems/problems_572"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "572", "problems", problem.Solve)
}
