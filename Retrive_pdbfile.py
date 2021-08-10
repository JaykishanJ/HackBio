#before running this command please make sure you have installed Biopython
from Bio.PDB import *
pdbl = PDBList()
print("Please enter only 4 char pdb id")
structure=input("Enter pdb id: ")#get input from user
pdbl.retrieve_pdb_file(structure, pdir="E:\pdb", file_format = 'pdb')#make sure you change path according to what you 

