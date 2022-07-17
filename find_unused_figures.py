"""Go through all files in ./Figures and check if they are imported."""
import os


thesis_folder = os.getcwd() + "/thesis"
fig_folder = thesis_folder + "/Figures"

figures = [
    f for f in os.listdir(fig_folder)
    if any(f.endswith(ext) for ext in ['.pdf', '.png', '.jpeg', '.jpg'])
]
tex_files = [f for f in os.listdir(thesis_folder) if f.endswith(".tex")]

for fig in figures:
    FOUND = False
    for tex_file in tex_files:
        with open(f"{thesis_folder}/{tex_file}", "r") as f:
            content = f.read()
        if fig in content:
            FOUND = True
    if not FOUND:
        os.remove(f"{fig_folder}/{fig}")
        print(f"{fig} was removed, as it was not used in TeX files.")
