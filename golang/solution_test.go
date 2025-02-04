package golang

import (
	problem "leetCode/problems/problems_90"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "90", "problems", problem.Solve)
}
