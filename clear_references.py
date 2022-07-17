"""Remove duplicate and unused references from bib file."""

import os

thesis_folder = os.getcwd() + "/thesis"
path = thesis_folder + "/mybib.bib"
tex_files = [f for f in os.listdir(thesis_folder) if f.endswith(".tex")]

with open(path, "r+") as f:
    content = f.read()
    contents = content.split("\n\n")
    keys = [c.split(",")[0].split("{")[-1] for c in contents]
    # By turning into a dict with Bib entries as keys, we remove duplicates
    map_ = dict(zip(keys, contents))

# Now we remove the keys that do not appear in the tex files
new = dict()
for k, v in map_.items():
    FOUND = False
    for tex_file in tex_files:
        with open(f"{thesis_folder}/{tex_file}", "r") as f:
            content = f.read()
            if k in content:
                FOUND = True
    if FOUND:
        new[k] = v
    else:
        print(
            f"Reference {k} was removed, as it "
            "was not used in TeX files.")

new_content = "\n\n".join(list(new.values()))
with open(path, "w") as f:
    f.write(new_content)
