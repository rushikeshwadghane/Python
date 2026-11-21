# Python Practice

A collection of standalone programming exercises, primarily in Python, with a few JavaScript and TypeScript examples. The repository is a learning archive, not an installable application.

## Topics

- Python fundamentals, functions, classes, decorators, generators, and exceptions
- Lists, dictionaries, sets, stacks, queues, and linked lists
- Searching, sorting, strings, arrays, and common algorithm exercises
- JavaScript callbacks, Promises, async/await, and array operations
- An Angular parent/child component communication example

Examples are kept as separate scripts so they can be explored individually. Filenames describe the example where possible; not every exercise has a shared API or test suite.

## Run an example

Install Python 3, then run a script from the repository root:

```powershell
python .\three_sum.py
```

Or on Linux/macOS:

```bash
python3 three_sum.py
```

Some scripts prompt for input. A few use optional third-party packages, including pandas, OpenCV, pytesseract, pdf2image, Graphviz, requests, Beautiful Soup, and lxml. Install only the dependencies required by the script you want to run; there is no shared dependency manifest yet.

## Examples

| File | Description |
|---|---|
| `three_sum.py`, `four_sum.py` | Sum-to-target array exercises |
| `binary_search_example.py`, `first_occurrence_binary_search.py` | Binary search examples |
| `singly_linked_list.py`, `reverse_linked_list.py` | Linked-list exercises |
| `longest_substring_two_distinct.py` | Sliding-window substring exercise |
| `pan_card_ocr.py` | Local OCR example for user-supplied image/PDF files |
| `trial_balance_export.py` | Creates an Excel report from synthetic sample data |

Most source files include a short module docstring describing their purpose. Some examples are exploratory and may need further testing or refinement.

## Notes

- File-based examples are intended to be run independently.
- `pan_card_ocr.py` requires local OCR tools and dependencies; it does not select or read a directory unless you provide one on the command line.
- Generated Python bytecode and spreadsheet output are excluded by `.gitignore`.
- The examples are educational and are not production-ready financial or personal-data processing tools.
