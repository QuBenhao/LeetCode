package golang

import (
	"leetCode/problems/problems_207"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "207", "problems", problem207.Solve)
}
