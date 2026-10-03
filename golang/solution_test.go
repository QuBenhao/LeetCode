package golang

import (
	problem "leetCode/problems/problems_678"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "678", "problems", problem.Solve)
}
