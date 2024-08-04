package golang

import (
	"leetCode/problems/problems_15"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "15", "problems", problem15.Solve)
}
