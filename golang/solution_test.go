package golang

import (
	problem "leetCode/problems/problems_672"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "672", "problems", problem.Solve)
}
