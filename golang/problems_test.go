package golang

import (
	"leetCode/problems/problems_160"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "160", "problems", problem160.Solve)
}
