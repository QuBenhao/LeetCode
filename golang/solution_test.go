package golang

import (
	problem "leetCode/problems/problems_756"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "756", "problems", problem.Solve)
}
