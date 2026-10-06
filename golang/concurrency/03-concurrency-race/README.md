# **3. Concurrent resource contention**
**Scenario:** Implement a thread-safe counter and start 1000 goroutines, each incrementing it by 1.

**Requirements:**
- The final result must be exactly 1000
- Compare the performance of `sync.Mutex` and `atomic` implementations
- Extension: Implement a counter with separate read and write access for a workload with many reads and few writes


## Exercise

[solution](your_solution.go)

---

## Solution

[answer](answer.go)
