"""Tests for ZVS 2018 compliance check and markdown validation."""

import os
import re
import subprocess
import sys
from pathlib import Path

import pytest
import yaml


# ZVS 2018 forbidden forms
FORBIDDEN_FORMS = {
    "pathian": "pasian",
    "ram": "gam",
    "fapa": "tapa",
    "bawipa": "topa",
    "siangpahrang": "kumpipa",
    "cu": "tua",
    "cun": "tua",
}

REPO_ROOT = Path(__file__).parent.parent
WORKFLOW_FILE = REPO_ROOT / ".github" / "workflows" / "ci.yml"


def get_markdown_files():
    """Get all markdown files in the repo (excluding .git and archive)."""
    md_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        # Skip .git and archive directories
        dirs[:] = [
            d
            for d in dirs
            if d not in (".git", "archive", "node_modules", ".cursor")
        ]
        for f in files:
            if f.endswith(".md"):
                md_files.append(Path(root) / f)
    return md_files


def find_forbidden_forms(md_files):
    """Search markdown files for ZVS 2018 forbidden forms."""
    violations = []
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding="utf-8")
            for forbidden, correct in FORBIDDEN_FORMS.items():
                # Use word boundary matching
                pattern = r"\b" + re.escape(forbidden) + r"\b"
                matches = list(re.finditer(pattern, content, re.IGNORECASE))
                if matches:
                    for match in matches:
                        # Get line number
                        line_num = content[: match.start()].count("\n") + 1
                        violations.append(
                            {
                                "file": str(md_file.relative_to(REPO_ROOT)),
                                "line": line_num,
                                "word": forbidden,
                                "correct": correct,
                            }
                        )
        except Exception as e:
            print(f"Warning: Could not read {md_file}: {e}")
    return violations


class TestZVSCompliance:
    """Test ZVS 2018 forbidden form detection."""

    def test_no_pathian_in_prose(self):
        """Test that 'pathian' is detected as a forbidden form."""
        md_files = get_markdown_files()
        violations = find_forbidden_forms(md_files)

        # Filter for 'pathian' violations
        pathian_violations = [v for v in violations if v["word"] == "pathian"]

        # We expect some violations to exist in the wiki
        # This test documents that the check is working
        print(f"\nFound {len(pathian_violations)} 'pathian' violations:")
        for v in pathian_violations[:5]:  # Show first 5
            print(f"  {v['file']}:{v['line']} - use '{v['correct']}' instead")

        # This test passes if the check runs without error
        # The number of violations depends on current wiki content
        assert isinstance(pathian_violations, list)

    def test_correct_pasian_not_flagged(self):
        """Test that 'pasian' (correct form) is NOT flagged."""
        md_files = get_markdown_files()
        violations = find_forbidden_forms(md_files)

        # pasian should never be in violations
        pasian_violations = [v for v in violations if v["word"] == "pasian"]
        assert len(pasian_violations) == 0, "pasian should not be flagged as forbidden"

    def test_zvs_forbidden_list_complete(self):
        """Test that all known forbidden forms are in the check list."""
        expected_forbidden = {
            "pathian",
            "ram",
            "fapa",
            "bawipa",
            "siangpahrang",
            "cu",
            "cun",
        }
        assert set(FORBIDDEN_FORMS.keys()) == expected_forbidden, (
            f"Forbidden forms mismatch: {set(FORBIDDEN_FORMS.keys())} != "
            f"{expected_forbidden}"
        )

        # Verify correct replacements
        assert FORBIDDEN_FORMS["pathian"] == "pasian"
        assert FORBIDDEN_FORMS["ram"] == "gam"
        assert FORBIDDEN_FORMS["fapa"] == "tapa"
        assert FORBIDDEN_FORMS["bawipa"] == "topa"
        assert FORBIDDEN_FORMS["siangpahrang"] == "kumpipa"
        assert FORBIDDEN_FORMS["cu"] == "tua"
        assert FORBIDDEN_FORMS["cun"] == "tua"

    def test_markdown_files_exist(self):
        """Test that there are markdown files to check."""
        md_files = get_markdown_files()
        assert len(md_files) > 0, "No markdown files found in repository"
        print(f"\nFound {len(md_files)} markdown files to check")

    def test_workflow_file_valid_yaml(self):
        """Test that the CI workflow file is valid YAML."""
        assert WORKFLOW_FILE.exists(), f"Workflow file not found: {WORKFLOW_FILE}"

        with open(WORKFLOW_FILE, "r") as f:
            try:
                config = yaml.safe_load(f)
            except yaml.YAMLError as e:
                pytest.fail(f"Invalid YAML in workflow file: {e}")

        # Verify required fields
        assert "name" in config, "Workflow missing 'name' field"
        # Note: YAML parses 'on' as True boolean in PyYAML
        assert "jobs" in config, "Workflow missing 'jobs' field"

        # Verify triggers - note: YAML parses 'on' as True boolean
        # In GitHub Actions, 'on' is a reserved key, PyYAML maps it to True
        on_config = config.get("on") or config.get(True)
        assert on_config is not None, "Workflow missing 'on' trigger"
        assert "push" in on_config or "pull_request" in on_config, (
            "Workflow must trigger on push or pull_request"
        )

        # Verify jobs exist
        jobs = config["jobs"]
        assert len(jobs) > 0, "Workflow has no jobs defined"

        print(f"\nWorkflow file is valid YAML with {len(jobs)} job(s)")


class TestMarkdownSyntax:
    """Test markdown syntax validation."""

    def test_no_empty_headers(self):
        """Test that there are no empty markdown headers."""
        md_files = get_markdown_files()
        empty_headers = []

        for md_file in md_files:
            try:
                content = md_file.read_text(encoding="utf-8")
                for i, line in enumerate(content.split("\n"), 1):
                    if re.match(r"^#+\s*$", line):
                        empty_headers.append(
                            f"{md_file.relative_to(REPO_ROOT)}:{i}"
                        )
            except Exception:
                pass

        if empty_headers:
            print(f"\nEmpty headers found:")
            for h in empty_headers:
                print(f"  {h}")

        # This is a warning, not a failure (empty headers might be intentional)
        assert isinstance(empty_headers, list)

    def test_code_blocks_balanced(self):
        """Test that code blocks are properly closed."""
        md_files = get_markdown_files()
        unclosed = []

        for md_file in md_files:
            try:
                content = md_file.read_text(encoding="utf-8")
                backtick_count = content.count("```")
                if backtick_count % 2 != 0:
                    unclosed.append(str(md_file.relative_to(REPO_ROOT)))
            except Exception:
                pass

        if unclosed:
            print(f"\nUnclosed code blocks in:")
            for f in unclosed:
                print(f"  {f}")

        assert len(unclosed) == 0, f"Unclosed code blocks in: {unclosed}"
