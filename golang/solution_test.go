package golang

import (
	problem "leetCode/problems/problems_486"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "486", "problems", problem.Solve)
}
