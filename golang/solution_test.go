package golang

import (
	problem "leetCode/problems/problems_685"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "685", "problems", problem.Solve)
}
