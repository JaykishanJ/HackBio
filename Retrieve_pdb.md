#before running this command please make sure you have installed Biopython
from Bio.PDB import *
pdbl = PDBList()
print("Please enter only 4 char pdb id")
#get input from user
structure=input("Enter pdb id: ")
#make sure you change path according to where you want to save your file 
pdbl.retrieve_pdb_file(structure, pdir="E:\pdb", file_format = 'pdb')
