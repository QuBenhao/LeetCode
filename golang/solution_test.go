package golang

import (
	problem "leetCode/problems/problems_342"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "342", "problems", problem.Solve)
}
