package golang

import (
	"leetCode/problems/problems_24"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "24", "problems", problem24.Solve)
}
