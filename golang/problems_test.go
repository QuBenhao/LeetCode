package golang

import (
	"leetCode/problems/problems_189"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "189", "problems", problem189.Solve)
}
