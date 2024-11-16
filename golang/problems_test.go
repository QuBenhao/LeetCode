package golang

import (
	"leetCode/problems/problems_LCR_072"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_072", "problems", problemLCR_072.Solve)
}
