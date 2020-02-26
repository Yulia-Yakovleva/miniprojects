from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

import csv


protein_file = 'data/peptides_augustus.aa'
records = SeqIO.parse(protein_file, format="fasta")

rows = [['protein', 'best_ident', 'best_cov', 'best_e_value', 'hit_id', 'hid_def']]

for i, record in enumerate(records):
    print(i, ':', record.id)
    handle = NCBIWWW.qblast("blastp", "swissprot", record.seq)

    blast_records = NCBIXML.parse(handle)
    for blast_record in blast_records:

        if len(list(blast_record.alignments)) == 0:
            rows.append([record.id, '', '', '', '', ''])
        else:
            for alignment in blast_record.alignments:
                hsp = alignment.hsps[0]
                cov = hsp.align_length / blast_record.query_length
                ident = hsp.identities / hsp.align_length

                rows.append([record.id, hsp.expect, ident, cov, alignment.hit_id, alignment.hit_def])

with open('data/blast_result.csv', 'w') as f:
    wr = csv.writer(f)
    wr.writerows(rows)