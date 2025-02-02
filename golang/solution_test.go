package golang

import (
	problem "leetCode/problems/problems_680"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "680", "problems", problem.Solve)
}
