#!/usr/bin/env python3
"""
Batch link LCR problems to their corresponding main site problems.

LCR problems have a note like:
"注意：本题与主站 XXX 题相同"

This script extracts these mappings and creates links.
"""

import logging
import re
import sys
from pathlib import Path

sys.path.append(Path(__file__).parent.parent.parent.as_posix())

from python.utils import create_link

# Pattern to match the main site problem reference
# Examples:
# - "注意：本题与主站 29 题相同"
# - "注意：本题与主站 1991 题相同"
# - "注意：本题与主站 29&nbsp;题相同" (&nbsp; instead of space)
MAIN_SITE_PATTERN = re.compile(r"注意：本题与主站\s*(\d+)(?:&nbsp;|\s*)题相同")


def extract_main_site_problem(problem_md_path: Path) -> str | None:
    """Extract the main site problem number from problem_zh.md."""
    if not problem_md_path.exists():
        return None

    content = problem_md_path.read_text(encoding="utf-8")
    match = MAIN_SITE_PATTERN.search(content)
    if match:
        return match.group(1)
    return None


def check_problem_exists(problem_id: str, folder: str = "problems") -> bool:
    """Check if a problem folder exists."""
    root_path = Path(__file__).parent.parent.parent
    problem_path = root_path / folder / f"{folder}_{problem_id}"
    return problem_path.exists() and problem_path.is_dir()


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    root_path = Path(__file__).parent.parent.parent
    problems_path = root_path / "problems"

    # Find all LCR problem folders
    lcr_folders = sorted(problems_path.glob("problems_LCR_*"))

    linked_count = 0
    skipped_no_match = 0
    skipped_no_source = 0
    skipped_already_linked = 0

    for lcr_folder in lcr_folders:
        lcr_id = lcr_folder.name.replace("problems_", "")
        problem_md = lcr_folder / "problem_zh.md"
        link_file = lcr_folder / "link.json"

        # Skip if already linked
        if link_file.exists():
            logging.info(f"[SKIP] {lcr_id} already linked")
            skipped_already_linked += 1
            continue

        # Extract main site problem ID
        main_id = extract_main_site_problem(problem_md)
        if not main_id:
            logging.warning(f"[NO MATCH] {lcr_id} - no main site reference found")
            skipped_no_match += 1
            continue

        # Check if main site problem exists
        if not check_problem_exists(main_id):
            logging.warning(f"[NO SOURCE] {lcr_id} -> {main_id} - source problem not found")
            skipped_no_source += 1
            continue

        # Create link
        try:
            create_link(
                target_problem=lcr_id,
                source_problem=main_id,
                reason=f"LCR题目，对应主站 {main_id} 题",
                source_folder="problems",
                target_folder="problems"
            )
            logging.info(f"[LINKED] {lcr_id} -> {main_id}")
            linked_count += 1
        except Exception as e:
            logging.error(f"[ERROR] {lcr_id} -> {main_id}: {e}")

    print(f"\n=== Summary ===")
    print(f"Linked: {linked_count}")
    print(f"Skipped (already linked): {skipped_already_linked}")
    print(f"Skipped (no match): {skipped_no_match}")
    print(f"Skipped (no source): {skipped_no_source}")
    print(f"Total LCR folders: {len(lcr_folders)}")


if __name__ == "__main__":
    main()
