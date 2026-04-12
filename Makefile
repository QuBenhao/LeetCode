# Makefile for LeetCode project

.PHONY: test test-unit test-integration test-codegen test-coverage clean help

# Default target
help:
	@echo "Available targets:"
	@echo "  test              - Run all tests"
	@echo "  test-unit         - Run unit tests only"
	@echo "  test-integration  - Run integration tests (requires language runtimes)"
	@echo "  test-codegen      - Run code generation tests"
	@echo "  test-coverage     - Run tests with coverage report"
	@echo "  test-parallel     - Run tests in parallel"
	@echo "  test-daily        - Run daily problem test (current problem)"
	@echo "  test-problems     - Run multiple problems test"
	@echo "  clean             - Clean up temporary files"
	@echo ""
	@echo "Code generation testing:"
	@echo "  test-snippets     - Test code generation for all snippets"
	@echo "  add-snippet       - Add a problem to snippets (use PROBLEM=id)"
	@echo "  print-snippet     - Print original snippet (use PROBLEM=id LANG=lang)"

# Run all unit tests
test-unit:
	PYTHONPATH=. pytest tests/ -m unit -v

# Run integration tests (requires language runtimes installed)
test-integration:
	PYTHONPATH=. pytest tests/ -m integration -v

# Run code generation tests
test-codegen:
	PYTHONPATH=. pytest tests/ -m codegen -v

# Run all tests
test:
	PYTHONPATH=. pytest tests/ -v

# Run tests with coverage
test-coverage:
	PYTHONPATH=. pytest tests/ --cov=python --cov-report=term-missing --cov-report=html

# Run tests in parallel
test-parallel:
	PYTHONPATH=. pytest tests/ -v -n auto

# Run daily problem test
test-daily:
	PYTHONPATH=. python python/test.py

# Run multiple problems test
test-problems:
	PYTHONPATH=. python python/tests.py

# Test code generation for all snippets (slow)
test-snippets:
	PYTHONPATH=. python python/dev/solution_code_test.py solution

# Add a problem snippet (requires COOKIE env var)
add-snippet:
ifndef PROBLEM
	@echo "Error: PROBLEM is required. Use: make add-snippet PROBLEM=123"
	@exit 1
endif
ifndef COOKIE
	@echo "Error: COOKIE is required. Set LEETCODE_COOKIE env var or pass COOKIE=..."
	@exit 1
endif
	PYTHONPATH=. python python/dev/solution_code_test.py add_question_code -p $(PROBLEM) -c $(COOKIE)

# Print original snippet
print-snippet:
ifndef PROBLEM
	@echo "Error: PROBLEM is required. Use: make print-snippet PROBLEM=123 LANG=python3"
	@exit 1
endif
ifndef LANG
	$(eval LANG = python3)
endif
	PYTHONPATH=. python python/dev/solution_code_test.py print_origin -p $(PROBLEM) -l $(LANG)

# Clean up temporary files
clean:
	find . -name "tmp_*.py" -delete
	find . -name "tmp_*.java" -delete
	find . -name "tmp_*.go" -delete
	find . -name "tmp_*.ts" -delete
	find . -name "tmp_*.cpp" -delete
	find . -name "tmp_*.rs" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf htmlcov/ .coverage 2>/dev/null || true

# Install dev dependencies
install-dev:
	pip install -r python/requirements.txt -r python/requirements-dev.txt
