package golang

import (
	"leetCode/problems/problems_200"
	"leetCode/problems/problems_20"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "200", "problems", problem200.Solve)
	TestEach(t, "20", "problems", problem20.Solve)
}
