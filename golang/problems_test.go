package golang

import (
	"leetCode/problems/problems_48"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "48", "problems", problem48.Solve)
}
