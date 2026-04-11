"""
Similarity detection for LeetCode problems.
Used to find and link duplicate/similar problems.
"""

import json
import logging
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List, Tuple, Dict

from python.utils import create_link

# Configurable similarity threshold (0.0 to 1.0)
SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", "0.7"))


@dataclass
class ProblemInfo:
    """Problem information for comparison"""
    problem_id: str
    title: str
    description: str
    method_name: Optional[str] = None
    method_signature: Optional[str] = None
    constraints: Optional[str] = None


# Pattern to match "本题与主站 xxx 题相同" or similar references
# Examples:
# - "注意：本题与主站 29 题相同"
# - "注意：本题与主站 1991 题相同"
# - "注意：本题与主站 29&nbsp;题相同" (&nbsp; instead of space)
MAIN_SITE_SAME_PATTERN = re.compile(r"注意[：:]\s*本题与主站\s*(\d+)(?:&nbsp;|\s*)题相同")


def extract_main_site_reference(description: str) -> Optional[str]:
    """
    Extract the main site problem ID from a problem description that indicates
    it's the same as a main site problem.

    Args:
        description: Problem description (HTML or plain text)

    Returns:
        Main site problem ID if found, None otherwise
    """
    if not description:
        return None

    match = MAIN_SITE_SAME_PATTERN.search(description)
    if match:
        return match.group(1)
    return None


def extract_description(problem_md_path: Path) -> Tuple[str, str, str]:
    """
    Extract title, description, and constraints from problem.md

    Returns:
        Tuple of (title, description_without_constraints, constraints)
    """
    if not problem_md_path.exists():
        return "", "", ""

    with problem_md_path.open("r", encoding="utf-8") as f:
        content = f.read()

    # Extract title (first line, format: # ID. Title [Rating: X])
    lines = content.split("\n")
    title = ""
    if lines:
        title_line = lines[0]
        # Remove rating part
        title = re.sub(r'\s*\[.*?\]', '', title_line).strip("# ").strip()

    # Find constraints section
    constraints = ""
    constraints_start = -1
    for i, line in enumerate(lines):
        if "**Constraints:**" in line or "<strong>Constraints:</strong>" in line:
            constraints_start = i
            break

    if constraints_start >= 0:
        # Extract constraints (until end or next major section)
        constraints_lines = []
        for i in range(constraints_start, len(lines)):
            line = lines[i]
            if line.startswith("#") and i > constraints_start:
                break
            constraints_lines.append(line)
        constraints = "\n".join(constraints_lines)

        # Description is before constraints
        description = "\n".join(lines[1:constraints_start])
    else:
        description = "\n".join(lines[1:])

    return title, description, constraints


def extract_method_info(solution_py_path: Path) -> Tuple[Optional[str], Optional[str]]:
    """
    Extract method name and signature from solution.py

    Returns:
        Tuple of (method_name, method_signature)
    """
    if not solution_py_path.exists():
        return None, None

    with solution_py_path.open("r", encoding="utf-8") as f:
        content = f.read()

    # Find all method definitions (look for def method_name(self, ...) -> ReturnType:)
    method_pattern = r'def\s+(\w+)\s*\((?:self,?\s*)?(.*?)\)\s*(?:->\s*(\w+(?:\[[^\]]+\])?))?'
    matches = re.findall(method_pattern, content, re.DOTALL)

    if matches:
        # Skip 'solve' method and find the actual solution method
        for method_name, params, return_type in matches:
            if method_name != 'solve' and not method_name.startswith('_'):
                signature = f"{method_name}({params.strip()}) -> {return_type if return_type else 'Any'}"
                return method_name, signature

        # Fallback to first method if no other found
        method_name, params, return_type = matches[0]
        signature = f"{method_name}({params.strip()}) -> {return_type if return_type else 'Any'}"
        return method_name, signature

    return None, None


def normalize_text(text: str) -> str:
    """Normalize text for comparison by removing numbers, whitespace variations, etc."""
    if not text:
        return ""

    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Remove code blocks
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)

    # Remove inline code
    text = re.sub(r'`[^`]+`', '', text)

    # Remove numbers (data ranges, etc.)
    text = re.sub(r'\b\d+\b', '', text)

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text.lower()


def extract_constraints_numbers(constraints: str) -> Dict[str, str]:
    """
    Extract numerical constraints from constraints section.

    Returns:
        Dict mapping constraint names to their values
    """
    if not constraints:
        return {}

    constraints_dict = {}

    # Pattern for constraints like "n <= 100" or "1 <= nums[i] <= n"
    patterns = [
        r'(\w+)\s*(?:<=|>=|<|>|==)\s*(\d+)',
        r'(\d+)\s*(?:<=|>=|<|>|==)\s*(\w+)',
        r'n\s*==\s*(\w+)\.length',
    ]

    for pattern in patterns:
        matches = re.findall(pattern, constraints)
        for match in matches:
            if isinstance(match, tuple):
                key = match[0] if not match[0].isdigit() else match[1]
                value = match[1] if not match[1].isdigit() else match[0]
                constraints_dict[key] = value

    return constraints_dict


def compare_problems(p1: ProblemInfo, p2: ProblemInfo) -> Tuple[bool, float, str]:
    """
    Compare two problems for similarity.

    Returns:
        Tuple of (is_similar, similarity_score, reason)
    """
    scores = []

    # 1. Compare normalized descriptions
    desc1 = normalize_text(p1.description)
    desc2 = normalize_text(p2.description)

    if desc1 and desc2:
        # Simple word overlap similarity
        words1 = set(desc1.split())
        words2 = set(desc2.split())
        if words1 and words2:
            overlap = len(words1 & words2)
            union = len(words1 | words2)
            desc_similarity = overlap / union if union > 0 else 0
            scores.append(("description", desc_similarity, 0.5))  # 50% weight

    # 2. Compare method signatures
    if p1.method_name and p2.method_name:
        if p1.method_name == p2.method_name:
            scores.append(("method_name", 1.0, 0.3))  # 30% weight for matching method name
        else:
            scores.append(("method_name", 0.0, 0.3))

        if p1.method_signature and p2.method_signature:
            # Compare signatures (ignoring variable names)
            sig1 = re.sub(r'\b\w+\b(?=\s*[,\)])', 'x', p1.method_signature)
            sig2 = re.sub(r'\b\w+\b(?=\s*[,\)])', 'x', p2.method_signature)
            if sig1 == sig2:
                scores.append(("signature", 1.0, 0.2))  # 20% weight

    # 3. Compare titles (often similar for same problem with different constraints)
    title1 = normalize_text(p1.title)
    title2 = normalize_text(p2.title)

    if title1 and title2:
        # Remove Roman numerals (I, II, III) and version numbers
        title1_clean = re.sub(r'\b[IVX]+\b|\b\d+\b', '', title1).strip()
        title2_clean = re.sub(r'\b[IVX]+\b|\b\d+\b', '', title2).strip()

        if title1_clean == title2_clean:
            scores.append(("title", 1.0, 0.1))

    # Calculate weighted score
    total_weight = sum(s[2] for s in scores)
    weighted_score = sum(s[1] * s[2] for s in scores) / total_weight if total_weight > 0 else 0

    # Determine if similar
    is_similar = weighted_score >= SIMILARITY_THRESHOLD

    # Generate reason
    reasons = []
    for name, score, weight in scores:
        if score >= 0.8:
            reasons.append(f"{name} matches")

    if is_similar:
        # Check if only constraints differ
        c1 = extract_constraints_numbers(p1.constraints or "")
        c2 = extract_constraints_numbers(p2.constraints or "")

        if c1 != c2:
            reasons.append("different constraints")

    reason = ", ".join(reasons) if reasons else f"similarity: {weighted_score:.2f}"

    return is_similar, weighted_score, reason


def load_problem_info(problem_path: Path) -> Optional[ProblemInfo]:
    """Load problem info from a problem directory"""
    if not problem_path.exists():
        return None

    problem_id = problem_path.name.split("_")[-1]

    # Check for link.json first - skip linked problems
    link_file = problem_path / "link.json"
    if link_file.exists():
        logging.debug(f"Skipping {problem_id} - already linked")
        return None

    # Get problem.md (prefer English version)
    problem_md = problem_path / "problem.md"
    if not problem_md.exists():
        problem_md = problem_path / "problem_zh.md"

    title, description, constraints = extract_description(problem_md)

    # Get method info from solution.py
    solution_py = problem_path / "solution.py"
    method_name, method_signature = extract_method_info(solution_py)

    return ProblemInfo(
        problem_id=problem_id,
        title=title,
        description=description,
        method_name=method_name,
        method_signature=method_signature,
        constraints=constraints
    )


def extract_method_from_template(code_template: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Extract method name and signature from LeetCode code template.

    Args:
        code_template: The code template from LeetCode API

    Returns:
        Tuple of (method_name, method_signature)
    """
    if not code_template:
        return None, None

    # Find method definition in Python template
    method_pattern = r'def\s+(\w+)\s*\((?:self,?\s*)?(.*?)\)\s*(?:->\s*(\w+(?:\[[^\]]+\])?))?'
    matches = re.findall(method_pattern, code_template, re.DOTALL)

    if matches:
        method_name, params, return_type = matches[0]
        signature = f"{method_name}({params.strip()}) -> {return_type if return_type else 'Any'}"
        return method_name, signature

    return None, None


def find_similar_existing_problem(root_path: Path, problem_folder: str, problem_id: str,
                                   title: str, description: str, method_name: str = None,
                                   method_signature: str = None) -> Optional[Tuple[str, float, str]]:
    """
    Find if there's a similar existing problem.

    Args:
        root_path: Repository root path
        problem_folder: Problem folder name
        problem_id: New problem ID
        title: New problem title
        description: New problem description
        method_name: New problem method name
        method_signature: New problem method signature

    Returns:
        Tuple of (similar_problem_id, similarity_score, reason) if found, None otherwise
    """
    problems_dir = root_path / problem_folder
    if not problems_dir.exists():
        return None

    new_info = ProblemInfo(
        problem_id=problem_id,
        title=title,
        description=description,
        method_name=method_name,
        method_signature=method_signature,
        constraints=""  # We don't have constraints yet
    )

    best_match = None
    best_score = 0.0
    best_reason = ""

    for problem_dir in problems_dir.iterdir():
        if not problem_dir.is_dir():
            continue
        if not problem_dir.name.startswith(f"{problem_folder}_"):
            continue

        existing_id = problem_dir.name.split("_")[-1]
        if existing_id == problem_id:
            continue

        existing_info = load_problem_info(problem_dir)
        if not existing_info:
            continue

        is_similar, score, reason = compare_problems(new_info, existing_info)

        if is_similar and score > best_score:
            best_match = existing_id
            best_score = score
            best_reason = reason

    if best_match:
        return (best_match, best_score, best_reason)
    return None


def check_recent_for_duplicates(root_path: Path, problem_folder: str = "problems", recent_count: int = 10,
                                auto_link: bool = False) -> List[Tuple[str, str, float]]:
    """
    Check recent problems for duplicates and optionally auto-link them.

    Args:
        root_path: Repository root path
        problem_folder: Problem folder name
        recent_count: Number of recent problems to check
        auto_link: Whether to automatically link similar problems

    Returns:
        List of (problem_id, linked_to, similarity_score) tuples
    """
    problems_dir = root_path / problem_folder

    if not problems_dir.exists():
        return []

    # Get all problem directories sorted by modification time
    problem_dirs = []
    for problem_dir in problems_dir.iterdir():
        if not problem_dir.is_dir():
            continue
        if not problem_dir.name.startswith(f"{problem_folder}_"):
            continue
        problem_dirs.append((problem_dir, problem_dir.stat().st_mtime))

    # Sort by modification time (newest first)
    problem_dirs.sort(key=lambda x: x[1], reverse=True)

    # Take recent N problems
    recent_dirs = [p[0] for p in problem_dirs[:recent_count]]

    # Load all info
    infos = {}
    for problem_dir in recent_dirs:
        problem_id = problem_dir.name.split("_")[-1]
        info = load_problem_info(problem_dir)
        if info:
            infos[problem_id] = info

    # Compare all pairs
    linked = []
    processed = set()

    for id1, info1 in infos.items():
        if id1 in processed:
            continue

        for id2, info2 in infos.items():
            if id2 == id1 or id2 in processed:
                continue

            is_similar, score, reason = compare_problems(info1, info2)

            if is_similar:
                # Link the higher ID to the lower ID
                target_id = max(id1, id2)
                source_id = min(id1, id2)

                logging.info(f"Found similar problems: {target_id} <-> {source_id} (score: {score:.2f}, reason: {reason})")

                if auto_link:
                    try:
                        create_link(
                            target_problem=target_id,
                            source_problem=source_id,
                            reason=f"Auto-detected: {reason}",
                            source_folder=problem_folder,
                            target_folder=problem_folder
                        )
                        logging.info(f"Auto-linked {target_id} -> {source_id}")
                        linked.append((target_id, source_id, score))
                        processed.add(target_id)
                    except Exception as e:
                        logging.error(f"Failed to auto-link: {e}")

    return linked
