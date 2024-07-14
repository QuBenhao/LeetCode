package golang

import (
	"leetCode/problems/problems_155"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "155", "problems", problem155.Solve)
}
