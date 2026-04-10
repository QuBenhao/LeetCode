# PR #183 Code Review: Problem Linking Feature

**Repository:** QuBenhao/LeetCode
**PR:** https://github.com/QuBenhao/LeetCode/pull/183
**Reviewer:** Miracle
**Date:** 2026-04-11

---

## 📋 Overview

| Item | Value |
|------|-------|
| Title | feat!: Add problem linking feature for duplicate problems |
| Changes | +866 / -166 lines |
| Files | 21 files |
| Feature | Problem linking to avoid duplicate code when problems have identical solutions |

---

## 🎯 Feature Summary

When two problems have identical or nearly identical solutions (e.g., same problem with different constraints like `n <= 100` vs `n <= 10^5`), this PR allows linking them instead of duplicating code.

**Key Components:**
- `python/utils/similarity.py` — Similarity detection module
- `python/utils/env_tool.py` — Link creation and resolution functions
- `python/scripts/link_problem.py` — CLI tool for manual linking
- `python/scripts/daily_auto.py` — Auto-link integration

---

## 🔍 Review Results

### Severity Summary

| Level | Count | Blocks Merge? |
|-------|-------|---------------|
| CRITICAL | 0 | — |
| MAJOR | 2 | **Yes** |
| MINOR | 2 | No |
| NIT | 1 | No |

---

## 🚨 MAJOR Issues

### 1. Circular Link Risk

**File:** `python/utils/env_tool.py` (lines 25-46)

**Problem:** `resolve_link()` does not check for circular links. If A → B → C → A forms a cycle, the function will cause infinite recursion / stack overflow.

**Current Code:**
```python
def resolve_link(problem_path: Path) -> Tuple[Path, Optional[dict]]:
    link_file = problem_path / "link.json"
    if not link_file.exists():
        return problem_path, None

    with link_file.open("r", encoding="utf-8") as f:
        link_info = json.load(f)

    link_to = link_info.get("link_to")
    link_folder = link_info.get("link_folder", "problems")

    if not link_to:
        return problem_path, None

    linked_path = root_path / link_folder / f"{link_folder}_{link_to}"
    if not linked_path.exists():
        raise FileNotFoundError(f"Linked problem not found: {linked_path}")

    return linked_path, link_info  # ❌ No circular check
```

**Suggested Fix:**
```python
def resolve_link(problem_path: Path, visited: set = None) -> Tuple[Path, Optional[dict]]:
    if visited is None:
        visited = set()

    link_file = problem_path / "link.json"
    if not link_file.exists():
        return problem_path, None

    problem_id = problem_path.name.split("_")[-1]
    if problem_id in visited:
        raise ValueError(f"Circular link detected involving problem {problem_id}")
    visited.add(problem_id)

    with link_file.open("r", encoding="utf-8") as f:
        link_info = json.load(f)

    link_to = link_info.get("link_to")
    link_folder = link_info.get("link_folder", "problems")

    if not link_to:
        return problem_path, None

    root_path = problem_path.parent.parent
    linked_path = root_path / link_folder / f"{link_folder}_{link_to}"

    if not linked_path.exists():
        raise FileNotFoundError(f"Linked problem not found: {linked_path}")

    # Recursively resolve if the linked problem also has a link
    return resolve_link(linked_path, visited)
```

---

### 2. Documentation References Non-Existent Script

**File:** `CLAUDE.md` (lines 185-199)

**Problem:** The documentation references `similarity_checker.py`, but this file does not exist in the repository.

**Current Documentation:**
```markdown
# Check if a problem has similar existing problems
PYTHONPATH=. python python/scripts/similarity_checker.py -i 3741

# Check recent 10 problems for duplicates
PYTHONPATH=. python python/scripts/similarity_checker.py --recent 10

# Auto-link similar problems
PYTHONPATH=. python python/scripts/similarity_checker.py --recent 5 --auto-link
```

**Suggested Fix:**
Either:
1. Create `python/scripts/similarity_checker.py` as documented, OR
2. Update documentation to use `link_problem.py` instead:
   ```markdown
   # Manual linking
   PYTHONPATH=. python python/scripts/link_problem.py -t 3741 -s 3740 -r "Same problem, different constraints"
   ```

---

## 💡 MINOR Issues

### 1. Missing Trailing Newline in JSON File

**File:** `problems/problems_3741/link.json`

**Problem:** The file ends without a newline character, which violates POSIX standards and may cause warnings with some tools.

**Suggested Fix:**
```python
# In create_link() function
with link_file.open("w", encoding="utf-8") as f:
    json.dump(link_info, f, indent=2, ensure_ascii=False)
    f.write("\n")  # Add trailing newline
```

---

### 2. Hardcoded Similarity Threshold

**File:** `python/utils/similarity.py` (line 172)

**Problem:** The similarity threshold is hardcoded at 0.7, making it difficult to adjust for different use cases.

**Current Code:**
```python
is_similar = weighted_score >= 0.7  # 70% threshold
```

**Suggested Fix:**
```python
# At module level
SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", "0.7"))

# In function
is_similar = weighted_score >= SIMILARITY_THRESHOLD
```

---

## 📝 NIT Issues

### Method Signature Regex May Miss Edge Cases

**File:** `python/utils/similarity.py` (lines 176-177)

The regex for normalizing method signatures may not handle nested generic types correctly (e.g., `List[List[int]]`). This is a minor issue since it affects edge cases only.

---

## ✅ What's Done Well

1. **Default disabled** — `AUTO_LINK_SIMILAR` defaults to `false`, preventing unexpected behavior
2. **Reason tracking** — Links include a `reason` field for documentation
3. **Complete integration** — Both test and submit workflows resolve links
4. **Error handling** — Proper checks for directory existence and linked problem existence
5. **i18n support** — Both Chinese and English menus updated

---

## 🔬 Edge Case Analysis

| Scenario | Handled? | Notes |
|----------|----------|-------|
| Linked target doesn't exist | ✅ | `FileNotFoundError` raised |
| Target directory doesn't exist | ✅ | `FileNotFoundError` raised |
| Circular links (A→B→C→A) | ❌ | Infinite recursion risk |
| Chained links (A→B, B→C) | ⚠️ | Only resolves one level currently |
| Link to a linked problem | ⚠️ | Only resolves one level |

---

## 📌 Recommendation

**Do not merge yet.** Please fix the two MAJOR issues:

1. Add circular link detection to `resolve_link()`
2. Either create `similarity_checker.py` or update documentation

After fixes, this is a solid feature that will help reduce code duplication in the repository.

---

## 📎 Related Files

- `python/utils/similarity.py` — 432 new lines
- `python/utils/env_tool.py` — +72 / -1
- `python/scripts/link_problem.py` — 86 new lines
- `python/scripts/daily_auto.py` — +88 / -29
