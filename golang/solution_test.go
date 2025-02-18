package golang

import (
	problem "leetCode/problems/problems_624"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "624", "problems", problem.Solve)
}
