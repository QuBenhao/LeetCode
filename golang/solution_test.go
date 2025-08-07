package golang

import (
	problem "leetCode/problems/problems_808"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "808", "problems", problem.Solve)
}
