# Protein-Structure-Prediction

Homology modeling done with the Modeller10.2 tool from Salilab at UCSF (https://salilab.org/modeller/). Homology modeling is the process of three-dimensional structure modeling of a protein with unknown structure with known related structures. "MODELLER implements comparative protein structure modeling by satisfaction of spatial restraints (3,4) and can perform many additional tasks, including de novo modeling of loops in protein structures, optimization of various models of protein structure with respect to a flexibly defined objective function, multiple alignments of protein sequences and/or structures, clustering, searching of sequence databases, comparison of protein structures, etc." (salilab). Download Modeller here: https://salilab.org/modeller/nonacademic.html


Our model protein [NP_001390169.1](https://www.ncbi.nlm.nih.gov/protein/NP_001390169.1/) is a mouse GTPase K-ras isoform with no experimentally verified 3D structure. Our template [1kaoA](https://www.rcsb.org/structure/1kao) is a human ras-related G-protein RAP2A with a known structure.

Both K-Ras and RAP2A proteins belong to the RAS family of proteins, which is a family of small GTPases. The RAS family of proteins function as molecular switches and are involved in cellular signaling pathways for cell growth and differentiation. They cycle between an inactive GDP-bound state and an active GTP-bound state. The activation of GTPases is regulated by guanine nucleotide exchange factors (GEFs) and GTPase activating proteins (GAP). GEFs facilitate the exchange of GDP to GTP and GAPs enhance the hydrolysis of GTP to GDP. GTP-bound RAS proteins have downstream effects on different pathways including MAPK (mitogen-activated protein kinase) pathways.

Download the .zip file > Run the scripts in the following order: a) build_profile.py b) compare.py c) align2d.py d) model-single.py e) evaluate_template.py f) evaluate_model.py g) dope_profile.py
