# Waybatch

*A tool to batch archive URLs to the Wayback Machine*

**Note:** for the non-technically minded, please refer to the "Executable" subsection under "Usage"

## Download

See the GitHub [releases](https://github.com/norrisng/waybatch/releases) page for precompiled Windows binaries (i.e. EXEs).

## URL file

Waybatch reads URLs from a text file. This text file should have only one URL per line.

Example:
```
https://example.com
https://github.com
https://google.com
```

## Usage

### Python

```shell
cd waybatch
python waybatch.py filename.txt
```

### Executable

1. Open Command Prompt, and navigate to the same directory as the executable file:

    ```
    cd "C:\Users\Username\Where\You\Placed\The\Exe"   
    ```

2. Run the following. For ease of use, your URL file should be in the same folder as the executable:
    ```
    waybatch filename.txt
    ```