# LucidLogs: Log Analyzer and Extractor

A lightweight, efficient Python utility designed to parse system log files, tally log levels (INFO, WARNING, ERROR), and extract critical error messages into a consolidated report. 

This project features both a core backend script for automated tasks and a Graphical User Interface (GUI) for easy desktop use. It demonstrates best practices in Python, including the use of Context Managers (`with` statements) for safe file handling, lazy evaluation for memory management, and a modular architecture.

---

## Features

* **Graphical User Interface (GUI):** A clean, intuitive desktop interface built with `tkinter` for seamlessly selecting input files and defining output destinations.
* **Memory-Efficient Processing:** Employs lazy evaluation to read logs line-by-line, allowing the processing of massive log files without exhausting system RAM.
* **Automated Error Extraction:** Isolates all `[ERROR]` entries and compiles them into a dedicated, readable text report.
* **Zero External Dependencies:** Built entirely using the Python Standard Library. No additional package installations via `pip` are required.
* **Separation of Concerns:** The GUI (frontend) is completely decoupled from the processing logic (backend), ensuring code maintainability and scalability.

---

## Prerequisites

* **Python 3.6 or higher** installed on your system.
* *Note for Linux users:* While `tkinter` is included in standard Python installations on Windows and macOS, some Linux distributions package it separately. You may need to install it via your package manager (e.g., `sudo apt-get install python3-tk` on Debian/Ubuntu).

---

## Getting Started

1. **Clone the repository:**
   Download the source code to your local machine:
   ```bash
   git clone [https://github.com/your-username/loglens.git](https://github.com/your-username/loglens.git)
   cd loglens
   ```

2. **Run the Graphical Interface (GUI):**
   To open the desktop application, execute:
   ```bash
   python interface.py
   ```
   Follow the on-screen prompts to select your target log file and the destination directory for the generated report.

3. **Run the Command Line Script (CLI):**
   If you prefer terminal execution or wish to integrate the tool into automated pipelines, run the core script directly:
   ```bash
   python analisador_logs.py
   ```
   *Note: Running the core script independently will automatically generate a sample `sistema.log` file in the directory for testing purposes.*

---

## Project Structure

* `analisador_logs.py`: The core processing logic and CLI execution script.
* `interface.py`: The `tkinter`-based Graphical User Interface.
* `sistema.log`: An auto-generated sample log (created when running the core script).
* `relatorio_erros.txt`: The standard output report containing analysis summaries and extracted errors.

---

## Customization

To use the CLI script with your own production logs rather than the test generator:
1. Open `analisador_logs.py` in your preferred code editor.
2. Comment out the `gerar_log_de_exemplo(arquivo_log)` function call within the `main()` block.
3. Update the `arquivo_log` variable to point to the absolute or relative path of your target log file.
```
