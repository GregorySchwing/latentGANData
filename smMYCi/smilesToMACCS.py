#!/usr/bin/env python
# coding: utf-8

# # Molecular Similarity

# ## Objectives

# - Generete molecular fingerprints for a given molecule.
# - Evaluate structural similarity between molecules using different molecular fingerpints and similarity metrics.

# Many useful documents/papers describe various aspects of molecular similarity, including molecular fingerprints and similarity measures.  Please read these if you need more details.

# - Getting Started with the RDKit in Python<br>
# (https://www.rdkit.org/docs/GettingStartedInPython.html#fingerprinting-and-molecular-similarity)
# 
# - Fingerprint Generation, GraphSim Toolkit 2.4.2<br>
# (https://docs.eyesopen.com/toolkits/python/graphsimtk/fingerprint.html)
# 
# - Chemical Fingerprints<br>
# (https://docs.chemaxon.com/display/docs/Chemical+Fingerprints)
# 
# - Extended-Connectivity Fingerprints<br>
# (https://doi.org/10.1021/ci100050t)
# 
# 

# ## 1. Fingerprint Generation

# In[39]:

# ### 1-(1) MACCS keys
# The MACCS key is a binary fingerprint (a string of 0's and 1's).  Each bit position represents the presence (=1) or absence (=0) of a pre-defined structural feature.  The feature definitions for the MACCS keys are available at:<br> https://github.com/rdkit/rdkit/blob/master/rdkit/Chem/MACCSkeys.py



from rdkit import Chem
#mol = Chem.MolFromSmiles('CC(C)C1=C(C(=C(N1CC[C@H](C[C@H](CC(=O)O)O)O)C2=CC=C(C=C2)F)C3=CC=CC=C3)C(=O)NC4=CC=CC=C4')
from rdkit.Chem import MACCSkeys
#fp = MACCSkeys.GenMACCSKeys(mol)
#fp.ToBitString()    # Alternative, easier way to convert it to a bitstring.

ids = []
smiles = []
maccs = []
import csv
with open('smiles2MACCS.csv', 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		ids.append(row[0])
		smiles.append(row[1])
		mol = Chem.MolFromSmiles(row[1])
		fp = MACCSkeys.GenMACCSKeys(mol)
		maccs.append(fp.ToBitString())
#print(ids)
#rows = zip(ids,maccs)
rows = zip(ids,smiles,maccs)
myfile = 'MACCS.csv'
with open(myfile, 'w', newline='') as f:
	writer = csv.writer(f)
	for row in rows:
		writer.writerow(row)
