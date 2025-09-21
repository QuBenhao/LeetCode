package golang

import (
	problem "leetCode/problems/problems_3005"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "3005", "problems", problem.Solve)
}
