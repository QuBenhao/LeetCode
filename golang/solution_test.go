package golang

import (
	problem "leetCode/problems/problems_792"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "792", "problems", problem.Solve)
}
