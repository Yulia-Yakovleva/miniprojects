from Bio import Entrez
from Bio import SeqIO

acc_file = '/home/yulia/Downloads/sequences.acc'

Entrez.email='yakovleva.spbu@mail.com'

accs = list()
with open('/home/yulia/Downloads/sequences.acc', 'r') as in_f:
    for line in in_f:
        line = line.strip()
        accs.append(line)

with Entrez.efetch(db='nucleotide', rettype='gb',
                    retmode='text', id=', '.join(accs)) as handle:
    seq_records = SeqIO.parse(handle, 'gb')
    for rec in seq_records:
        for feature in rec.features:
            for key, val in feature.qualifiers.items():
                if 'surface glycoprotein' in str(val):
                    print(f'>{rec.id}')
                    print(feature.extract(rec.seq))