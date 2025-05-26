# **5. 多路 channel 合并**
**场景**：实现 `fanIn` 函数合并三个输入 channel 的数据到一个输出 channel。

**要求**：
- 当所有输入 channel 关闭后自动关闭输出 channel
- 使用 `select` 语句实现
- 处理不同 channel 关闭时间不一致的情况

## 解题

[solution](your_solution.go)

---

## 答案

[answer](answer.go)
