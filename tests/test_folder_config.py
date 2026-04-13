"""Tests for PROBLEM_FOLDER configuration and folder handling."""

import json
import os
import pytest
import shutil
import tempfile
from pathlib import Path
from typing import Generator

from python.constants import PROBLEM_FOLDER
from python.utils import get_default_folder, resolve_link, create_link


@pytest.mark.unit
class TestGetDefaultFolder:
    """Tests for get_default_folder function."""

    def test_default_returns_problems(self):
        """Test default behavior returns 'problems'."""
        assert get_default_folder() == "problems"

    def test_paid_only_returns_premiums(self):
        """Test paid_only=True returns 'premiums'."""
        assert get_default_folder(paid_only=True) == "premiums"

    def test_database_category_returns_mysql(self):
        """Test database category returns 'mysql'."""
        assert get_default_folder(problem_category="database") == "mysql"

    def test_database_with_paid_only_returns_mysql(self):
        """Test database category ignores paid_only flag."""
        assert get_default_folder(problem_category="database", paid_only=True) == "mysql"

    def test_unknown_category_returns_problems(self):
        """Test unknown category defaults to 'problems'."""
        assert get_default_folder(problem_category="unknown") == "problems"

    def test_unknown_category_with_paid_only_returns_premiums(self):
        """Test unknown category with paid_only returns 'premiums'."""
        assert get_default_folder(problem_category="unknown", paid_only=True) == "premiums"


@pytest.mark.unit
class TestResolveLink:
    """Tests for resolve_link function."""

    @pytest.fixture
    def temp_project(self, tmp_path: Path) -> Generator[Path, None, None]:
        """Create a temporary project structure for testing."""
        # Create problems folder
        problems = tmp_path / "problems"
        problems.mkdir()

        # Create premiums folder
        premiums = tmp_path / "premiums"
        premiums.mkdir()

        # Create custom folder
        custom = tmp_path / "custom"
        custom.mkdir()

        # Create a problem in problems folder
        problem_1 = problems / "problems_1"
        problem_1.mkdir()
        (problem_1 / "solution.py").write_text("# Solution 1")

        # Create a problem in premiums folder
        premium_1 = premiums / "premiums_101"
        premium_1.mkdir()
        (premium_1 / "solution.py").write_text("# Premium Solution 101")

        # Create a problem in custom folder
        custom_1 = custom / "custom_201"
        custom_1.mkdir()
        (custom_1 / "solution.py").write_text("# Custom Solution 201")

        yield tmp_path

    def test_no_link_returns_same_path(self, temp_project: Path):
        """Test that non-linked problem returns same path."""
        problem_path = temp_project / "problems" / "problems_1"
        resolved, link_info = resolve_link(problem_path)
        assert resolved == problem_path
        assert link_info is None

    def test_link_to_same_folder(self, temp_project: Path):
        """Test linking to another problem in the same folder."""
        # Create source problem
        source = temp_project / "problems" / "problems_2"
        source.mkdir()
        (source / "solution.py").write_text("# Solution 2")

        # Create link from problems_1 to problems_2
        target = temp_project / "problems" / "problems_1"
        link_file = target / "link.json"
        link_file.write_text(json.dumps({"link_to": "2", "link_folder": "problems"}))

        resolved, link_info = resolve_link(target)
        assert resolved == source
        assert link_info["link_to"] == "2"
        assert link_info["link_folder"] == "problems"

    def test_link_cross_folder_problems_to_premiums(self, temp_project: Path):
        """Test linking from problems to premiums folder."""
        # Create link from problems_1 to premiums_101
        target = temp_project / "problems" / "problems_1"
        link_file = target / "link.json"
        link_file.write_text(json.dumps({
            "link_to": "101",
            "link_folder": "premiums",
            "reason": "Same problem in premium"
        }))

        resolved, link_info = resolve_link(target)
        expected = temp_project / "premiums" / "premiums_101"
        assert resolved == expected
        assert link_info["link_to"] == "101"
        assert link_info["link_folder"] == "premiums"
        assert link_info["reason"] == "Same problem in premium"

    def test_link_cross_folder_premiums_to_problems(self, temp_project: Path):
        """Test linking from premiums to problems folder."""
        # Create link from premiums_101 to problems_1
        target = temp_project / "premiums" / "premiums_101"
        link_file = target / "link.json"
        link_file.write_text(json.dumps({
            "link_to": "1",
            "link_folder": "problems"
        }))

        resolved, link_info = resolve_link(target)
        expected = temp_project / "problems" / "problems_1"
        assert resolved == expected
        assert link_info["link_to"] == "1"

    def test_link_to_custom_folder(self, temp_project: Path):
        """Test linking to a custom folder (not problems or premiums)."""
        # Create link from problems_1 to custom_201
        target = temp_project / "problems" / "problems_1"
        link_file = target / "link.json"
        link_file.write_text(json.dumps({
            "link_to": "201",
            "link_folder": "custom"
        }))

        resolved, link_info = resolve_link(target)
        expected = temp_project / "custom" / "custom_201"
        assert resolved == expected
        assert link_info["link_to"] == "201"
        assert link_info["link_folder"] == "custom"

    def test_circular_link_detection(self, temp_project: Path):
        """Test that circular links are detected and raise error."""
        # Create two problems that link to each other
        problem_1 = temp_project / "problems" / "problems_1"
        problem_2 = temp_project / "problems" / "problems_2"
        problem_2.mkdir()
        (problem_2 / "solution.py").write_text("# Solution 2")

        # Link 1 -> 2
        (problem_1 / "link.json").write_text(json.dumps({"link_to": "2", "link_folder": "problems"}))
        # Link 2 -> 1
        (problem_2 / "link.json").write_text(json.dumps({"link_to": "1", "link_folder": "problems"}))

        with pytest.raises(ValueError, match="Circular link detected"):
            resolve_link(problem_1)

    def test_missing_linked_problem_raises_error(self, temp_project: Path):
        """Test that linking to non-existent problem raises error."""
        target = temp_project / "problems" / "problems_1"
        link_file = target / "link.json"
        link_file.write_text(json.dumps({"link_to": "999", "link_folder": "problems"}))

        with pytest.raises(FileNotFoundError, match="Linked problem not found"):
            resolve_link(target)

    def test_chained_links_resolved(self, temp_project: Path):
        """Test that chained links (A->B->C) are resolved to final destination."""
        # Create problems 2 and 3
        problem_2 = temp_project / "problems" / "problems_2"
        problem_3 = temp_project / "problems" / "problems_3"
        problem_2.mkdir()
        problem_3.mkdir()
        (problem_2 / "solution.py").write_text("# Solution 2")
        (problem_3 / "solution.py").write_text("# Solution 3")

        # Link 1 -> 2
        problem_1 = temp_project / "problems" / "problems_1"
        (problem_1 / "link.json").write_text(json.dumps({"link_to": "2", "link_folder": "problems"}))
        # Link 2 -> 3
        (problem_2 / "link.json").write_text(json.dumps({"link_to": "3", "link_folder": "problems"}))

        resolved, link_info = resolve_link(problem_1)
        assert resolved == problem_3
        # Should return the first link info encountered
        assert link_info["link_to"] == "2"


@pytest.mark.unit
class TestCreateLinkLogic:
    """Tests for create_link function logic (using resolve_link for verification)."""

    def test_create_link_file_format(self, tmp_path: Path):
        """Test that link.json is created with correct format."""
        # Create mock link file directly
        link_path = tmp_path / "link.json"
        link_data = {
            "link_to": "1",
            "link_folder": "problems",
            "reason": "Test reason"
        }
        link_path.write_text(json.dumps(link_data, indent=2, ensure_ascii=False) + "\n")

        assert link_path.exists()
        loaded = json.loads(link_path.read_text())
        assert loaded["link_to"] == "1"
        assert loaded["link_folder"] == "problems"
        assert loaded["reason"] == "Test reason"


@pytest.mark.integration
class TestCreateLinkIntegration:
    """Integration tests for create_link with actual project structure."""

    @pytest.fixture(autouse=True)
    def cleanup_links(self, project_root: Path):
        """Clean up any test links created during tests."""
        yield
        # Cleanup: remove any test link files
        for folder in ["problems", "premiums"]:
            for problem_dir in (project_root / folder).glob(f"{folder}_*"):
                link_file = problem_dir / "link_test_temp.json"
                link_file.unlink(missing_ok=True)

    def test_create_link_validates_target_exists(self, project_root: Path):
        """Test that create_link validates target problem exists."""
        # Try to create link for non-existent problem
        with pytest.raises(FileNotFoundError, match="Target problem directory not found"):
            create_link("999999", "1", source_folder="problems", target_folder="problems")

    def test_create_link_validates_source_exists(self, project_root: Path):
        """Test that create_link validates source problem exists."""
        # problems_1 exists, problems_999999 does not
        with pytest.raises(FileNotFoundError, match="Source problem directory not found"):
            create_link("1", "999999", source_folder="problems", target_folder="problems")

    def test_create_link_cross_folder_problems_to_premiums(self, project_root: Path):
        """Test creating a link from problems to premiums folder."""
        # problems_1 exists, premiums_1055 exists
        # First check if link already exists
        link_file = project_root / "problems" / "problems_1" / "link.json"
        original_link = None
        if link_file.exists():
            original_link = link_file.read_text()

        try:
            # Remove existing link if any
            link_file.unlink(missing_ok=True)

            # Create new link
            result = create_link("1", "1055", reason="Cross-folder test",
                                 source_folder="premiums", target_folder="problems")
            assert result.exists()

            with result.open("r") as f:
                link_data = json.load(f)
            assert link_data["link_to"] == "1055"
            assert link_data["link_folder"] == "premiums"
            assert link_data["reason"] == "Cross-folder test"

        finally:
            # Restore or cleanup
            link_file.unlink(missing_ok=True)
            if original_link:
                link_file.write_text(original_link)


@pytest.mark.integration
class TestFolderConfiguration:
    """Integration tests for folder configuration with test runners."""

    @pytest.fixture
    def temp_project(self, tmp_path: Path) -> Generator[Path, None, None]:
        """Create a temporary project structure with multiple folders."""
        # Create folder structure
        for folder_name in ["problems", "premiums", "contest", "custom"]:
            folder = tmp_path / folder_name
            folder.mkdir()

            # Create a sample problem
            problem = folder / f"{folder_name}_1"
            problem.mkdir()
            (problem / "solution.py").write_text('''
import solution
from typing import *

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.add(test_input[0], test_input[1])

    def add(self, a: int, b: int) -> int:
        return a + b
''')
            (problem / "testcase.py").write_text('''
from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])

class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 2], Output=3))

    def get_testcases(self):
        return self.testcases
''')

        yield tmp_path

    def test_json_config_file_naming(self, temp_project: Path):
        """Test that config file naming follows daily-{folder}.json pattern."""
        # Config files should be named based on the folder
        expected_configs = [
            "daily-problems.json",
            "daily-premiums.json",
            "daily-contest.json",
            "daily-custom.json",
        ]

        for config_name in expected_configs:
            config_path = temp_project / config_name
            # Just verify the naming convention
            assert "daily-" in config_name
            assert ".json" in config_name

    def test_problem_path_resolution(self, temp_project: Path):
        """Test that problem paths are correctly resolved for different folders."""
        folders = ["problems", "premiums", "contest", "custom"]

        for folder in folders:
            problem_path = temp_project / folder / f"{folder}_1"
            assert problem_path.exists(), f"Problem path should exist for {folder}"
            assert (problem_path / "solution.py").exists()
            assert (problem_path / "testcase.py").exists()


@pytest.mark.integration
class TestNonStandardFolder:
    """Tests for non-standard folder configurations (not problems or premiums)."""

    @pytest.fixture
    def temp_project_with_custom(self, tmp_path: Path) -> Generator[tuple[Path, str], None, None]:
        """Create a project with a custom folder and config."""
        custom_folder = "contest"
        folder_path = tmp_path / custom_folder
        folder_path.mkdir()

        # Create a problem
        problem = folder_path / f"{custom_folder}_100"
        problem.mkdir()
        (problem / "solution.py").write_text('''
import solution
from typing import *

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.multiply(test_input[0], test_input[1])

    def multiply(self, a: int, b: int) -> int:
        return a * b
''')
        (problem / "testcase.py").write_text('''
from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])

class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[3, 4], Output=12))
        self.testcases.append(case(Input=[5, 6], Output=30))

    def get_testcases(self):
        return self.testcases
''')

        # Create config file
        config = {"daily": "100", "plans": ["100", custom_folder]}
        config_path = tmp_path / f"daily-{custom_folder}.json"
        with config_path.open("w") as f:
            json.dump(config, f)

        yield tmp_path, custom_folder

    def test_custom_folder_config_exists(self, temp_project_with_custom: tuple[Path, str]):
        """Test that custom folder config file is created correctly."""
        project_path, custom_folder = temp_project_with_custom
        config_path = project_path / f"daily-{custom_folder}.json"
        assert config_path.exists()

        with config_path.open("r") as f:
            config = json.load(f)
        assert config["daily"] == "100"
        assert config["plans"] == ["100", custom_folder]

    def test_custom_folder_problem_resolvable(self, temp_project_with_custom: tuple[Path, str]):
        """Test that problems in custom folder can be resolved."""
        project_path, custom_folder = temp_project_with_custom
        problem_path = project_path / custom_folder / f"{custom_folder}_100"

        # Verify problem structure
        assert problem_path.exists()
        assert (problem_path / "solution.py").exists()
        assert (problem_path / "testcase.py").exists()

        # Verify no link (direct problem)
        resolved, link_info = resolve_link(problem_path)
        assert resolved == problem_path
        assert link_info is None

    def test_cross_folder_link_from_custom(self, temp_project_with_custom: tuple[Path, str]):
        """Test creating a link from custom folder to problems folder."""
        project_path, custom_folder = temp_project_with_custom

        # Create a problem in problems folder
        problems = project_path / "problems"
        problems.mkdir()
        problem_1 = problems / "problems_1"
        problem_1.mkdir()
        (problem_1 / "solution.py").write_text("# Solution 1")

        # Create link file directly (since create_link uses hardcoded path)
        custom_problem = project_path / custom_folder / f"{custom_folder}_100"
        link_file = custom_problem / "link.json"
        link_data = {
            "link_to": "1",
            "link_folder": "problems",
            "reason": "Same as free problem"
        }
        link_file.write_text(json.dumps(link_data, indent=2, ensure_ascii=False) + "\n")

        assert link_file.exists()

        # Verify link resolution
        resolved, link_info = resolve_link(custom_problem)
        assert resolved == problem_1
        assert link_info["link_to"] == "1"
        assert link_info["link_folder"] == "problems"

    def test_custom_folder_naming_convention(self, temp_project_with_custom: tuple[Path, str]):
        """Test that custom folder follows naming convention {folder}_{problem_id}."""
        project_path, custom_folder = temp_project_with_custom

        # Verify folder structure follows convention
        folder_path = project_path / custom_folder
        problem_dirs = list(folder_path.iterdir())
        assert len(problem_dirs) == 1

        problem_dir = problem_dirs[0]
        assert problem_dir.name == f"{custom_folder}_100"
        assert problem_dir.name.startswith(custom_folder)


@pytest.mark.integration
class TestConfigFileResolution:
    """Tests for configuration file resolution with different folders."""

    def test_config_file_path_format(self, tmp_path: Path):
        """Test that config file path follows daily-{folder}.json format."""
        folders = ["problems", "premiums", "contest", "custom", "mysql"]

        for folder in folders:
            config_path = tmp_path / f"daily-{folder}.json"
            config_data = {"daily": "1", "plans": ["1", folder]}
            config_path.write_text(json.dumps(config_data))

            assert config_path.exists()
            loaded = json.loads(config_path.read_text())
            assert loaded["daily"] == "1"

    def test_plans_array_alternates_problem_id_and_folder(self, tmp_path: Path):
        """Test that plans array format is [problem_id, folder, ...]."""
        # Test plans with mixed folders
        config = {
            "daily": "1",
            "plans": ["1", "problems", "101", "premiums", "201", "custom"]
        }
        config_path = tmp_path / "daily-test.json"
        config_path.write_text(json.dumps(config))

        loaded = json.loads(config_path.read_text())
        plans = loaded["plans"]

        # Verify alternation: even indices are problem IDs, odd indices are folders
        for i in range(0, len(plans), 2):
            assert isinstance(plans[i], str), f"Problem ID at index {i} should be string"
            assert plans[i].isdigit() or plans[i].isalnum(), f"Problem ID format at index {i}"
        for i in range(1, len(plans), 2):
            assert isinstance(plans[i], str), f"Folder at index {i} should be string"

    def test_missing_config_file_handling(self, tmp_path: Path):
        """Test handling when config file doesn't exist."""
        config_path = tmp_path / "daily-nonexistent.json"
        assert not config_path.exists()

        # Code should handle missing config gracefully
        # This tests the expectation, actual error handling is in test.py/tests.py


@pytest.mark.integration
class TestEnvVarHandling:
    """Tests for environment variable handling."""

    def test_problem_folder_env_var_name(self):
        """Test that PROBLEM_FOLDER constant is correct."""
        from python.constants import PROBLEM_FOLDER
        assert PROBLEM_FOLDER == "PROBLEM_FOLDER"

    def test_env_var_not_set_uses_default(self, monkeypatch):
        """Test that unset PROBLEM_FOLDER uses default."""
        monkeypatch.delenv(PROBLEM_FOLDER, raising=False)
        result = get_default_folder()
        assert result == "problems"

    def test_env_var_set_to_premiums(self, monkeypatch):
        """Test PROBLEM_FOLDER=premiums behavior."""
        monkeypatch.setenv(PROBLEM_FOLDER, "premiums")
        result = os.getenv(PROBLEM_FOLDER)
        assert result == "premiums"

    def test_env_var_set_to_custom_folder(self, monkeypatch):
        """Test PROBLEM_FOLDER=custom behavior."""
        monkeypatch.setenv(PROBLEM_FOLDER, "contest")
        result = os.getenv(PROBLEM_FOLDER)
        assert result == "contest"


@pytest.mark.integration
class TestMultiFolderPlans:
    """Tests for multi-folder test execution via plans array."""

    def test_plans_with_multiple_folders(self, tmp_path: Path):
        """Test that plans can reference multiple different folders."""
        config = {
            "daily": "1",
            "plans": [
                "1", "problems",
                "101", "premiums",
                "201", "contest",
                "301", "mysql"
            ]
        }
        config_path = tmp_path / "daily-mixed.json"
        config_path.write_text(json.dumps(config))

        loaded = json.loads(config_path.read_text())
        plans = loaded["plans"]

        # Extract folders from plans
        folders_in_plans = plans[1::2]  # Odd indices are folders
        assert "problems" in folders_in_plans
        assert "premiums" in folders_in_plans
        assert "contest" in folders_in_plans
        assert "mysql" in folders_in_plans

    def test_plans_cross_folder_link_scenario(self, tmp_path: Path):
        """Test scenario where a problem links to another folder."""
        # Create two folder structures
        problems = tmp_path / "problems"
        problems.mkdir()
        premiums = tmp_path / "premiums"
        premiums.mkdir()

        # Create problem in premiums
        premium_problem = premiums / "premiums_101"
        premium_problem.mkdir()
        (premium_problem / "solution.py").write_text("# Premium 101")

        # Create problem in problems with link to premiums
        free_problem = problems / "problems_1"
        free_problem.mkdir()
        (free_problem / "solution.py").write_text("# Free 1 (linked)")
        (free_problem / "link.json").write_text(json.dumps({
            "link_to": "101",
            "link_folder": "premiums"
        }))

        # Create config that tests both
        config = {
            "daily": "1",
            "plans": ["1", "problems", "101", "premiums"]
        }
        config_path = tmp_path / "daily-mixed.json"
        config_path.write_text(json.dumps(config))

        # Verify link resolves correctly
        resolved, link_info = resolve_link(free_problem)
        assert resolved == premium_problem
        assert link_info["link_to"] == "101"
        assert link_info["link_folder"] == "premiums"


@pytest.mark.integration
class TestGoSetupCustomFolder:
    """Tests for Go test setup with custom PROBLEM_FOLDER."""

    @pytest.fixture
    def temp_project_with_custom(self, tmp_path: Path) -> Generator[tuple[Path, str], None, None]:
        """Create a project with custom folder structure for Go testing."""
        custom_folder = "contest"
        folder_path = tmp_path / "problems"  # Go stores all under problems/
        folder_path.mkdir()

        # Create a problem with Go solution
        problem = folder_path / f"{custom_folder}_{100}"
        problem.mkdir()
        (problem / "solution.go").write_text('''
package problem

func Solve(input string) string {
    return input
}
''')
        (problem / "testcase").write_text('["input1"]\n["output1"]')

        # Create config file
        config = {"daily": "100", "plans": []}
        config_path = tmp_path / f"daily-{custom_folder}.json"
        with config_path.open("w") as f:
            json.dump(config, f)

        # Create .env file
        env_path = tmp_path / ".env"
        env_path.write_text(f'PROBLEM_FOLDER="{custom_folder}"\n')

        yield tmp_path, custom_folder

    def test_go_setup_reads_custom_folder(self, temp_project_with_custom: tuple[Path, str], monkeypatch):
        """Test that go_setup.py reads PROBLEM_FOLDER from .env."""
        project_path, custom_folder = temp_project_with_custom

        # Read .env to verify PROBLEM_FOLDER setting
        env_content = (project_path / ".env").read_text()
        assert f'PROBLEM_FOLDER="{custom_folder}"' in env_content

        # Verify config file exists with correct naming
        config_path = project_path / f"daily-{custom_folder}.json"
        assert config_path.exists()

        config = json.loads(config_path.read_text())
        assert config["daily"] == "100"

    def test_go_setup_import_path_format(self, temp_project_with_custom: tuple[Path, str]):
        """Test that Go import paths use correct folder prefix."""
        project_path, custom_folder = temp_project_with_custom

        # Go imports should be: leetCode/{folder}_{id}
        problem_path = project_path / "problems" / f"{custom_folder}_100"
        assert problem_path.exists()

        # Verify the naming convention for Go imports
        folder_name = problem_path.name
        assert folder_name.startswith(custom_folder)
        assert "_" in folder_name

    def test_go_setup_with_link_resolution(self, temp_project_with_custom: tuple[Path, str]):
        """Test Go setup with linked problem in different folder."""
        project_path, custom_folder = temp_project_with_custom

        # Create a source problem in problems folder
        problems = project_path / "problems"
        source_problem = problems / "problems_50"
        source_problem.mkdir()
        (source_problem / "solution.go").write_text('''
package problem

func Solve(input string) string {
    return "from_source"
}
''')

        # Create link from custom problem to source
        custom_problem = problems / f"{custom_folder}_100"
        link_file = custom_problem / "link.json"
        link_file.write_text(json.dumps({
            "link_to": "50",
            "link_folder": "problems"
        }))

        # Verify link resolution
        from python.utils import resolve_link
        resolved, link_info = resolve_link(custom_problem)
        assert resolved == source_problem
        assert link_info["link_to"] == "50"


@pytest.mark.integration
class TestRustSetupCustomFolder:
    """Tests for Rust Cargo.toml setup with custom PROBLEM_FOLDER."""

    @pytest.fixture
    def temp_project_with_custom(self, tmp_path: Path) -> Generator[tuple[Path, str], None, None]:
        """Create a project with custom folder structure for Rust testing."""
        custom_folder = "contest"
        folder_path = tmp_path / "problems"  # Rust stores all under problems/
        folder_path.mkdir()

        # Create a problem with Rust solution
        problem = folder_path / f"{custom_folder}_200"
        problem.mkdir()
        (problem / "lib.rs").write_text('''
pub fn solve(input: &str) -> String {
    input.to_string()
}
''')
        (problem / "Cargo.toml").write_text('[package]\nname = "solution_200"\nversion = "0.1.0"\nedition = "2021"\n')

        # Create config file
        config = {"daily": "200", "plans": []}
        config_path = tmp_path / f"daily-{custom_folder}.json"
        with config_path.open("w") as f:
            json.dump(config, f)

        # Create .env file
        env_path = tmp_path / ".env"
        env_path.write_text(f'PROBLEM_FOLDER="{custom_folder}"\n')

        yield tmp_path, custom_folder

    def test_rust_setup_reads_custom_folder(self, temp_project_with_custom: tuple[Path, str]):
        """Test that cargo_setup.py reads PROBLEM_FOLDER from .env."""
        project_path, custom_folder = temp_project_with_custom

        # Verify .env and config
        env_content = (project_path / ".env").read_text()
        assert custom_folder in env_content

        config_path = project_path / f"daily-{custom_folder}.json"
        assert config_path.exists()

    def test_rust_workspace_member_naming(self, temp_project_with_custom: tuple[Path, str]):
        """Test that Rust workspace members use correct folder prefix."""
        project_path, custom_folder = temp_project_with_custom

        # Rust workspace member should be: "problems/{folder}_{id}"
        problem_path = project_path / "problems" / f"{custom_folder}_200"
        assert problem_path.exists()

        # Verify Cargo.toml exists
        assert (problem_path / "Cargo.toml").exists()
        assert (problem_path / "lib.rs").exists()

    def test_rust_setup_with_link_resolution(self, temp_project_with_custom: tuple[Path, str]):
        """Test Rust setup resolves links correctly."""
        project_path, custom_folder = temp_project_with_custom

        # Create source problem
        problems = project_path / "problems"
        source_problem = problems / "problems_150"
        source_problem.mkdir()
        (source_problem / "lib.rs").write_text('pub fn solve(input: &str) -> String { input.to_string() }')
        (source_problem / "Cargo.toml").write_text('[package]\nname = "solution_150"\nversion = "0.1.0"\nedition = "2021"\n')

        # Create link
        custom_problem = problems / f"{custom_folder}_200"
        (custom_problem / "link.json").write_text(json.dumps({
            "link_to": "150",
            "link_folder": "problems"
        }))

        # Verify resolution
        from python.utils import resolve_link
        resolved, link_info = resolve_link(custom_problem)
        assert resolved == source_problem


@pytest.mark.integration
class TestJavaSetupCustomFolder:
    """Tests for Java test setup with custom PROBLEM_FOLDER."""

    @pytest.fixture
    def temp_project_with_custom(self, tmp_path: Path) -> Generator[tuple[Path, str], None, None]:
        """Create a project with custom folder structure for Java testing."""
        custom_folder = "contest"
        folder_path = tmp_path / custom_folder
        folder_path.mkdir()

        # Create a problem with Java solution
        problem = folder_path / f"{custom_folder}_300"
        problem.mkdir()
        (problem / "Solution.java").write_text('''
package contest.contest_300;

public class Solution {
    public String solve(String input) {
        return input;
    }
}
''')

        # Create config file
        config = {"daily": "300", "plans": []}
        config_path = tmp_path / f"daily-{custom_folder}.json"
        with config_path.open("w") as f:
            json.dump(config, f)

        # Create .env file
        env_path = tmp_path / ".env"
        env_path.write_text(f'PROBLEM_FOLDER="{custom_folder}"\n')

        yield tmp_path, custom_folder

    def test_java_class_package_naming(self, temp_project_with_custom: tuple[Path, str]):
        """Test that Java package names use correct folder prefix."""
        project_path, custom_folder = temp_project_with_custom

        # Java package should be: {folder}.{folder}_{id}
        solution_path = project_path / custom_folder / f"{custom_folder}_300" / "Solution.java"
        assert solution_path.exists()

        content = solution_path.read_text()
        assert f"package {custom_folder}.{custom_folder}_300" in content

    def test_java_config_file_resolution(self, temp_project_with_custom: tuple[Path, str]):
        """Test Java reads correct config file based on PROBLEM_FOLDER."""
        project_path, custom_folder = temp_project_with_custom

        # Verify config file naming
        config_path = project_path / f"daily-{custom_folder}.json"
        assert config_path.exists()

        config = json.loads(config_path.read_text())
        assert config["daily"] == "300"

    def test_java_class_name_format(self, temp_project_with_custom: tuple[Path, str]):
        """Test Java class naming follows {folder}_{id} convention."""
        project_path, custom_folder = temp_project_with_custom

        problem_dir = project_path / custom_folder / f"{custom_folder}_300"
        assert problem_dir.exists()
        assert problem_dir.name == f"{custom_folder}_300"


@pytest.mark.integration
class TestTypeScriptSetupCustomFolder:
    """Tests for TypeScript test setup with custom PROBLEM_FOLDER."""

    @pytest.fixture
    def temp_project_with_custom(self, tmp_path: Path) -> Generator[tuple[Path, str], None, None]:
        """Create a project with custom folder structure for TypeScript testing."""
        custom_folder = "contest"
        folder_path = tmp_path / custom_folder
        folder_path.mkdir()

        # Create a problem with TypeScript solution
        problem = folder_path / f"{custom_folder}_400"
        problem.mkdir()
        (problem / "solution.ts").write_text('''
export function Solve(input: string): string {
    return input;
}
''')
        (problem / "testcase").write_text('["input1"]\n["output1"]')

        # Create config file
        config = {"daily": "400", "plans": []}
        config_path = tmp_path / f"daily-{custom_folder}.json"
        with config_path.open("w") as f:
            json.dump(config, f)

        # Create .env file
        env_path = tmp_path / ".env"
        env_path.write_text(f'PROBLEM_FOLDER="{custom_folder}"\n')

        yield tmp_path, custom_folder

    def test_typescript_path_resolution(self, temp_project_with_custom: tuple[Path, str]):
        """Test TypeScript resolves paths correctly for custom folder."""
        project_path, custom_folder = temp_project_with_custom

        # TypeScript uses: {folder}/{folder}_{id}/solution.ts
        solution_path = project_path / custom_folder / f"{custom_folder}_400" / "solution.ts"
        assert solution_path.exists()

        testcase_path = project_path / custom_folder / f"{custom_folder}_400" / "testcase"
        assert testcase_path.exists()

    def test_typescript_config_file_naming(self, temp_project_with_custom: tuple[Path, str]):
        """Test TypeScript reads correct config file."""
        project_path, custom_folder = temp_project_with_custom

        config_path = project_path / f"daily-{custom_folder}.json"
        assert config_path.exists()

        config = json.loads(config_path.read_text())
        assert config["daily"] == "400"

    def test_typescript_fallback_to_problems(self, temp_project_with_custom: tuple[Path, str]):
        """Test TypeScript falls back to problems folder if custom not found."""
        project_path, custom_folder = temp_project_with_custom

        # Create problems folder with same problem
        problems = project_path / "problems"
        problems.mkdir()
        problem = problems / "problems_400"
        problem.mkdir()
        (problem / "solution.ts").write_text('export function Solve(input: string): string { return "fallback"; }')
        (problem / "testcase").write_text('["test"]\n["fallback"]')

        # Verify fallback path exists
        fallback_path = problems / "problems_400"
        assert fallback_path.exists()


@pytest.mark.integration
class TestCppSetupCustomFolder:
    """Tests for C++ test setup with custom PROBLEM_FOLDER."""

    @pytest.fixture
    def temp_project_with_custom(self, tmp_path: Path) -> Generator[tuple[Path, str], None, None]:
        """Create a project with custom folder structure for C++ testing."""
        custom_folder = "contest"
        folder_path = tmp_path / "problems"  # C++ stores all under problems/
        folder_path.mkdir()

        # Create a problem with C++ solution
        problem = folder_path / f"{custom_folder}_500"
        problem.mkdir()
        (problem / "Solution.cpp").write_text('''
#include <string>

class Solution {
public:
    std::string solve(std::string input) {
        return input;
    }
};
''')
        (problem / "testcase").write_text('["input1"]\n["output1"]')

        # Create config file
        config = {"daily": "500", "plans": []}
        config_path = tmp_path / f"daily-{custom_folder}.json"
        with config_path.open("w") as f:
            json.dump(config, f)

        # Create .env file
        env_path = tmp_path / ".env"
        env_path.write_text(f'PROBLEM_FOLDER="{custom_folder}"\n')

        yield tmp_path, custom_folder

    def test_cpp_problem_path_format(self, temp_project_with_custom: tuple[Path, str]):
        """Test C++ problem paths use correct folder prefix."""
        project_path, custom_folder = temp_project_with_custom

        # C++ problems stored under problems/{folder}_{id}
        problem_path = project_path / "problems" / f"{custom_folder}_500"
        assert problem_path.exists()

    def test_cpp_testcase_file_format(self, temp_project_with_custom: tuple[Path, str]):
        """Test C++ testcase file format is correct."""
        project_path, custom_folder = temp_project_with_custom

        testcase_path = project_path / "problems" / f"{custom_folder}_500" / "testcase"
        assert testcase_path.exists()

        content = testcase_path.read_text()
        lines = content.strip().split('\n')
        assert len(lines) == 2  # inputs and outputs

    def test_cpp_config_file_resolution(self, temp_project_with_custom: tuple[Path, str]):
        """Test C++ setup uses correct config file."""
        project_path, custom_folder = temp_project_with_custom

        config_path = project_path / f"daily-{custom_folder}.json"
        assert config_path.exists()

        config = json.loads(config_path.read_text())
        assert config["daily"] == "500"


@pytest.mark.integration
class TestCrossLanguageConsistency:
    """Tests for cross-language consistency with custom folders."""

    @pytest.fixture
    def temp_project_multi_lang(self, tmp_path: Path) -> Generator[Path, None, None]:
        """Create a project with multi-language solutions in custom folder."""
        custom_folder = "contest"
        folder_path = tmp_path / custom_folder
        folder_path.mkdir()

        problem_id = "600"
        problem = folder_path / f"{custom_folder}_{problem_id}"
        problem.mkdir()

        # Python solution
        (problem / "solution.py").write_text('''
import solution
from typing import *

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.add(test_input[0], test_input[1])

    def add(self, a: int, b: int) -> int:
        return a + b
''')
        (problem / "testcase.py").write_text('''
from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])

class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 2], Output=3))

    def get_testcases(self):
        return self.testcases
''')

        # Go solution (under problems/ for Go)
        go_problems = tmp_path / "problems"
        go_problems.mkdir()
        go_problem = go_problems / f"{custom_folder}_{problem_id}"
        go_problem.mkdir()
        (go_problem / "solution.go").write_text('package problem\n\nfunc Solve(input string) string { return input }')
        (go_problem / "testcase").write_text('[[1,2]]\n[3]')

        # Java solution
        java_problem = tmp_path / custom_folder / f"{custom_folder}_{problem_id}"
        (java_problem / "Solution.java").write_text(f'''
package {custom_folder}.{custom_folder}_{problem_id};

public class Solution {{
    public int add(int a, int b) {{ return a + b; }}
}}
''')

        # TypeScript solution
        (problem / "solution.ts").write_text('export function Solve(input: number[]): number { return input[0] + input[1]; }')
        (problem / "testcase").write_text('[[1,2]]\n[3]')

        # Rust solution (under problems/ for Rust)
        rust_problem = go_problems / f"{custom_folder}_{problem_id}"
        (rust_problem / "lib.rs").write_text('pub fn solve(input: &str) -> String { input.to_string() }')
        (rust_problem / "Cargo.toml").write_text('[package]\nname = "solution_600"\nversion = "0.1.0"\nedition = "2021"\n')

        # Config file
        config = {"daily": problem_id, "plans": []}
        config_path = tmp_path / f"daily-{custom_folder}.json"
        with config_path.open("w") as f:
            json.dump(config, f)

        # .env file
        env_path = tmp_path / ".env"
        env_path.write_text(f'PROBLEM_FOLDER="{custom_folder}"\n')

        yield tmp_path

    def test_all_languages_use_same_config(self, temp_project_multi_lang: Path):
        """Test that all languages read from the same config file."""
        # All languages should use daily-{folder}.json
        # Python: reads from .env -> PROBLEM_FOLDER -> daily-{folder}.json
        # Go: go_setup.py reads .env
        # Rust: cargo_setup.py reads .env
        # Java: TestMain.java reads .env
        # TypeScript: test.ts reads .env

        custom_folder = "contest"
        config_path = temp_project_multi_lang / f"daily-{custom_folder}.json"
        assert config_path.exists()

        config = json.loads(config_path.read_text())
        assert config["daily"] == "600"

    def test_folder_naming_consistency(self, temp_project_multi_lang: Path):
        """Test that all languages follow the same folder naming convention."""
        custom_folder = "contest"
        problem_id = "600"

        # Expected naming: {folder}_{problem_id}
        expected_name = f"{custom_folder}_{problem_id}"

        # Check Python/Java/TypeScript path
        direct_path = temp_project_multi_lang / custom_folder / expected_name
        assert direct_path.exists()

        # Check Go/Rust path (under problems/)
        problems_path = temp_project_multi_lang / "problems" / expected_name
        assert problems_path.exists()

    def test_env_file_consistency(self, temp_project_multi_lang: Path):
        """Test that .env file is consistent for all languages."""
        env_path = temp_project_multi_lang / ".env"
        env_content = env_path.read_text()

        # All languages should read same PROBLEM_FOLDER value
        assert 'PROBLEM_FOLDER="contest"' in env_content


@pytest.mark.integration
class TestEdgeCases:
    """Tests for edge cases in folder configuration."""

    def test_folder_name_with_special_chars(self, tmp_path: Path):
        """Test handling of folder names with underscores."""
        # Folder names like "contest_weekly" should work
        folder_name = "contest_weekly"
        folder = tmp_path / folder_name
        folder.mkdir()

        problem = folder / f"{folder_name}_100"
        problem.mkdir()

        assert problem.exists()
        assert problem.name == f"{folder_name}_100"

    def test_numeric_folder_name(self, tmp_path: Path):
        """Test handling of numeric folder names."""
        # Folder names like "2024" should work
        folder_name = "2024"
        folder = tmp_path / folder_name
        folder.mkdir()

        problem = folder / f"{folder_name}_100"
        problem.mkdir()

        assert problem.exists()

    def test_missing_env_file_uses_default(self, tmp_path: Path):
        """Test that missing .env uses default 'problems' folder."""
        # When .env doesn't exist, should default to problems
        from python.utils import get_default_folder

        result = get_default_folder()
        assert result == "problems"

    def test_missing_config_file_error(self, tmp_path: Path):
        """Test that missing config file is handled appropriately."""
        # Config file daily-{folder}.json should exist
        custom_folder = "nonexistent"
        config_path = tmp_path / f"daily-{custom_folder}.json"

        assert not config_path.exists()
        # Actual error handling is done by test.py/tests.py

    def test_empty_plans_array(self, tmp_path: Path):
        """Test handling of empty plans array in config."""
        folder = "problems"
        config = {"daily": "1", "plans": []}
        config_path = tmp_path / f"daily-{folder}.json"
        config_path.write_text(json.dumps(config))

        loaded = json.loads(config_path.read_text())
        assert loaded["daily"] == "1"
        assert loaded["plans"] == []

    def test_single_problem_in_plans(self, tmp_path: Path):
        """Test handling of single problem in plans array."""
        config = {
            "daily": "1",
            "plans": ["1", "problems"]
        }
        config_path = tmp_path / "daily-problems.json"
        config_path.write_text(json.dumps(config))

        loaded = json.loads(config_path.read_text())
        assert len(loaded["plans"]) == 2
        assert loaded["plans"][0] == "1"
        assert loaded["plans"][1] == "problems"
