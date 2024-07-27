package golang

import (
	"leetCode/problems/problems_215"
	"leetCode/problems/problems_39"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "215", "problems", problem215.Solve)
	TestEach(t, "39", "problems", problem39.Solve)
}
