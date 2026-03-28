# Log Analyzer and Extractor

A lightweight and efficient Python utility designed to parse and analyze system log files. This script tallies the occurrences of different log levels (INFO, WARNING, ERROR) and automatically extracts critical entries into a consolidated, easy-to-read report.

This project demonstrates the effective use of Python's **Context Managers (`with` statement)**, ensuring safe file handling and preventing resource leaks. It also implements lazy evaluation (reading files line-by-line) to process large-scale log files without exhausting system memory (RAM).

---

## Features

* **Test Log Generation:** Automatically creates a dummy `.log` file for immediate testing and validation.
* **Memory-Efficient Processing:** Processes files line by line, ensuring smooth operation even with gigabyte-sized log files.
* **Automated Error Extraction:** Isolates and compiles all `[ERROR]` messages into a dedicated output report.
* **Zero External Dependencies:** Built entirely with the Python Standard Library, requiring no additional package installations.

---

## Getting Started

This project is designed to be ready to run out of the box. Since it relies solely on the standard library, there is no need to set up complex virtual environments or install packages via `pip`.

### Prerequisites
* **Python 3.6 or higher** installed on your machine (required for Type Hints and the `pathlib` module).

### Execution

1. **Clone the repository** or download the source code to your local machine:
   ```bash
   git clone [https://github.com/your-username/log-analyzer.git](https://github.com/your-username/log-analyzer.git)
   cd log-analyzer
   ```

2. **Run the main script:**
   Open your terminal in the project directory and execute the following command:
   ```bash
   python analisador_logs.py
   ```

3. **Check the output:**
   Upon execution, the script will generate (or read) a `sistema.log` file and output the analysis into a new file named `relatorio_erros.txt` in the same directory.

---

## File Structure

* `analisador_logs.py`: The main source code containing the parsing and extraction logic.
* `sistema.log`: The sample log file automatically generated for testing purposes.
* `relatorio_erros.txt`: The final output report generated after the script runs.

---

## Customization

To analyze your own production log files instead of the test file:
1. Open `analisador_logs.py` in your text editor.
2. Comment out or remove the `gerar_log_de_exemplo(arquivo_log)` function call inside the `main()` block.
3. Update the `arquivo_log` variable path to point to your actual log file.
```