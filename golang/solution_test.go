package golang

import (
	problem "leetCode/problems/problems_2012"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "2012", "problems", problem.Solve)
}
