package golang

import (
	problem "leetCode/problems/problems_316"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "316", "problems", problem.Solve)
}
