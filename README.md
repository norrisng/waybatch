# Waybatch

*A tool to batch archive URLs to the Wayback Machine*

---

## How to use

1. Place all URLs inside a text file in the root directory. The text file should have only one URL per line.

   Example:
   ```
   https://example.com
   https://github.com
   https://google.com
   ```
2. Run the following:
    ```bash
    cd waybatch 
    python waybatch filename.txt
    ```