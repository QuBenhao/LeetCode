package golang

import (
	"leetCode/problems/problems_55"
	"leetCode/problems/problems_139"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "55", "problems", problem55.Solve)
	TestEach(t, "139", "problems", problem139.Solve)
}
