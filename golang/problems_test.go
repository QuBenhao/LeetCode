package golang

import (
	"leetCode/problems/problems_LCR_098"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_098", "problems", problemLCR_098.Solve)
}
