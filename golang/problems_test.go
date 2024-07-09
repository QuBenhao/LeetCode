package golang

import (
	"leetCode/problems/problems_118"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "118", "problems", problem118.Solve)
}
