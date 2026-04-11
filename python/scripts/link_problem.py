#!/usr/bin/env python3
"""
Link problems with identical or similar solutions.

Usage:
    PYTHONPATH=. python python/scripts/link_problem.py -t 3741 -s 3740 -r "Same problem, different constraints"
    PYTHONPATH=. python python/scripts/link_problem.py -t 3741 -s 3740 -r "reason" -d  # Also delete solution files

This will create a link.json file in problems_3741 that points to problems_3740.
"""

import argparse
import logging
import sys
from pathlib import Path

sys.path.append(Path(__file__).parent.parent.parent.as_posix())

from python.utils import create_link

# Solution files to delete when -d flag is used
SOLUTION_FILES = [
    "solution.py",
    "solution.go",
    "Solution.java",
    "Solution.cpp",
    "solution.rs",
    "solution.ts",
    "Cargo.toml",  # Rust package config
]


def main():
    parser = argparse.ArgumentParser(description="Create a link between two problems")
    parser.add_argument("-t", "--target", required=True, type=str,
                        help="Target problem ID (the problem that will have the link)")
    parser.add_argument("-s", "--source", required=True, type=str,
                        help="Source problem ID (the problem to link to)")
    parser.add_argument("-r", "--reason", required=False, type=str, default=None,
                        help="Reason for the link (optional)")
    parser.add_argument("-tf", "--target-folder", required=False, type=str, default="problems",
                        help="Target problem folder (default: problems)")
    parser.add_argument("-sf", "--source-folder", required=False, type=str, default="problems",
                        help="Source problem folder (default: problems)")
    parser.add_argument("-d", "--delete-solution", required=False, action="store_true",
                        help="Delete existing solution files in target problem after creating link")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    try:
        link_file = create_link(
            target_problem=args.target,
            source_problem=args.source,
            reason=args.reason,
            source_folder=args.source_folder,
            target_folder=args.target_folder
        )
        logging.info(f"Created link file: {link_file}")

        if args.delete_solution:
            root_path = Path(__file__).parent.parent.parent
            target_path = root_path / args.target_folder / f"{args.target_folder}_{args.target}"
            deleted_count = 0
            for sol_file_name in SOLUTION_FILES:
                sol_file = target_path / sol_file_name
                if sol_file.exists():
                    sol_file.unlink()
                    logging.info(f"Deleted: {sol_file}")
                    deleted_count += 1
            if deleted_count > 0:
                logging.info(f"Deleted {deleted_count} solution file(s)")

        logging.info(f"Problem {args.target} is now linked to {args.source}")
        return 0

    except FileNotFoundError as e:
        logging.error(str(e))
        return 1
    except Exception as e:
        logging.error(f"Failed to create link: {e}", exc_info=True)
        return 1


if __name__ == '__main__':
    sys.exit(main())
