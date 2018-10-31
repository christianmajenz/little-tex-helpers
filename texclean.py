#######################################################################################
## Script to remove tex auxiliary files                                              ##
## Use at your own risk!!!!!!!!!                                                     ##
## This script will e.g. remove .bbl files, as it assumes you use bibtex or similar. ##
#######################################################################################

import os


dir = "."
files = os.listdir(dir)
for file in files:
    if file.endswith(".bbl")|file.endswith(".aux")|file.endswith(".blg")|file.endswith(".fdb_latexmk")|file.endswith(".fls")|file.endswith(".log")|file.endswith(".out")|file.endswith(".run.xml")|file.endswith(".synctex.gz")|file.endswith("-blx.bib"):
        os.remove(os.path.join(dir,file))

