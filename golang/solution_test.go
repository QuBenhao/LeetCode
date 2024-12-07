package golang

import (
	problem "leetCode/problems/problems_782"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "782", "problems", problem.Solve)
}
