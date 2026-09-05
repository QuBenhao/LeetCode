package golang

import (
	problem "leetCode/problems/problems_115"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "115", "problems", problem.Solve)
}
