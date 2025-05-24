package golang

import (
	"leetCode/problems/problems_LCR_069"
	"leetCode/problems/problems_LCR_112"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_069", "problems", problemLCR_069.Solve)
	TestEach(t, "LCR_112", "problems", problemLCR_112.Solve)
}
