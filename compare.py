from modeller import *

env = Environ()
aln = Alignment(env)
for (pdb, chain) in (('1u8z', 'A'), ('1c1y', 'A'), ('1kao', 'A'),
                     ('1g16', 'A'), ('1oix', 'A'), ('1xtq', 'A')):
    m = Model(env, file=pdb, model_segment=('FIRST:'+chain, 'LAST:'+chain))
    aln.append_model(m, atom_files=pdb, align_codes=pdb+chain)
aln.malign()
aln.malign3d()
aln.compare_structures()
aln.id_table(matrix_file='family.mat')
env.dendrogram(matrix_file='family.mat', cluster_cut=-1.0)
