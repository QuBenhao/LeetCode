package golang

import (
	"leetCode/problems/problems_114"
	"leetCode/problems/problems_LCR_088"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_088", "problems", problemLCR_088.Solve)
	TestEach(t, "114", "problems", problem114.Solve)
}
