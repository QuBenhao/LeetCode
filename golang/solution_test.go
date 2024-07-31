package golang

import (
	problem "leetCode/problems/problems_LCP_40"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "LCP_40", "problems", problem.Solve)
}
