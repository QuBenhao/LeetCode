import base64
import json
import logging
import re
import time
from pathlib import Path
from typing import Optional, Tuple


def init_env():
    """Load .env file once at script entry point. Idempotent and safe."""
    from dotenv import load_dotenv
    try:
        load_dotenv()
    except Exception as e:
        print(f"Load Env exception, {e}")

from python.constants import COOKIE_EXPIRY_SECONDS


def get_default_folder(problem_category: str = None, paid_only: bool = False):
    if problem_category == "database":
        return "mysql"
    return "problems" if not paid_only else "premiums"


def resolve_link(problem_path: Path, visited: set = None, original_link_info: dict = None) -> Tuple[Path, Optional[dict]]:
    """
    Resolve problem link if link.json exists.

    Args:
        problem_path: Path to the problem directory
        visited: Set of visited problem IDs (for circular link detection)
        original_link_info: The first link info encountered (for returning to caller)

    Returns:
        Tuple of (resolved_path, link_info) where:
        - resolved_path: The actual problem path to use for solution
        - link_info: The first link configuration dict encountered, None if not linked

    Raises:
        ValueError: If circular link detected
        FileNotFoundError: If linked problem not found
    """
    if visited is None:
        visited = set()

    link_file = problem_path / "link.json"
    if not link_file.exists():
        return problem_path, original_link_info

    problem_id = problem_path.name.split("_")[-1]
    if problem_id in visited:
        raise ValueError(f"Circular link detected involving problem {problem_id}")
    visited.add(problem_id)

    with link_file.open("r", encoding="utf-8") as f:
        link_info = json.load(f)

    # Store the first link info encountered
    if original_link_info is None:
        original_link_info = link_info

    link_to = link_info.get("link_to")
    link_folder = link_info.get("link_folder", "problems")

    if not link_to:
        return problem_path, original_link_info

    # Resolve the linked problem path
    root_path = problem_path.parent.parent
    linked_path = root_path / link_folder / f"{link_folder}_{link_to}"

    if not linked_path.exists():
        raise FileNotFoundError(f"Linked problem not found: {linked_path}")

    # Recursively resolve if the linked problem also has a link
    return resolve_link(linked_path, visited, original_link_info)


def create_link(target_problem: str, source_problem: str, reason: str = None,
                source_folder: str = "problems", target_folder: str = "problems") -> Path:
    """
    Create a link.json file for a problem.

    Args:
        target_problem: The problem ID to create link for (e.g., "3741")
        source_problem: The problem ID to link to (e.g., "3740")
        reason: Optional reason for the link
        source_folder: Folder of the source problem (default: "problems")
        target_folder: Folder of the target problem (default: "problems")

    Returns:
        Path to the created link.json file

    Raises:
        FileNotFoundError: If target or source problem directory not found
        ValueError: If source problem already has a link (would create chain)
    """
    root_path = Path(__file__).parent.parent.parent
    target_path = root_path / target_folder / f"{target_folder}_{target_problem}"
    source_path = root_path / source_folder / f"{source_folder}_{source_problem}"

    if not target_path.exists():
        raise FileNotFoundError(f"Target problem directory not found: {target_path}")

    if not source_path.exists():
        raise FileNotFoundError(f"Source problem directory not found: {source_path}")

    # Prevent linking to a linked problem (would create chain)
    source_link_file = source_path / "link.json"
    if source_link_file.exists():
        raise ValueError(
            f"Source problem {source_problem} is already linked. "
            "Linking to a linked problem is not allowed to prevent chains."
        )

    link_info = {
        "link_to": source_problem,
        "link_folder": source_folder,
    }
    if reason:
        link_info["reason"] = reason

    link_file = target_path / "link.json"
    with link_file.open("w", encoding="utf-8") as f:
        json.dump(link_info, f, indent=2, ensure_ascii=False)
        f.write("\n")  # Add trailing newline per POSIX standards

    return link_file


# Maps normalized language names (as used by daily_auto / submit) to the
# regex that extracts the LeetCode method name from a generated solution file.
# The harness wrapper (solve/Solve/main) is excluded — we want the real
# LeetCode entry method (e.g. smallestSubsequence / removeDuplicateLetters).
_METHOD_NAME_PATTERNS = {
    "python3": r"def\s+(\w+)\(self",
    "py": r"def\s+(\w+)\(self",
    "cpp": r"class\s+Solution\s*\{.*?public:\s*[\w\s\*]*?(\w+)\s*\(",
    "c++": r"class\s+Solution\s*\{.*?public:\s*[\w\s\*]*?(\w+)\s*\(",
    "golang": r"func\s+(\w+)\(s\b",
    "go": r"func\s+(\w+)\(s\b",
    "java": r"public\s+\w+\s+(\w+)\(String\s+s\)",
    "typescript": r"function\s+(\w+)\(s:\s*string\)",
    "ts": r"function\s+(\w+)\(s:\s*string\)",
    "rust": r"pub\s+fn\s+(\w+)\(s:\s*String\)",
}
_WRAPPER_METHODS = {"solve", "Solve", "main"}


def extract_solution_method_name(solution_file, lang: str) -> Optional[str]:
    """Extract the LeetCode method name from a generated solution file.

    Returns None if the file is missing or the language is unsupported.
    The harness wrapper (solve/Solve/main) is never returned.
    """
    path = Path(solution_file) if not isinstance(solution_file, Path) else solution_file
    if not path.exists():
        return None
    pattern = _METHOD_NAME_PATTERNS.get(lang)
    if not pattern:
        return None
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return None
    # A solution file may contain a harness wrapper (solve/Solve/main) before the
    # real LeetCode method. Skip wrappers and return the first real method name.
    for match in re.finditer(pattern, text, re.S):
        name = match.group(1)
        if name not in _WRAPPER_METHODS:
            return name
    return None


def rename_solution_method(code: str, lang: str, old_name: str, new_name: str) -> str:
    """Rename a solution method (definition + self/recursive calls) in submitted code.

    Uses word-boundary matching so substrings of other identifiers are untouched.
    No-op when old/new are missing or identical.
    """
    if not code or not old_name or not new_name or old_name == new_name:
        return code
    return re.sub(r"\b" + re.escape(old_name) + r"\b", new_name, code)


def adapt_linked_solution_code(root_path: Path, problem_folder: str, problem_id: str,
                               solution_folder: str, solution_problem_id: str,
                               lang: str, code: str, solution_file: str) -> str:
    """Adapt submitted code when a problem is linked to another with a different method name.

    When submitting problem `problem_id` whose solution resolves to `solution_problem_id`
    (via link.json), LeetCode expects `problem_id`'s own method name. If the two methods
    differ (e.g. 1081 `smallestSubsequence` vs 316 `removeDuplicateLetters`), rewrite the
    linked solution's method name to the current problem's.

    Method names are taken from each problem's local solution file; no network needed.
    If the current problem has no own solution file, the linked code is returned unchanged
    (assumes method names match, which holds for auto-detected same-method links).
    """
    if not code or not solution_file or problem_id == solution_problem_id:
        return code
    target_file = root_path / problem_folder / f"{problem_folder}_{problem_id}" / solution_file
    linked_file = root_path / solution_folder / f"{solution_folder}_{solution_problem_id}" / solution_file
    new_name = extract_solution_method_name(target_file, lang)
    old_name = extract_solution_method_name(linked_file, lang)
    if new_name and old_name and new_name != old_name:
        logging.info(
            f"Linked method name differs ({old_name} from {solution_problem_id} "
            f"-> {new_name} for {problem_id}); renaming for submission"
        )
        return rename_solution_method(code, lang, old_name, new_name)
    return code


def check_cookie_expired(cookie: Optional[str]) -> bool:
    """
    Checks if a LeetCode cookie has expired by examining the LEETCODE_SESSION JWT.

    Parameters:
        cookie (str): The cookie string to check. Should contain LEETCODE_SESSION.

    Returns:
        bool: True if the cookie is expired or invalid; False otherwise.
    """
    if not cookie:
        return True

    # 查找 LEETCODE_SESSION
    session_match = re.search(r'LEETCODE_SESSION=([^;]+)', cookie)
    if not session_match:
        return True

    session_token = session_match.group(1)

    try:
        # JWT 格式: header.payload.signature
        parts = session_token.split('.')
        if len(parts) != 3:
            return True

        # 解码 payload (第二部分)
        payload = parts[1]
        # 补齐 base64 padding
        payload += '=' * (4 - len(payload) % 4)
        decoded = base64.urlsafe_b64decode(payload)
        payload_data = json.loads(decoded)

        # 检查过期时间字段 (exp 或 expired_time_)
        exp = payload_data.get('exp') or payload_data.get('expired_time_')
        if not exp:
            return True

        # exp 是过期时间，如果当前时间大于 exp，则已过期
        return time.time() > exp

    except Exception:
        # 如果解析失败，回退到旧逻辑检查其他时间戳
        timestamp_pattern = r"(?<!\d)[\s,=]*([1-9]\d{9})[\s,=]*(?!\d)"
        match = re.findall(timestamp_pattern, cookie)
        if not match:
            return True
        max_timestamp = max(match)
        return time.time() - int(max_timestamp) >= COOKIE_EXPIRY_SECONDS
