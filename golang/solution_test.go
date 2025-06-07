package golang

import (
	problem "leetCode/problems/problems_386"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "386", "problems", problem.Solve)
}
