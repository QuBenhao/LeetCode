package golang

import (
	"leetCode/problems/problems_94"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "94", "problems", problem94.Solve)
}
