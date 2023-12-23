from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='1kao', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='1kaoA', atom_files='1kao.pdb')
aln.append(file='NP_001390169.ali', align_codes='NP001390169')
aln.align2d(max_gap_length=50)
aln.write(file='1kao-ras.ali', alignment_format='PIR')
aln.write(file='1kao-ras.pap', alignment_format='PAP')
