```python
# before starting this code we need Biopython so go to the python promt in my case its Anaconda prompt and just type 
#im oderd to install Biopython type pip install Biopython 
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
```

    WARNING: The default download format has changed from PDB to PDBx/mmCif
    

    Structure exists: 'C:\Users\Jaykishan\Desktop\xp\4xp1.cif' 
    

    c:\programdata\miniconda3\lib\site-packages\Bio\PDB\StructureBuilder.py:89: PDBConstructionWarning: WARNING: Chain A is discontinuous at line 7523.
      warnings.warn(
    c:\programdata\miniconda3\lib\site-packages\Bio\PDB\StructureBuilder.py:89: PDBConstructionWarning: WARNING: Chain L is discontinuous at line 7658.
      warnings.warn(
    c:\programdata\miniconda3\lib\site-packages\Bio\PDB\StructureBuilder.py:89: PDBConstructionWarning: WARNING: Chain A is discontinuous at line 7659.
      warnings.warn(
    c:\programdata\miniconda3\lib\site-packages\Bio\PDB\StructureBuilder.py:89: PDBConstructionWarning: WARNING: Chain L is discontinuous at line 7674.
      warnings.warn(
    c:\programdata\miniconda3\lib\site-packages\Bio\PDB\StructureBuilder.py:89: PDBConstructionWarning: WARNING: Chain H is discontinuous at line 7677.
      warnings.warn(
    


    NGLWidget()

