package golang

import (
	"leetCode/problems/problems_739"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "739", "problems", problem739.Solve)
}
