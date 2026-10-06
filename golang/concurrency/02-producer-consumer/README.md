
# **2. Producer-consumer pattern**
**Scenario:** Create 3 producer goroutines and 2 consumer goroutines:
- Each producer generates a random integer (1-100) every second
- Consumers immediately print the numbers they receive
- The program terminates automatically after 5 seconds

**Requirements:**
- Use `context.Context` for graceful shutdown
- Avoid channel leaks
- Include the consumer ID in the output

## Exercise

[solution](your_solution.go)

---

## Solution

[answer](answer.go)
