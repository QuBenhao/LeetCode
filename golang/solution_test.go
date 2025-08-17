package golang

import (
	problem "leetCode/problems/problems_679"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "679", "problems", problem.Solve)
}
