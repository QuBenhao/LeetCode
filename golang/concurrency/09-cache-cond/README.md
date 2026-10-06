# **9. Using condition variables**
**Scenario:** Implement a ring buffer with a capacity of 10:
- Multiple producer goroutines write data when the buffer is not full
- Multiple consumer goroutines read data when the buffer is not empty
- Producers block and wait when the buffer is full
- Consumers block and wait when the buffer is empty

**Requirements:**
- Use `sync.Cond`
- Avoid busy waiting
- Handle safe goroutine termination


## Exercise

[solution](your_solution.go)

---

## Solution

[answer](answer.go)
