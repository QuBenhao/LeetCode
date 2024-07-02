# Golang

## Start

First install Requirements,
```shell
go mod download
```

**change both `problem "leetCode/problems/1652"` and `TestEach(t, "2065", "problems", problem.Solve)` in [solution_test.go](solution_test.go)**, and try:
```shell
go test golang/solution_test.go golang/test_basic.go -test.timeout 3s
```

or if you want to run more than one questions,
**change problems in [problems_test.go](problems_test.go)**, and try:
```shell
go test golang/problems_test.go golang/test_basic.go -test.timeout 10s
```