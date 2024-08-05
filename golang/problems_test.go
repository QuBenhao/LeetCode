package golang

import (
	"leetCode/problems/problems_438"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "438", "problems", problem438.Solve)
}
