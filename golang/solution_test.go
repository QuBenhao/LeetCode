package golang

import (
	problem "leetCode/problems/problems_45"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "45", "problems", problem.Solve)
}
