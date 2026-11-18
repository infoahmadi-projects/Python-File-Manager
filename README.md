# Python File Manager

A command-line file manager built with Python's standard library.

## Features

- List files and folders with file sizes
- Create directories and UTF-8 text files
- Rename, copy, and move files or folders
- Search recursively using filename patterns
- Delete individual files after explicit confirmation

## Run

```bash
python file_manager.py --help
```

## Example commands

```bash
python file_manager.py list .
python file_manager.py mkdir ./work
python file_manager.py create ./work/ideas.txt --content "Portfolio project"
python file_manager.py rename ./work/ideas.txt notes.txt
python file_manager.py copy ./work/notes.txt ./backup/notes.txt
python file_manager.py search . --pattern "*.py"
python file_manager.py delete ./backup/notes.txt
```

## Safety

The program refuses to overwrite existing destinations. It requires typing `yes`
before deleting a file and does not support recursive directory deletion.
