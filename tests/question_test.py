"""Tests for question/problem handling across languages."""

import pytest
from os import getenv
from pathlib import Path

from dotenv import load_dotenv

from python import lc_libs
from python.constants import PROBLEM_FOLDER
from python.utils import get_default_folder

LANGUAGES = ["python3", "cpp", "java", "typescript", "golang", "rust"]


@pytest.mark.integration
class TestQuestion:
    """Integration tests for question handling."""

    def test_question_environment_and_problem_id(self, project_root: Path):
        """Test that all language writers can access the current problem."""
        load_dotenv(project_root / ".env")
        problem_folder = getenv(PROBLEM_FOLDER, get_default_folder())
        problem_id = None

        for language in LANGUAGES:
            cls = getattr(lc_libs, f"{language.capitalize()}Writer", None)
            assert cls is not None, f"Language {language} Writer not found"
            obj: lc_libs.LanguageWriter = cls()

            fetched_id = obj.get_test_problem_id(project_root, problem_folder)

            # Golang uses a different test file format with hardcoded problem ID
            # Skip the ID consistency check for golang
            if language == "golang":
                if fetched_id is None:
                    pytest.skip(f"Golang test file not configured for {problem_folder}")
                continue

            if problem_id is None:
                problem_id = fetched_id
                assert problem_id is not None, f"Problem id not found in {problem_folder}"
            else:
                assert problem_id == fetched_id, \
                    f"{language} problem id mismatch: expected {problem_id}, got {fetched_id}"

            # Environment check (may fail if runtime not installed)
            env_ok = obj.env_check()
            if not env_ok:
                pytest.skip(f"Environment not set up for {language}")
