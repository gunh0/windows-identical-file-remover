# Windows Identical File Remover

### Overview

This Python code aims to remove large files that are identical to files in another directory. It looks for files in a specified directory (REMOVE_PATH), checks if they exist in another directory (ORIGIN_PATH), and if so, moves them to a trash folder (TRASH). If a file is not found in the ORIGIN_PATH, it can optionally be moved to a check folder (NEED_CHECK) for further inspection.

<br/>

### Env.

-   Python 3.9.7

```
# Make virtual env.
python -m venv venv

# Global variables
REMOVE_PATH = "{root directory path to be deleted}"
ORIGIN_PATH = "{source root directory path}"
TRASH = "{duplicate Files}"
NEED_CHECK = "{files that need to be verified}"
```

<br/>

### Usage

Set the REMOVE_PATH, ORIGIN_PATH, TRASH, and NEED_CHECK paths at the beginning of the script to the desired values.
Run the script using a Python interpreter.
Functionality:

The code defines a function "find_file" that takes two arguments, ORIGIN_PATH and remove_file_path. It walks through the ORIGIN_PATH and compares each file with remove_file_path. If a match is found, the function moves the remove_file_path to the TRASH directory.
The code then walks through the REMOVE_PATH and calls the find_file function for each file in the directory.
If a match is found, the code logs a message indicating that the file was found and moved to the TRASH directory. Otherwise, it logs a message indicating that the file was not found and optionally moves it to the NEED_CHECK directory.
The code logs messages to the console and a log file named "log.log" in the current working directory.

<br/>

### Note

The logging level is set to INFO which means that only INFO level messages and above will be logged. To change the logging level, modify the logger.setLevel(level=logging.INFO) line to the desired logging level.
The code is currently commented out to move files to the NEED_CHECK directory. If desired, uncomment the relevant lines to enable this functionality.
