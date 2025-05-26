# **10. Goroutine 泄漏排查**
**场景**：给定一个有泄漏的并发代码：
```go
func leakyFunction() {
    ch := make(chan int)
    go func() {
        time.Sleep(time.Second)
        ch <- 1
    }()
    return // 直接返回
}
```
**要求**：
- 分析泄漏原因
- 给出两种修复方案
- 使用 `runtime.NumGoroutine()` 验证修复效果


## 解题

[solution](your_solution.go)

---

## 答案

[answer](answer.go)
