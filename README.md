import Bio
import nglview as nv 
from Bio.PDB import *
pdbl.retrieve_pdb_file('4xp1')
parser = MMCIFParser()
structure = parser.get_structure('4xp1', 'xp/4xp1.cif')
view = nv.show_biopython(structure)
view.clear_representations()
#view as ball and stick (atom and bond)
view.add_ball_and_stick()
view
