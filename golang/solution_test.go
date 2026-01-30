package golang

import (
	problem "leetCode/problems/problems_744"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "744", "problems", problem.Solve)
}
