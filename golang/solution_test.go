package golang

import (
	problem "leetCode/problems/problems_80"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "80", "problems", problem.Solve)
}
