# Repo of Numbers
---
## Workflows

![Handle Issues](https://github.com/Xtha-Sunil/Numbers/actions/workflows/issue-raised.yml/badge.svg)
![Handle PR](https://github.com/Xtha-Sunil/Numbers/actions/workflows/pr-raised.yml/badge.svg)
![Merge PR](https://github.com/Xtha-Sunil/Numbers/actions/workflows/merger.yml/badge.svg)

# Contribution Guide

Thank you for considering contributing to this repository! Please follow the steps below to contribute a new number file:

## Steps to Contribute:

1. **Raise an Issue**
   - Before making any changes, create an issue in this repository with the title `Info of <number>`.
   - Replace `<number>` with the actual number you plan to contribute.
   - The issue ensures no one else is working on the same number.

2. **Create a New File**
   - Once the issue is approved, create a file named `<number>.txt`.
   - Replace `<number>` with the actual number (e.g., `5.txt` for number 5).

3. **File Content Format**
   The content of the file should be formatted as follows:
   ```
   Number : <digit>
   Word : <number in words>
   Binary : 0b<binary representation>
   Octal : 0o<octal representation>
   Hex : 0x<hexadecimal representation>
   ```

   **Example for the number 5:**
   ```
   Number : 5
   Word : Five
   Binary : 0b101
   Octal : 0o5
   Hex : 0x5
   ```

4. **Only One File Change**
   - Only change one file per commit, i.e., only one number per contribution.

5. **Check for Duplicates**
   - Before committing, check that the file for the number does not already exist in the repository.
   - Do not proceed with the commit if a file for that number is already present.

6. **Submit a Pull Request**
   - After completing the file, commit your changes and submit a pull request (PR) referencing the issue you created.

7. **Review Process**
   - Your PR will be reviewed, and any necessary feedback will be provided before merging.
   - Once approved, the PR will be merged, and the branch may be deleted.

Happy contributing!
