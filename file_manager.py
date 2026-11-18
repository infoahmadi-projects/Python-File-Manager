#!/usr/bin/env python3
"""
A safe, beginner-friendly command-line file manager.

Features:
- List files and folders
- Create folders and text files
- Rename, copy, and move files
- Search by filename pattern
- Delete files only after explicit confirmation

This tool intentionally does not recursively delete directories.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def resolve_path(raw_path: str) -> Path:
    """Expand '~' and return an absolute path for predictable operations."""
    return Path(raw_path).expanduser().resolve()


def list_directory(target: Path) -> None:
    """Display directory entries with a simple type and size indicator."""
    if not target.exists():
        raise FileNotFoundError(f"Path does not exist: {target}")
    if not target.is_dir():
        raise NotADirectoryError(f"Not a directory: {target}")

    entries = sorted(target.iterdir(), key=lambda item: (item.is_file(), item.name.lower()))
    if not entries:
        print("This directory is empty.")
        return

    print(f"\nContents of: {target}\n")
    for entry in entries:
        if entry.is_dir():
            print(f"[DIR ] {entry.name}/")
        else:
            size = entry.stat().st_size
            print(f"[FILE] {entry.name:<35} {size:>10} bytes")


def create_directory(target: Path) -> None:
    """Create a directory, including any missing parent directories."""
    target.mkdir(parents=True, exist_ok=False)
    print(f"Directory created: {target}")


def create_file(target: Path, content: str) -> None:
    """Create a new UTF-8 text file without overwriting an existing file."""
    target.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive mode ('x') prevents accidental replacement of existing content.
    with target.open("x", encoding="utf-8") as file:
        file.write(content)
    print(f"File created: {target}")


def rename_path(source: Path, new_name: str) -> None:
    """Rename a file or directory within its current parent directory."""
    if not source.exists():
        raise FileNotFoundError(f"Source does not exist: {source}")

    # Treat the supplied value as a name, not an arbitrary destination path.
    if Path(new_name).name != new_name or new_name in {"", ".", ".."}:
        raise ValueError("Please provide a simple new name, not a path.")

    destination = source.with_name(new_name)
    if destination.exists():
        raise FileExistsError(f"Destination already exists: {destination}")

    source.rename(destination)
    print(f"Renamed to: {destination}")


def copy_path(source: Path, destination: Path) -> None:
    """Copy one file or directory while refusing to overwrite a destination."""
    if not source.exists():
        raise FileNotFoundError(f"Source does not exist: {source}")
    if destination.exists():
        raise FileExistsError(f"Destination already exists: {destination}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        shutil.copytree(source, destination)
    else:
        shutil.copy2(source, destination)
    print(f"Copied to: {destination}")


def move_path(source: Path, destination: Path) -> None:
    """Move a file or directory to a destination that does not yet exist."""
    if not source.exists():
        raise FileNotFoundError(f"Source does not exist: {source}")
    if destination.exists():
        raise FileExistsError(f"Destination already exists: {destination}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(source), str(destination))
    print(f"Moved to: {destination}")


def search_files(root: Path, pattern: str) -> None:
    """Recursively find files and folders matching a glob pattern."""
    if not root.exists() or not root.is_dir():
        raise NotADirectoryError(f"Search root must be an existing directory: {root}")

    matches = sorted(root.rglob(pattern))
    if not matches:
        print("No matching items found.")
        return

    for match in matches:
        print(match)


def delete_file(target: Path) -> None:
    """Delete a single file after a clear interactive confirmation."""
    if not target.exists():
        raise FileNotFoundError(f"Path does not exist: {target}")
    if target.is_dir():
        raise IsADirectoryError(
            "Directory deletion is disabled for safety. Delete individual files manually."
        )

    answer = input(f"Delete '{target}' permanently? Type 'yes' to confirm: ").strip().lower()
    if answer != "yes":
        print("Deletion cancelled.")
        return

    target.unlink()
    print(f"Deleted: {target}")


def build_parser() -> argparse.ArgumentParser:
    """Define the command-line interface and its subcommands."""
    parser = argparse.ArgumentParser(
        description="Manage files and folders from the command line."
    )
    commands = parser.add_subparsers(dest="command", required=True)

    list_cmd = commands.add_parser("list", help="List a directory")
    list_cmd.add_argument("path", nargs="?", default=".")

    mkdir_cmd = commands.add_parser("mkdir", help="Create a directory")
    mkdir_cmd.add_argument("path")

    create_cmd = commands.add_parser("create", help="Create a UTF-8 text file")
    create_cmd.add_argument("path")
    create_cmd.add_argument("--content", default="", help="Initial file content")

    rename_cmd = commands.add_parser("rename", help="Rename a file or directory")
    rename_cmd.add_argument("source")
    rename_cmd.add_argument("new_name")

    copy_cmd = commands.add_parser("copy", help="Copy a file or directory")
    copy_cmd.add_argument("source")
    copy_cmd.add_argument("destination")

    move_cmd = commands.add_parser("move", help="Move a file or directory")
    move_cmd.add_argument("source")
    move_cmd.add_argument("destination")

    search_cmd = commands.add_parser("search", help="Search by filename pattern")
    search_cmd.add_argument("root", nargs="?", default=".")
    search_cmd.add_argument("--pattern", required=True, help='For example "*.pdf"')

    delete_cmd = commands.add_parser("delete", help="Delete one file after confirmation")
    delete_cmd.add_argument("path")

    return parser


def main() -> int:
    """Parse arguments, dispatch the selected operation, and report errors."""
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "list":
            list_directory(resolve_path(args.path))
        elif args.command == "mkdir":
            create_directory(resolve_path(args.path))
        elif args.command == "create":
            create_file(resolve_path(args.path), args.content)
        elif args.command == "rename":
            rename_path(resolve_path(args.source), args.new_name)
        elif args.command == "copy":
            copy_path(resolve_path(args.source), resolve_path(args.destination))
        elif args.command == "move":
            move_path(resolve_path(args.source), resolve_path(args.destination))
        elif args.command == "search":
            search_files(resolve_path(args.root), args.pattern)
        elif args.command == "delete":
            delete_file(resolve_path(args.path))
        return 0
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
