#!/usr/bin/env python3
"""
Test file to verify Claude Code is working in the correct directory.
Created: 2026-01-07
"""

import os
import sys
from pathlib import Path


def test_working_directory():
    """Verify we're in the correct project directory."""
    cwd = os.getcwd()
    print(f"✓ Current working directory: {cwd}")

    expected = "/workspace/src/active-project"
    assert cwd == expected, f"Expected {expected}, got {cwd}"
    print(f"✓ Working directory is correct!")


def test_project_structure():
    """Verify expected project structure exists."""
    expected_dirs = ['cert', 'logs', 'data', 'scripts', 'tools', 'docs', 'src', 'tests']
    expected_files = ['CLAUDE.md', 'requirements.txt']

    print("\nChecking project structure:")

    # Check directories
    for dir_name in expected_dirs:
        dir_path = Path(dir_name)
        assert dir_path.exists() and dir_path.is_dir(), f"Missing directory: {dir_name}"
        print(f"  ✓ {dir_name}/ exists")

    # Check files
    for file_name in expected_files:
        file_path = Path(file_name)
        assert file_path.exists() and file_path.is_file(), f"Missing file: {file_name}"
        print(f"  ✓ {file_name} exists")

    print("\n✓ All expected project structure verified!")


def test_resource_access():
    """Verify Claude can access project-level resources."""
    print("\nChecking resource access:")

    # Check if we can write to logs
    log_file = Path("logs/test_claude.log")
    log_file.write_text("Claude Code test log entry\n")
    print(f"  ✓ Can write to logs/ directory")

    # Check if we can read CLAUDE.md
    claude_md = Path("CLAUDE.md")
    content = claude_md.read_text()
    assert "active-project" in content, "CLAUDE.md doesn't contain expected content"
    print(f"  ✓ Can read CLAUDE.md ({len(content)} bytes)")

    # Check docs structure
    docs_path = Path("docs")
    arch_file = docs_path / "ARCHITECTURE.md"
    adr_dir = docs_path / "architectural_decisions"

    if arch_file.exists():
        print(f"  ✓ docs/ARCHITECTURE.md exists")
    if adr_dir.exists():
        print(f"  ✓ docs/architectural_decisions/ exists")

    print("\n✓ Resource access verified!")


def main():
    """Run all tests."""
    print("=" * 60)
    print("Claude Code Working Directory Test")
    print("=" * 60)
    print()

    try:
        test_working_directory()
        test_project_structure()
        test_resource_access()

        print("\n" + "=" * 60)
        print("✓ ALL TESTS PASSED - Claude is working correctly!")
        print("=" * 60)
        return 0

    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
