package golang

import (
	"leetCode/problems/problems_49"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "49", "problems", problem49.Solve)
}
