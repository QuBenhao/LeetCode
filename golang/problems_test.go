package golang

import (
	"leetCode/problems/problems_169"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "169", "problems", problem169.Solve)
}
