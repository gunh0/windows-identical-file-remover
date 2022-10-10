# windows-user-files-deduplication

<br/>

### Input

-   Specify two directory paths

<br/>

### Output

-   Scan and remove for each duplicate file

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
