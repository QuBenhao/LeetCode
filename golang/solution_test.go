package golang

import (
	problem "leetCode/problems/problems_978"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "978", "problems", problem.Solve)
}
