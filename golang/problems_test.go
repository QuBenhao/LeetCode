package golang

import (
	"leetCode/problems/problems_141"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "141", "problems", problem141.Solve)
}
