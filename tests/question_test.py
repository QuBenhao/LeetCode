import unittest
from os import getenv
from pathlib import Path

from dotenv import load_dotenv

from python.constants import PROBLEM_FOLDER
from python import lc_libs
from python.utils import get_default_folder


class QuestionTest(unittest.TestCase):
    def test_question(self):
        root_path = Path(__file__).parent.parent
        load_dotenv(root_path / ".env")
        problem_folder = getenv(PROBLEM_FOLDER, get_default_folder())
        problem_id = None
        for language in ["python3", "cpp", "java", "typescript", "golang", "rust"]:
            cls = getattr(lc_libs, f"{language.capitalize()}Writer", None)
            self.assertIsNotNone(cls, f"Language {language} Writer not found")
            obj: lc_libs.LanguageWriter = cls()
            if problem_id is None:
                problem_id = obj.get_test_problem_id(root_path, problem_folder)
                self.assertIsNotNone(problem_id, f"Problem id {problem_id} not found")
            else:
                self.assertEqual(problem_id, obj.get_test_problem_id(root_path, problem_folder),
                                 f"{language} problem id mismatch: {obj.get_test_problem_id(root_path, problem_folder)}")

if __name__ == '__main__':
    unittest.main()
