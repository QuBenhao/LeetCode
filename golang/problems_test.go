package golang

import (
	"leetCode/problems/problems_LCR_071"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_071", "problems", problemLCR_071.Solve)
}
