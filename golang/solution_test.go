package golang

import (
	problem "leetCode/problems/problems_781"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "781", "problems", problem.Solve)
}
