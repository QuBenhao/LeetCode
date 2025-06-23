package golang

import (
	problem "leetCode/problems/problems_816"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "816", "problems", problem.Solve)
}
