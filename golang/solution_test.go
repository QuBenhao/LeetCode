package golang

import (
	problem "leetCode/problems/problems_85"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "85", "problems", problem.Solve)
}
