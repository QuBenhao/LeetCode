package golang

import (
	problem "leetCode/problems/problems_791"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "791", "problems", problem.Solve)
}
