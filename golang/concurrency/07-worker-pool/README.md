# **7. 工作池模式**
**场景**：创建包含 4 个 worker 的协程池，处理持续到达的任务：
- Worker 处理任务需要 100-500ms 随机时间
- 当收到 SIGINT (ctrl+c) 信号时：
    - 停止接收新任务
    - 优雅完成已接收任务
    - 输出统计信息（总处理任务数）

**要求**：
- 使用 `os/signal` 处理系统信号
- 使用带缓冲的 channel 作为任务队列
- 实现 graceful shutdown

## 解题

[solution](your_solution.go)

---

## 答案

[answer](answer.go)
