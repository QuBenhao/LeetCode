package golang

import (
	problem "leetCode/problems/problems_450"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "450", "problems", problem.Solve)
}
