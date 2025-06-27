package golang

import (
	problem "leetCode/problems/problems_496"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "496", "problems", problem.Solve)
}
