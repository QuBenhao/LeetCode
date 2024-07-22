package golang

import (
	"leetCode/problems/problems_543"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "543", "problems", problem543.Solve)
}
