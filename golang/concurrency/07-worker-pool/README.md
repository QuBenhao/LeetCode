# **7. Worker pool pattern**
**Scenario:** Create a pool of 4 worker goroutines to process a continuous stream of tasks:
- Each worker takes a random 100-500ms to process a task
- When SIGINT (ctrl+c) is received:
    - Stop accepting new tasks
    - Finish accepted tasks gracefully
    - Print statistics (total number of processed tasks)

**Requirements:**
- Use `os/signal` to handle system signals
- Use a buffered channel as the task queue
- Implement graceful shutdown

## Exercise

[solution](your_solution.go)

---

## Solution

[answer](answer.go)
