package golang

import (
	problem "leetCode/problems/problems_908"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "908", "problems", problem.Solve)
}
