package golang

import (
	problem3618 "leetCode/problems/problems_3618"
	problem3619 "leetCode/problems/problems_3619"
	problem3620 "leetCode/problems/problems_3620"
	problem3621 "leetCode/problems/problems_3621"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "3618", "problems", problem3618.Solve)
	TestEach(t, "3619", "problems", problem3619.Solve)
	TestEach(t, "3620", "problems", problem3620.Solve)
	TestEach(t, "3621", "problems", problem3621.Solve)
}
