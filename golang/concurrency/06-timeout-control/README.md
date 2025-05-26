# **6. 超时控制**
**场景**：实现一个网络请求函数，要求：
- 并发请求三个镜像服务器
- 使用第一个返回的响应
- 超过 500ms 自动取消所有请求
- 输出最终使用的服务器编号

**要求**：
- 使用 `context.WithTimeout`
- 确保未完成的协程不会泄漏
- 处理可能的 panic

## 解题

[solution](your_solution.go)

---

## 答案

[answer](answer.go)
