package golang

import (
	problem "leetCode/problems/problems_321"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "321", "problems", problem.Solve)
}
