package golang

import (
	problem "leetCode/problems/problems_551"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "551", "problems", problem.Solve)
}
