import unittest
import time

from pathlib import Path

from python import lc_libs
from python.scripts.daily_auto import process_daily

LANGUAGES = ["python3", "cpp", "java", "typescript", "golang", "rust"]

class DailyAutoTest(unittest.TestCase):

    def test_daily_auto(self):
        root_path = Path(__file__).parent.parent
        tmp_folder = str(int(time.time()))
        self.assertIsNone(process_daily(LANGUAGES, tmp_folder),
                          "Daily auto process should not return an error code")
        folder_path = root_path / tmp_folder
        self.assertTrue(folder_path.exists(), f"Temporary folder {tmp_folder} should be created")
        folders = list(folder_path.iterdir())
        self.assertEqual(len(folders), 1, "There should be only one folder in the temporary folder")
        sub_folder_path = folder_path / folders[0]
        for language in LANGUAGES:
            cls = getattr(lc_libs, f"{language.capitalize()}Writer", None)
            self.assertIsNotNone(cls, f"Language {language} Writer not found")
            obj: lc_libs.LanguageWriter = cls()
            self.assertTrue((sub_folder_path / obj.solution_file).exists(),
                            f"Solution file {obj.solution_file} should exist in {tmp_folder}")
        self.assertTrue((sub_folder_path / "problem.md").exists(),
                        "Problem markdown file should exist in " + tmp_folder)
        self.assertTrue((sub_folder_path / "problem_zh.md").is_file(),
                        "Problem Chinese markdown file should exist in " + tmp_folder)
        folder_path.rmdir()
        (root_path / f"daily-{tmp_folder}.json").unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
