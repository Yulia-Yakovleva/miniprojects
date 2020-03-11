import glob
from Bio import SeqIO

folder = 'data/Human'

all_contigs = []
for file in glob.glob(f'{folder}/*.fasta'):
    if file.endswith('merged.fasta'): continue
    print(file)

    all_contigs += [contig for contig in SeqIO.parse(open(file), 'fasta')]

SeqIO.write(all_contigs, open(f'{folder}/merged.fasta', 'w'), 'fasta')