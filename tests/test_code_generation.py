"""
Tests for code generation across all supported languages.

Uses question_code_snippets.json to test that code templates are properly
transformed into runnable solution files.
"""

import pytest
import tempfile
from pathlib import Path
from typing import Dict, List, Any, Optional

from python import lc_libs
from python.utils import format_question_id


# Map language slug to Writer class name suffix
LANG_SLUG_TO_CLASS = {
    "python": "Python3Writer",  # Note: "python" slug maps to Python3Writer
    "python3": "Python3Writer",
    "cpp": "CppWriter",
    "java": "JavaWriter",
    "typescript": "TypescriptWriter",
    "golang": "GolangWriter",
    "rust": "RustWriter",
}

# Languages that are fully supported
SUPPORTED_LANGUAGES = ["python3", "cpp", "java", "typescript", "golang", "rust"]

# These cases are intentionally sourced from python/dev/question_code_snippets.json.
# Keep them aligned with that fixture so targeted codegen tests do not silently skip.
DEV_SNIPPET_CASES = {
    "simple": "1",
    "list_node": "23",
    "tree_node": "919",
    "design": "1656",
}


def get_writer(lang_slug: str) -> Optional[lc_libs.LanguageWriter]:
    """Get the Writer instance for a language slug."""
    class_name = LANG_SLUG_TO_CLASS.get(lang_slug)
    if not class_name:
        return None
    cls = getattr(lc_libs, class_name, None)
    if not cls:
        return None
    return cls()


def get_problem_snippets(question_snippets: List[Dict[str, Any]], problem_id: str) -> List[Dict[str, Any]]:
    """Return snippet records for a problem that must exist in the dev fixture."""
    for item in question_snippets:
        if problem_id in item:
            return item[problem_id]
    raise AssertionError(f"Problem {problem_id} not found in python/dev/question_code_snippets.json")


class TestCodeGeneration:
    """Tests for code generation across languages."""

    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for generated files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)

    @pytest.mark.codegen
    @pytest.mark.parametrize("lang_slug", SUPPORTED_LANGUAGES)
    def test_writer_exists(self, lang_slug: str):
        """Test that each supported language has a Writer class."""
        writer = get_writer(lang_slug)
        assert writer is not None, f"No Writer found for language: {lang_slug}"

    @pytest.mark.codegen
    @pytest.mark.parametrize("lang_slug", SUPPORTED_LANGUAGES)
    def test_writer_has_solution_file(self, lang_slug: str):
        """Test that each Writer has a solution file extension."""
        writer = get_writer(lang_slug)
        assert writer is not None
        assert writer.solution_file, f"Writer for {lang_slug} has no solution_file"
        assert "." in writer.solution_file, f"solution_file should have extension: {writer.solution_file}"

    @pytest.mark.codegen
    def test_generate_simple_two_sum(self, question_snippets: List[Dict[str, Any]], temp_dir: Path):
        """Test code generation for Two Sum problem (simple function signature)."""
        problem_id = DEV_SNIPPET_CASES["simple"]
        problem_data = get_problem_snippets(question_snippets, problem_id)

        for code_snippet in problem_data:
            lang_slug = code_snippet.get("langSlug", "")
            if lang_slug not in SUPPORTED_LANGUAGES:
                continue

            writer = get_writer(lang_slug)
            if writer is None:
                continue

            try:
                generated = writer.write_solution(
                    code_snippet["code"],
                    None,
                    format_question_id(problem_id),
                    "problems"
                )
                assert generated, f"Generated code should not be empty for {lang_slug}"
                assert len(generated) > len(code_snippet["code"]), \
                    f"Generated code should be longer than template for {lang_slug}"
            except NotImplementedError as e:
                pytest.skip(f"Language {lang_slug} not fully implemented: {e}")

    @pytest.mark.codegen
    def test_generate_tree_node_problem(self, question_snippets: List[Dict[str, Any]], temp_dir: Path):
        """Test code generation for a TreeNode problem."""
        problem_id = DEV_SNIPPET_CASES["tree_node"]
        problem_data = get_problem_snippets(question_snippets, problem_id)

        for code_snippet in problem_data:
            lang_slug = code_snippet.get("langSlug", "")
            if lang_slug not in SUPPORTED_LANGUAGES:
                continue

            writer = get_writer(lang_slug)
            if writer is None:
                continue

            try:
                generated = writer.write_solution(
                    code_snippet["code"],
                    None,
                    format_question_id(problem_id),
                    "problems"
                )
                assert generated, f"Generated code should not be empty for {lang_slug}"
                # Check for tree-related processing in generated code
                assert "Tree" in generated or "tree" in generated or "TreeNode" in generated, \
                    f"Generated code should reference TreeNode for {lang_slug}"
            except NotImplementedError as e:
                pytest.skip(f"Language {lang_slug} not fully implemented: {e}")

    @pytest.mark.codegen
    def test_generate_list_node_problem(self, question_snippets: List[Dict[str, Any]], temp_dir: Path):
        """Test code generation for a ListNode problem."""
        problem_id = DEV_SNIPPET_CASES["list_node"]
        problem_data = get_problem_snippets(question_snippets, problem_id)

        for code_snippet in problem_data:
            lang_slug = code_snippet.get("langSlug", "")
            if lang_slug not in SUPPORTED_LANGUAGES:
                continue

            writer = get_writer(lang_slug)
            if writer is None:
                continue

            try:
                generated = writer.write_solution(
                    code_snippet["code"],
                    None,
                    format_question_id(problem_id),
                    "problems"
                )
                assert generated, f"Generated code should not be empty for {lang_slug}"
                # Check for list-related processing in generated code
                assert "List" in generated or "list" in generated or "ListNode" in generated, \
                    f"Generated code should reference ListNode for {lang_slug}"
            except NotImplementedError as e:
                pytest.skip(f"Language {lang_slug} not fully implemented: {e}")

    @pytest.mark.codegen
    def test_generate_design_problem(self, question_snippets: List[Dict[str, Any]], temp_dir: Path):
        """Test code generation for a class/design problem from the dev snippets."""
        problem_id = DEV_SNIPPET_CASES["design"]
        problem_data = get_problem_snippets(question_snippets, problem_id)

        for code_snippet in problem_data:
            lang_slug = code_snippet.get("langSlug", "")
            if lang_slug not in SUPPORTED_LANGUAGES:
                continue

            writer = get_writer(lang_slug)
            if writer is None:
                continue

            try:
                generated = writer.write_solution(
                    code_snippet["code"],
                    None,
                    format_question_id(problem_id),
                    "problems"
                )
                assert generated, f"Generated code should not be empty for {lang_slug}"
                assert "orderedstream" in generated.lower() and "insert" in generated, \
                    f"Generated code should preserve design/class structure for {lang_slug}"
            except NotImplementedError as e:
                pytest.skip(f"Language {lang_slug} not fully implemented: {e}")

    @pytest.mark.codegen
    def test_generate_all_snippets(self, question_snippets: List[Dict[str, Any]]):
        """Test code generation for all supported snippets in python/dev."""
        errors = []
        generated_count = {}
        problems_seen = set()

        for item in question_snippets:
            for problem_id, code_list in item.items():
                problems_seen.add(problem_id)
                for code_snippet in code_list:
                    lang_slug = code_snippet.get("langSlug", "")
                    if lang_slug not in SUPPORTED_LANGUAGES:
                        continue

                    writer = get_writer(lang_slug)
                    if writer is None:
                        continue

                    try:
                        generated = writer.write_solution(
                            code_snippet["code"],
                            None,
                            format_question_id(problem_id),
                            "problems"
                        )
                        if generated:
                            generated_count[lang_slug] = generated_count.get(lang_slug, 0) + 1
                    except NotImplementedError:
                        pass  # Expected for unimplemented features
                    except Exception as e:
                        errors.append(f"Problem {problem_id} ({lang_slug}): {type(e).__name__}: {e}")

        print(f"\nCode generation summary: {generated_count}")

        assert problems_seen, "No problems found in python/dev/question_code_snippets.json"
        assert generated_count, "No supported snippets generated from python/dev/question_code_snippets.json"
        if errors:
            pytest.fail("Code generation failures:\n" + "\n".join(errors[:20]))


class TestWriterEnvironment:
    """Tests for Writer environment checks."""

    @pytest.mark.integration
    @pytest.mark.parametrize("lang_slug", SUPPORTED_LANGUAGES)
    def test_environment_check(self, lang_slug: str):
        """Test that each language's environment is properly set up."""
        writer = get_writer(lang_slug)
        if writer is None:
            pytest.skip(f"No writer for {lang_slug}")

        if not writer.lang_env_commands:
            pytest.skip(f"No environment check for {lang_slug}")

        result = writer.env_check()
        # Note: This test will fail if language runtime is not installed
        # It's marked as integration test for this reason
        if not result:
            pytest.skip(f"Environment not set up for {lang_slug}")


class TestProblemLinking:
    """Tests for problem linking functionality."""

    def test_resolve_link_no_link(self, tmp_path: Path):
        """Test link resolution when no link file exists."""
        from python.lc_libs.language_writer import LanguageWriter

        problem_path = tmp_path / "problems_1"
        problem_path.mkdir()

        resolved, link_info = LanguageWriter._resolve_link(problem_path)
        assert resolved == problem_path
        assert link_info is None

    def test_resolve_link_with_link(self, tmp_path: Path):
        """Test link resolution when link file exists."""
        import json
        from python.lc_libs.language_writer import LanguageWriter

        # Create target problem
        target_path = tmp_path / "problems_1"
        target_path.mkdir()

        # Create linked problem
        linked_path = tmp_path / "problems_2"
        linked_path.mkdir()

        # Create link file
        link_file = linked_path / "link.json"
        link_data = {
            "link_to": "1",
            "link_folder": "problems",
            "reason": "Same problem with different constraints"
        }
        with link_file.open("w") as f:
            json.dump(link_data, f)

        resolved, link_info = LanguageWriter._resolve_link(linked_path)
        assert resolved == target_path
        assert link_info == link_data

    def test_resolve_circular_link(self, tmp_path: Path):
        """Test that circular links are detected."""
        import json
        from python.lc_libs.language_writer import LanguageWriter

        # Create two problems with circular links
        problem_1 = tmp_path / "problems_1"
        problem_1.mkdir()
        problem_2 = tmp_path / "problems_2"
        problem_2.mkdir()

        # Create circular link: 1 -> 2 -> 1
        with (problem_1 / "link.json").open("w") as f:
            json.dump({"link_to": "2", "link_folder": "problems"}, f)
        with (problem_2 / "link.json").open("w") as f:
            json.dump({"link_to": "1", "link_folder": "problems"}, f)

        with pytest.raises(ValueError, match="Circular link"):
            LanguageWriter._resolve_link(problem_1)
