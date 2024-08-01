package golang

import (
	"leetCode/problems/problems_322"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "322", "problems", problem322.Solve)
}
