package golang

import (
	"leetCode/problems/problems_198"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "198", "problems", problem198.Solve)
}
