"""Tests for daily auto functionality."""

import pytest
import time
from pathlib import Path

from python import lc_libs
from python.scripts.daily_auto import process_daily

LANGUAGES = ["python3", "cpp", "java", "typescript", "golang", "rust"]


@pytest.mark.integration
@pytest.mark.slow
class TestDailyAuto:
    """Integration tests for daily auto processing."""

    def test_daily_auto_creates_folder(self, project_root: Path):
        """Test that daily auto process creates expected files."""
        tmp_folder = str(int(time.time()))

        # Run daily auto process
        result = process_daily(LANGUAGES, tmp_folder)
        assert result is None, "Daily auto process should not return an error code"

        folder_path = project_root / tmp_folder
        assert folder_path.exists(), f"Temporary folder {tmp_folder} should be created"

        folders = list(folder_path.iterdir())
        assert len(folders) == 1, "There should be only one folder in the temporary folder"

        sub_folder_path = folder_path / folders[0]

        # Check all language solution files
        for language in LANGUAGES:
            cls = getattr(lc_libs, f"{language.capitalize()}Writer", None)
            assert cls is not None, f"Language {language} Writer not found"
            obj: lc_libs.LanguageWriter = cls()
            solution_file = sub_folder_path / obj.solution_file
            assert solution_file.exists(), \
                f"Solution file {obj.solution_file} should exist in {tmp_folder}"

        # Check problem markdown files
        assert (sub_folder_path / "problem.md").exists(), \
            f"Problem markdown file should exist in {tmp_folder}"
        assert (sub_folder_path / "problem_zh.md").is_file(), \
            f"Problem Chinese markdown file should exist in {tmp_folder}"

        # Cleanup
        import shutil
        shutil.rmtree(folder_path)
        (project_root / f"daily-{tmp_folder}.json").unlink(missing_ok=True)
