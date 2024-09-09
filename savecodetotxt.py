import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Fonction pour créer les fichiers txt
def create_code_summary(root_dir, output_dir, excluded_items=[]):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    base_files_content = []  # Contenu des fichiers du dossier racine

    for folder_name, subfolders, filenames in os.walk(root_dir):
        # Convertir le chemin des dossiers et fichiers à leur forme absolue pour comparaison
        subfolders[:] = [d for d in subfolders if os.path.join(folder_name, d) not in excluded_items]
        filenames = [f for f in filenames if os.path.join(folder_name, f) not in excluded_items]

        relative_folder = os.path.relpath(folder_name, root_dir)

        # Fichiers dans le dossier racine (base)
        if relative_folder == ".":  # Si on est dans le dossier racine
            for filename in filenames:
                file_path = os.path.join(folder_name, filename)
                if file_path in excluded_items:
                    continue  # Exclure le fichier s'il est marqué pour exclusion
                try:
                    with open(file_path, 'r') as code_file:
                        code_content = code_file.read()
                    base_files_content.append(f"\n\n== File Name: {filename} ==\n")
                    base_files_content.append(f"File Source: {file_path}\n\n")
                    base_files_content.append(code_content)
                except Exception as e:
                    base_files_content.append(f"\n\n== File Name: {filename} ==\n")
                    base_files_content.append(f"File Source: {file_path}\n")
                    base_files_content.append(f"Erreur lors de la lecture du fichier : {e}\n")
        # Un seul fichier par dossier de premier niveau
        elif os.path.dirname(relative_folder) == "":  # Si c'est un dossier de premier niveau
            output_filename = os.path.basename(relative_folder) + ".txt"
            output_path = os.path.join(output_dir, output_filename)

            with open(output_path, 'w') as output_file:
                for dirpath, dirnames, files in os.walk(folder_name):
                    # Exclure les fichiers et sous-dossiers avec chemins relatifs au dossier sélectionné
                    dirnames[:] = [d for d in dirnames if os.path.join(dirpath, d) not in excluded_items]
                    files = [f for f in files if os.path.join(dirpath, f) not in excluded_items]

                    for filename in files:
                        file_path = os.path.join(dirpath, filename)
                        if file_path in excluded_items:
                            continue  # Exclure le fichier s'il est marqué pour exclusion
                        try:
                            with open(file_path, 'r') as code_file:
                                code_content = code_file.read()
                            output_file.write(f"\n\n== File Name: {filename} ==\n")
                            output_file.write(f"File Source: {file_path}\n\n")
                            output_file.write(code_content)
                        except Exception as e:
                            output_file.write(f"\n\n== File Name: {filename} ==\n")
                            output_file.write(f"File Source: {file_path}\n")
                            output_file.write(f"Erreur lors de la lecture du fichier : {e}\n")

    # Écrire le fichier base.txt avec les fichiers du dossier racine
    base_output_path = os.path.join(output_dir, "base.txt")
    with open(base_output_path, 'w') as base_output_file:
        base_output_file.writelines(base_files_content)

# Fonction pour exclure automatiquement node_modules et lire .gitignore
def handle_exclusions(root_dir):
    global excluded_items
    # Exclure automatiquement node_modules
    node_modules_path = os.path.join(root_dir, 'node_modules')
    if os.path.isdir(node_modules_path):
        excluded_items.append(node_modules_path)

    # Lire le fichier .gitignore s'il existe
    gitignore_path = os.path.join(root_dir, '.gitignore')
    if os.path.isfile(gitignore_path):
        with open(gitignore_path, 'r') as gitignore_file:
            for line in gitignore_file:
                line = line.strip()
                # Ignorer les commentaires et les lignes vides
                if not line or line.startswith("#"):
                    continue
                # Ajouter les chemins du .gitignore à la liste des exclusions
                exclude_path = os.path.join(root_dir, line)
                excluded_items.append(exclude_path)

# Fonction pour sélectionner un dossier
def select_directory():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_label.config(text=folder_selected)
        root_dir.set(folder_selected)
        handle_exclusions(folder_selected)  # Appeler la fonction pour gérer les exclusions automatiques
        update_tree_view(folder_selected)

# Fonction pour construire l'arborescence dans le Treeview
def update_tree_view(directory):
    tree_view.delete(*tree_view.get_children())  # Effacer l'arborescence actuelle

    def insert_items(parent, path):
        for item in os.listdir(path):
            abs_item = os.path.join(path, item)
            if os.path.isdir(abs_item):
                folder_id = tree_view.insert(parent, 'end', text=item, open=False)
                insert_items(folder_id, abs_item)  # Insertion récursive des sous-éléments
            else:
                tree_view.insert(parent, 'end', text=item, open=False)

    insert_items('', directory)

# Fonction pour exclure les éléments sélectionnés
def toggle_exclusion(item_id):
    item_text = tree_view.item(item_id, "text")
    # Utiliser un chemin relatif au dossier racine sélectionné
    item_path = os.path.join(root_dir.get(), get_item_path(item_id))
    
    if item_path in excluded_items:
        excluded_items.remove(item_path)
        tree_view.item(item_id, text=item_text.replace(" [X]", ""))  # Retirer la croix
    else:
        excluded_items.append(item_path)
        tree_view.item(item_id, text=item_text + " [X]")  # Ajouter la croix

    update_exclusion_list()

# Fonction pour récupérer le chemin complet d'un élément par rapport au dossier sélectionné
def get_item_path(item_id):
    path = []
    while item_id:
        path.append(tree_view.item(item_id, "text").replace(" [X]", ""))
        item_id = tree_view.parent(item_id)
    return os.path.join(*reversed(path))

# Fonction pour afficher les exclusions dans la liste
def update_exclusion_list():
    exclusion_listbox.delete(0, tk.END)
    for item in excluded_items:
        exclusion_listbox.insert(tk.END, item)

# Fonction principale pour exécuter le script
def execute_script():
    if not root_dir.get():
        messagebox.showerror("Erreur", "Veuillez sélectionner un dossier.")
        return

    output_directory_name = os.path.basename(root_dir.get()) + "_txt"
    output_directory = os.path.join(os.getcwd(), output_directory_name)

    create_code_summary(root_dir.get(), output_directory, excluded_items)
    messagebox.showinfo("Succès", f"Les fichiers txt ont été générés dans le dossier : {output_directory}")

# Interface principale
root = tk.Tk()
root.title("Sélecteur de projet")

root_dir = tk.StringVar()
excluded_items = []  # Liste des éléments exclus

# Texte explicatif
label = tk.Label(root, text="Choisissez un dossier pour analyser le code")
label.pack(pady=10)

# Bouton pour sélectionner le dossier
folder_label = tk.Label(root, text="Aucun dossier sélectionné", wraplength=400)
folder_label.pack(pady=10)

select_button = tk.Button(root, text="Sélectionner le dossier", command=select_directory)
select_button.pack(pady=10)

# Treeview pour afficher les dossiers et fichiers
tree_frame = tk.Frame(root)
tree_frame.pack(fill=tk.BOTH, expand=True)

tree_view = ttk.Treeview(tree_frame)
tree_view.pack(fill=tk.BOTH, expand=True)

# Ajout d'un événement lors du clic sur un élément pour exclure/inclure
tree_view.bind("<Double-1>", lambda event: toggle_exclusion(tree_view.focus()))

# Liste pour afficher les exclusions sélectionnées
exclusion_listbox = tk.Listbox(root, height=10)
exclusion_listbox.pack(pady=10)

# Bouton pour générer les fichiers txt
execute_button = tk.Button(root, text="Générer les fichiers txt", command=execute_script)
execute_button.pack(pady=20)

root.mainloop()
