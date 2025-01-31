package golang

import (
	problem "leetCode/problems/problems_81"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "81", "problems", problem.Solve)
}
