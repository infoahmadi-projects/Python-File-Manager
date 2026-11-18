# Python File Manager

A simple, safe, and beginner-friendly command-line file manager built with Python. This project provides essential file and directory management operations through an easy-to-use command-line interface (CLI).

## Features

- **List Files & Directories:** Display the contents of a directory with file sizes and type indicators.
- **Create Directories:** Create new directories, including nested parent directories.
- **Create Text Files:** Create UTF-8 text files with optional initial content.
- **Rename Files & Directories:** Rename files and folders safely.
- **Copy Files & Directories:** Copy individual files or entire directories.
- **Move Files & Directories:** Move files and folders to a specified destination.
- **Search Files:** Recursively search for files and directories using filename patterns (glob).
- **Delete Files Safely:** Delete individual files only after explicit user confirmation.

## Technologies Used

- Python 3
- `argparse` – Command-line argument parsing
- `pathlib` – Filesystem path handling
- `shutil` – File and directory operations
- `sys` – Error output and program exit handling

**Dependencies:** No external packages are required. The project uses only Python's standard library.

## Project Structure

```text
Python-File-Manager/
│
├── file_manager.py
├── README.md
├── .gitignore
└── LICENSE
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/infoahmadi-projects/Python-File-Manager.git
```

2. Navigate to the project directory:

```bash
cd Python-File-Manager
```

3. Run the application:

```bash
python file_manager.py --help
```

## Usage

The application provides several commands for managing files and directories.

### 1. List Directory Contents

Display files and folders in the current directory:

```bash
python file_manager.py list .
```

### 2. Create a Directory

```bash
python file_manager.py mkdir ./work
```

### 3. Create a Text File

Create a new UTF-8 text file:

```bash
python file_manager.py create ./work/ideas.txt --content "My first file"
```

### 4. Rename a File or Directory

```bash
python file_manager.py rename ./work/ideas.txt notes.txt
```

### 5. Copy Files or Directories

```bash
python file_manager.py copy ./work/notes.txt ./backup/notes.txt
```

### 6. Move Files or Directories

```bash
python file_manager.py move ./work/notes.txt ./backup/notes.txt
```

### 7. Search for Files

Search recursively using filename patterns:

```bash
python file_manager.py search . --pattern "*.pdf"
```

You can also search for Python files:

```bash
python file_manager.py search . --pattern "*.py"
```

### 8. Delete a File

```bash
python file_manager.py delete ./backup/notes.txt
```

The application asks for explicit confirmation before deleting a file. Type `yes` to proceed.

## Safety Features

Safety is an important part of this project.

- Existing files and directories are not overwritten during create, copy, rename, or move operations.
- File deletion requires explicit user confirmation.
- Recursive directory deletion is intentionally disabled.
- File creation uses exclusive mode to prevent accidental overwriting.
- Invalid paths and filesystem errors are handled gracefully.

These safeguards help reduce the risk of accidental data loss.

## Error Handling

The application handles common filesystem and input-related errors, including:

- Missing files or directories
- Invalid directory operations
- Existing destination paths
- Invalid filenames
- Permission and filesystem errors

Errors are displayed in the standard error stream.

## Requirements

- Python 3.9 or later recommended.
- No third-party libraries required.

## Future Improvements

Potential improvements for future versions include:

- File information and metadata display
- Logging file operations
- Unit testing with `pytest`
- Improved interactive command-line interface
- Additional file filtering options

## Contributing

Contributions, suggestions, and bug reports are welcome.

If you would like to improve this project:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Open a Pull Request.

## License

This project is available under the MIT License. See the `LICENSE` file for details.

## Author

**ALI HOSSEIN AHMADI**

GitHub: [@infoahmadi-projects](https://github.com/infoahmadi-projects)

---

If you find this project useful, consider giving it a ⭐ on GitHub!
