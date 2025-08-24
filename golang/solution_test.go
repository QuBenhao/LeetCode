package golang

import (
	problem "leetCode/problems/problems_498"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "498", "problems", problem.Solve)
}
