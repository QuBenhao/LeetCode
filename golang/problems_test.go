package golang

import (
	"leetCode/problems/problems_141"
	"leetCode/problems/problems_142"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "141", "problems", problem141.Solve)
	TestEach(t, "142", "problems", problem142.Solve)
}
