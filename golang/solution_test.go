package golang

import (
	problem "leetCode/problems/problems_110"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "110", "problems", problem.Solve)
}
