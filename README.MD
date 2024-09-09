<<<<<<< HEAD
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
=======
SaveCodeToTXT
🇬🇧 Save all your code in a text file for ChatGPT fine-tuning.

SaveCodeToTXT is a Python tool that allows you to save all your code into text files for later use in fine-tuning ChatGPT models, or simply to keep a readable archive of your code.

With SaveCodeToTXT, you can easily generate .txt files for all the files in your project. You also have the ability to exclude certain files or directories with a simple click.

Features
Save all your project’s code: Generate text files containing your code for all directories in your project.
Easily exclude files/directories: Double-click on a file or directory to exclude it from the generation.
Automatic exclusions: The node_modules folder and files specified in a .gitignore are automatically excluded.
User-friendly interface: An intuitive user interface built with Tkinter.
Use Cases
Storing code for ChatGPT fine-tuning
You can use this tool to generate .txt files containing all your code, which you can then use to fine-tune a GPT model by loading these files into a training environment.

Building your own GPT model
If you are working on a large project with a lot of code, this tool helps you create a structured text dataset with all your code. You can use this dataset to create or fine-tune a GPT model that understands your codebase.

Installation
Before using SaveCodeToTXT, you need to install Tkinter (if it's not already installed).

For Ubuntu / Debian:
bash
Copier le code
sudo apt-get install python3-tk
For macOS with Homebrew:
bash
Copier le code
brew install python-tk
For Windows:
Tkinter is usually included with the standard installation of Python on Windows. If not, ensure you have installed Python via the official method.

Usage
Clone or download this project:

bash
Copier le code
git clone https://github.com/your-username/SaveCodeToTXT.git
Navigate to the project folder:

bash
Copier le code
cd SaveCodeToTXT
Run the tool by executing the Python script:

bash
Copier le code
python3 savecodetotxt.py
A window will open. You can select the project folder you want to analyze.

To exclude files or directories:

Double-click on a file or directory to add an [X] next to its name. This means it will not be included in the .txt generation.
To include a previously excluded file or directory, double-click again to remove the [X].
Click the Generate txt files button. The .txt files will be created in a folder named your-project_txt in the current directory.

Technical Details
The generated .txt files contain the code of each file, organized to include:

The file name.
The file path.
The file content.
A base.txt file collects all files in the root directory.

Each top-level directory generates a single .txt file, combining all files and subdirectories into one.

Automatic Exclusions
When selecting a project folder, the program automatically ignores the following directories and files:

node_modules: This folder is ignored by default to avoid including unnecessary dependencies.
Files listed in .gitignore: If a .gitignore file exists in the selected root directory, all files and folders listed within are automatically excluded.
Contributing
Contributions are welcome! If you'd like to contribute to this project, feel free to fork it, create a feature branch, and then submit a pull request.

Fork the project.
Create your feature branch (git checkout -b my-new-feature).
Commit your changes (git commit -am 'Add new feature').
Push the branch (git push origin my-new-feature).
Open a pull request for review.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

SaveCodeToTXT
🇫🇷 Sauvegardez tout votre code dans un fichier texte pour l'entraînement de ChatGPT.

SaveCodeToTXT est un outil Python qui vous permet de sauvegarder tout votre code dans des fichiers texte pour une utilisation ultérieure dans des tâches d'ajustement de modèles ChatGPT, ou simplement pour conserver une archive lisible de votre code.

Avec SaveCodeToTXT, vous pouvez facilement générer des fichiers .txt pour tous les fichiers de votre projet. Vous avez également la possibilité d'exclure certains fichiers ou dossiers en quelques clics.

Fonctionnalités
Sauvegardez tout le code de votre projet : Générez des fichiers texte contenant votre code pour tous les répertoires de votre projet.
Exclure facilement des fichiers/dossiers : Double-cliquez sur un fichier ou un dossier pour l'exclure de la génération.
Exclusions automatiques : Le dossier node_modules et les fichiers mentionnés dans un fichier .gitignore sont automatiquement exclus.
Interface conviviale : Une interface utilisateur intuitive construite avec Tkinter.
Cas d'usage
Enregistrer du code pour l'entraînement de ChatGPT
Vous pouvez utiliser cet outil pour générer des fichiers .txt contenant tout votre code, que vous pourrez ensuite utiliser pour entraîner ou ajuster un modèle GPT en chargeant ces fichiers dans un environnement d'entraînement.

Créer votre propre modèle GPT
Si vous travaillez sur un projet complexe avec beaucoup de code, cet outil vous aide à créer un jeu de données textuel structuré avec tout votre code. Vous pouvez utiliser ce jeu de données pour créer ou ajuster un modèle GPT qui comprend votre base de code.

Installation
Avant d'utiliser SaveCodeToTXT, vous devez installer Tkinter (si ce n'est pas déjà fait).

Pour Ubuntu / Debian :
bash
Copier le code
sudo apt-get install python3-tk
Pour macOS avec Homebrew :
bash
Copier le code
brew install python-tk
Pour Windows :
Tkinter est généralement inclus avec l'installation standard de Python sur Windows. Sinon, assurez-vous d'avoir installé Python via la méthode officielle.

Utilisation
Clonez ou téléchargez ce projet :

bash
Copier le code
git clone https://github.com/votre-utilisateur/SaveCodeToTXT.git
Allez dans le répertoire du projet :

bash
Copier le code
cd SaveCodeToTXT
Lancez l'outil en exécutant le script Python :

bash
Copier le code
python3 savecodetotxt.py
Une fenêtre s'ouvre. Vous pouvez sélectionner le dossier de votre projet à analyser.

Pour exclure des fichiers ou des dossiers :

Double-cliquez sur un fichier ou un dossier pour ajouter une croix [X] à côté de son nom. Cela signifie qu'il ne sera pas pris en compte dans la génération des fichiers .txt.
Si vous souhaitez réintégrer un fichier ou un dossier, double-cliquez à nouveau pour retirer la croix.
Cliquez sur le bouton Générer les fichiers txt. Les fichiers .txt seront créés dans un dossier nommé votre-projet_txt dans le répertoire courant.

Détails techniques
Les fichiers .txt générés contiennent le code de chaque fichier, organisé de manière à inclure :

Le nom du fichier.
Le chemin d'accès au fichier.
Le contenu du fichier.
Un fichier base.txt regroupe tous les fichiers situés dans le dossier racine sélectionné.

Chaque dossier de premier niveau génère un fichier .txt unique, fusionnant tous les fichiers et sous-dossiers en un seul.

Exclusions automatiques
Lorsque vous sélectionnez un projet, le programme ignore automatiquement les répertoires et fichiers suivants :

node_modules : Ce dossier est ignoré par défaut pour éviter d'inclure des dépendances inutiles.
Fichiers listés dans .gitignore : Si un fichier .gitignore existe dans le répertoire racine sélectionné, tous les fichiers et dossiers listés sont automatiquement exclus.
Contribuer
Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, n'hésitez pas à faire un fork, créer une branche de fonctionnalité, puis soumettre une pull request.

Forkez ce projet.
Créez votre branche de fonctionnalité (git checkout -b ma-nouvelle-fonctionnalite).
Committez vos modifications (git commit -am 'Ajoute une nouvelle fonctionnalité').
Poussez la branche (git push origin ma-nouvelle-fonctionnalite).
Ouvrez une pull request pour examen.
Licence
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.

>>>>>>> ab676e37d8de6139eb255c4fae613e341b4c70d2
