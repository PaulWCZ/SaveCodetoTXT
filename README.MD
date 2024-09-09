# SaveCodeToTXT

## 🇬🇧 Save all your code in a text file for ChatGPT fine-tuning.

SaveCodeToTXT is a Python tool that allows you to save all your code into text files for later use in fine-tuning ChatGPT models or simply to maintain a readable archive of your code. This tool helps developers create text datasets from their code, which can be used for training GPT models or for storing code in an organized manner.

---

## Table of Contents
- [Features](#features)
- [Use Cases](#use-cases)
- [Installation](#installation)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [Automatic Exclusions](#automatic-exclusions)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Save all your project’s code:** Generate `.txt` files containing your code for all directories in your project.
- **Easily exclude files/directories:** Double-click on a file or directory to exclude it from the generation.
- **Automatic exclusions:** Automatically excludes the `node_modules` folder and files specified in `.gitignore`.
- **User-friendly interface:** Includes an intuitive user interface built with Tkinter.

---

## Use Cases

### Storing Code for ChatGPT Fine-tuning
Generate `.txt` files containing your entire project’s code, which can then be used for training or fine-tuning GPT models by loading them into a training environment.

### Building Your Own GPT Model
For large projects with many code files, SaveCodeToTXT helps you create structured text datasets of your codebase. This can be useful if you are training your own model to understand your project’s specific code style and structure.

---

## Installation

Before using SaveCodeToTXT, ensure Tkinter is installed on your system.

### For Ubuntu / Debian:
\`\`\`bash
sudo apt-get install python3-tk
\`\`\`

### For macOS with Homebrew:
\`\`\`bash
brew install python-tk
\`\`\`

### For Windows:
Tkinter is usually included with the standard installation of Python. If not, install Python from the official site and ensure Tkinter is included.

---

## Usage

### 1. Clone or download the project:
\`\`\`bash
git clone https://github.com/your-username/SaveCodeToTXT.git
\`\`\`

### 2. Navigate to the project folder:
\`\`\`bash
cd SaveCodeToTXT
\`\`\`

### 3. Run the tool:
\`\`\`bash
python3 savecodetotxt.py
\`\`\`

A window will open, where you can select the project folder to analyze.

### 4. Excluding files or directories:
- Double-click on a file or directory to add an `[X]` next to its name. This indicates that it will be excluded from the `.txt` generation.
- Double-click again to remove the `[X]` and include the file or directory.

### 5. Generating the `.txt` files:
Click the "Generate txt files" button. The `.txt` files will be created in a folder named `your-project_txt` within the current directory.

---

## Technical Details

The generated `.txt` files are organized as follows:
- **File Name:** Each text file is named after the source code file.
- **File Path:** The text file includes the original file path for easy reference.
- **File Content:** The content of each file is stored in the `.txt`.

Additionally:
- A `base.txt` file collects all files from the root directory.
- Each top-level directory generates a single `.txt` file combining all files and subdirectories into one.

---

## Automatic Exclusions

The following directories and files are automatically excluded when selecting a project folder:

- **node_modules:** Ignored by default to avoid unnecessary dependencies.
- **.gitignore files:** Files and directories listed in the `.gitignore` are automatically excluded.

---

## Contributing

Contributions are welcome! To contribute to SaveCodeToTXT, follow these steps:

1. Fork the project.
2. Create your feature branch:
\`\`\`bash
git checkout -b my-new-feature
\`\`\`

3. Commit your changes:
\`\`\`bash
git commit -am 'Add new feature'
\`\`\`

4. Push the branch:
\`\`\`bash
git push origin my-new-feature
\`\`\`

5. Open a pull request for review.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
