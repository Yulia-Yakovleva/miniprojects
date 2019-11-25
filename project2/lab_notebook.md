## 1. Inspect raw sequencing data with fastqc

Time:  
`Sun Nov 24 16:54:41 MSK 2019`

Command:  
`fastqc -o . SRR1705851.fastq.gz`

Output:
```
Started analysis of SRR1705851.fastq.gz
Approx 5% complete for SRR1705851.fastq.gz
Approx 10% complete for SRR1705851.fastq.gz
Approx 15% complete for SRR1705851.fastq.gz
Approx 20% complete for SRR1705851.fastq.gz
Approx 25% complete for SRR1705851.fastq.gz
Approx 30% complete for SRR1705851.fastq.gz
Approx 35% complete for SRR1705851.fastq.gz
Approx 40% complete for SRR1705851.fastq.gz
Approx 45% complete for SRR1705851.fastq.gz
Approx 50% complete for SRR1705851.fastq.gz
Approx 55% complete for SRR1705851.fastq.gz
Approx 60% complete for SRR1705851.fastq.gz
Approx 65% complete for SRR1705851.fastq.gz
Approx 70% complete for SRR1705851.fastq.gz
Approx 75% complete for SRR1705851.fastq.gz
Approx 80% complete for SRR1705851.fastq.gz
Approx 85% complete for SRR1705851.fastq.gz
Approx 90% complete for SRR1705851.fastq.gz
Approx 95% complete for SRR1705851.fastq.gz
Analysis complete for SRR1705851.fastq.gz
```

## 2. Align your roommate’s data to the reference sequence

### Indexing reference file

Time:  
`Sat Nov 23 15:42:36 MSK 2019`

Command:  
`bwa index Influenza_A_virus_A_USA_RVD1_H3_H3N2.fasta`

Output:  
```
[bwa_index] Pack FASTA... 0.00 sec
[bwa_index] Construct BWT for the packed sequence...
[bwa_index] 0.00 seconds elapse.
[bwa_index] Update BWT... 0.00 sec
[bwa_index] Pack forward-only FASTA... 0.00 sec
[bwa_index] Construct SA from BWT and Occ... 0.00 sec
[main] Version: 0.7.17-r1188
[main] CMD: bwa index Influenza_A_virus_A_USA_RVD1_H3_H3N2.fasta
[main] Real time: 0.017 sec; CPU: 0.012 sec
```

### Running alignment with mpileup

Time:  
`Sun Nov 24 16:31:40 MSK 2019`

Command:  
`bwa mem Influenza_A_virus_A_USA_RVD1_H3_H3N2.fasta SRR1705851.fastq.gz | samtools view -S -b - | samtools sort - -o SRR1705851_alignment_sorted.bam`

Output:
```
[M::bwa_idx_load_from_disk] read 0 ALT contigs
[M::process] read 68388 sequences (10000129 bp)...
[M::process] read 67628 sequences (10000233 bp)...
[M::mem_process_seqs] Processed 68388 reads in 2.378 CPU sec, 2.216 real sec
[M::process] read 67698 sequences (10000046 bp)...
[M::mem_process_seqs] Processed 67628 reads in 1.883 CPU sec, 1.684 real sec
[M::process] read 67652 sequences (10000169 bp)...
[M::mem_process_seqs] Processed 67698 reads in 2.413 CPU sec, 2.209 real sec
[M::process] read 68072 sequences (10000295 bp)...
[M::mem_process_seqs] Processed 67652 reads in 2.360 CPU sec, 2.157 real sec
[M::process] read 18827 sequences (2716992 bp)...
[M::mem_process_seqs] Processed 68072 reads in 2.006 CPU sec, 1.874 real sec
[M::mem_process_seqs] Processed 18827 reads in 0.974 CPU sec, 0.883 real sec
[main] Version: 0.7.17-r1188
[main] CMD: bwa mem Influenza_A_virus_A_USA_RVD1_H3_H3N2.fasta SRR1705851.fastq.gz
[main] Real time: 11.669 sec; CPU: 12.234 sec
```

### Statictics

Time:  
`Sun Nov 24 16:35:54 MSK 2019`

Command:  
`samtools flagstat SRR1705851_alignment_sorted.bam`

Output:  
```
361349 + 0 in total (QC-passed reads + QC-failed reads)
0 + 0 secondary
3084 + 0 supplementary
0 + 0 duplicates
361116 + 0 mapped (99.94% : N/A)
0 + 0 paired in sequencing
0 + 0 read1
0 + 0 read2
0 + 0 properly paired (N/A : N/A)
0 + 0 with itself and mate mapped
0 + 0 singletons (N/A : N/A)
0 + 0 with mate mapped to a different chr
0 + 0 with mate mapped to a different chr (mapQ>=5)
```

## 3. Look for common variants with VarScan

### Indexing the bam file

Time:  
`Sun Nov 24 17:11:10 MSK 2019`

Command:  
`samtools index alignment_sorted.bam`

Output:
```
```

### Counting average and maximum coverage 

> (What is the desired value of d if we want to keep all possible variants, given the length of the reference sequence, the number of reads, and the average read length?)

Average coverage can be calculated as:  
average_contig_len * number_of_contigs / reference_len = 149 * 360000 / 1665 ~ 32000

But we can find **actual maximum** coverage with *samtools depth* and *awk*:


Time:  
`Sun Nov 24 17:33:56 MSK 2019`

Command:  
`samtools depth -d 1000000 SRR1705851_alignment_sorted.bam | awk 'BEGIN{a=   0}{if ($3>0+a) a=$3} END{print a}'`

Output:
```
44522
```


### Running VarScan

Time:  
`Sun Nov 24 17:39:13 MSK 2019`

Command:  
`samtools mpileup -d 45000 -f Influenza_A_virus_A_USA_RVD1_H3_H3N2.fasta SRR1705851_alignment_sorted.bam | java -jar VarScan.v2.4.0.jar mpileup2snp --min-var-freq 0.95 --variants --output-vcf 1 > VarScan_results_0_95.vcf`

Output:
```
[mpileup] 1 samples in 1 input files
Only SNPs will be reported
Warning: No p-value threshold provided, so p-values will not be calculated
Min coverage:	8
Min reads2:	2
Min var freq:	0.95
Min avg qual:	15
P-value thresh:	0.01
Input stream not ready, waiting for 5 seconds...
Reading input from STDIN
1665 bases in pileup file
5 variant positions (5 SNP, 0 indel)
0 were failed by the strand-filter
5 variant positions reported (5 SNP, 0 indel)
```

### Pull out the variants

Time:  
`Sun Nov 24 17:50:57 MSK 2019`

Command:  
`cat VarScan_results_0_95.vcf | awk 'NR>24 {split($10,a,":"); print $1, $2, $4, $5, a[7]}'`

Output:
```
KF848938.1 72 A G 99.96%
KF848938.1 117 C T 99.82%
KF848938.1 774 T C 99.96%
KF848938.1 999 C T 99.86%
KF848938.1 1260 A C 99.94%
```


## 4. Look for rare variants with VarScan

### Running VarScan

Time:  
`Sun Nov 24 17:52:13 MSK 2019`

Command:  
`samtools mpileup -d 45000 -f Influenza_A_virus_A_USA_RVD1_H3_H3N2.fasta SRR1705851_alignment_sorted.bam | java -jar VarScan.v2.4.0.jar mpileup2snp --min-var-freq 0.001 --variants --output-vcf 1 > VarScan_results_0_001.vcf`

Output:
```
[mpileup] 1 samples in 1 input files
Only SNPs will be reported
Warning: No p-value threshold provided, so p-values will not be calculated
Min coverage:	8
Min reads2:	2
Min var freq:	0.001
Min avg qual:	15
P-value thresh:	0.01
Input stream not ready, waiting for 5 seconds...
Reading input from STDIN
1665 bases in pileup file
23 variant positions (21 SNP, 2 indel)
0 were failed by the strand-filter
21 variant positions reported (21 SNP, 0 indel)
```

### Pull out the variants

Time:  
`Sun Nov 24 17:53:57 MSK 2019`

Command:  
`cat VarScan_results_0_001.vcf | awk 'NR>24 {split($10,a,":"); print $1, $2, $4, $5, a[7]}'`

Output:
```
KF848938.1 72 A G 99.96%
KF848938.1 117 C T 99.82%
KF848938.1 254 A G 0.17%
KF848938.1 276 A G 0.17%
KF848938.1 307 C T 0.94%
KF848938.1 340 T C 0.17%
KF848938.1 389 T C 0.22%
KF848938.1 691 A G 0.17%
KF848938.1 722 A G 0.2%
KF848938.1 744 A G 0.17%
KF848938.1 774 T C 99.96%
KF848938.1 802 A G 0.23%
KF848938.1 859 A G 0.18%
KF848938.1 915 T C 0.19%
KF848938.1 999 C T 99.86%
KF848938.1 1043 A G 0.18%
KF848938.1 1086 A G 0.21%
KF848938.1 1213 A G 0.22%
KF848938.1 1260 A C 99.94%
KF848938.1 1280 T C 0.18%
KF848938.1 1458 T C 0.84%
```

## 5. Inspect and align the control sample sequencing data


## Inspect raw sequencing data with fastqc



Time:  
`Mon Nov 25 12:49:17 MSK 2019`

Command:  
`fastqc -o . control_1.fastq.gz control_2.fastq.gz control_3.fastq.gz`

Output:  
3x of
```
Started analysis of control_i.fastq.gz
Approx 5% complete for control_i.fastq.gz
Approx 10% complete for control_i.fastq.gz
Approx 15% complete for control_i.fastq.gz
Approx 20% complete for control_i.fastq.gz
Approx 25% complete for control_i.fastq.gz
Approx 30% complete for control_i.fastq.gz
Approx 35% complete for control_i.fastq.gz
Approx 40% complete for control_i.fastq.gz
Approx 45% complete for control_i.fastq.gz
Approx 50% complete for control_i.fastq.gz
Approx 55% complete for control_i.fastq.gz
Approx 60% complete for control_i.fastq.gz
Approx 65% complete for control_i.fastq.gz
Approx 70% complete for control_i.fastq.gz
Approx 75% complete for control_i.fastq.gz
Approx 80% complete for control_i.fastq.gz
Approx 85% complete for control_i.fastq.gz
Approx 90% complete for control_i.fastq.gz
Approx 95% complete for control_i.fastq.gz
Analysis complete for control_i.fastq.gz
```

### Running alignment with mpileup

Time:  
`Mon Nov 25 12:54:16 MSK 2019`

Command:  
`bwa mem Influenza_A_virus_A_USA_RVD1_H3_H3N2.fasta control_1.fastq.gz | samtools view -S -b - | samtools sort - -o control_1_alignment_sorted.bam`

Output:
```
[M::bwa_idx_load_from_disk] read 0 ALT contigs
[M::process] read 67448 sequences (10000210 bp)...
[M::process] read 67230 sequences (10000094 bp)...
[M::mem_process_seqs] Processed 67448 reads in 1.651 CPU sec, 1.536 real sec
[M::process] read 67100 sequences (10000113 bp)...
[M::mem_process_seqs] Processed 67230 reads in 1.883 CPU sec, 1.674 real sec
[M::process] read 54808 sequences (8118313 bp)...
[M::mem_process_seqs] Processed 67100 reads in 1.863 CPU sec, 1.674 real sec
[M::mem_process_seqs] Processed 54808 reads in 1.547 CPU sec, 1.446 real sec
[main] Version: 0.7.17-r1188
[main] CMD: bwa mem Influenza_A_virus_A_USA_RVD1_H3_H3N2.fasta control_1.fastq.gz
[main] Real time: 7.270 sec; CPU: 7.160 sec
```

Time:  
`Mon Nov 25 12:55:16 MSK 2019`

Command:  
`bwa mem Influenza_A_virus_A_USA_RVD1_H3_H3N2.fasta control_2.fastq.gz | samtools view -S -b - | samtools sort - -o control_2_alignment_sorted.bam`

Output:
```
[M::bwa_idx_load_from_disk] read 0 ALT contigs
[M::process] read 67476 sequences (10000274 bp)...
[M::process] read 67236 sequences (10000039 bp)...
[M::mem_process_seqs] Processed 67476 reads in 1.688 CPU sec, 1.586 real sec
[M::process] read 67216 sequences (10000283 bp)...
[M::mem_process_seqs] Processed 67236 reads in 2.223 CPU sec, 2.576 real sec
[M::process] read 31399 sequences (4635971 bp)...
[M::mem_process_seqs] Processed 67216 reads in 2.059 CPU sec, 2.311 real sec
[M::mem_process_seqs] Processed 31399 reads in 1.165 CPU sec, 1.201 real sec
[main] Version: 0.7.17-r1188
[main] CMD: bwa mem Influenza_A_virus_A_USA_RVD1_H3_H3N2.fasta control_2.fastq.gz
[main] Real time: 8.371 sec; CPU: 7.323 sec
```


Time:  
`Mon Nov 25 12:56:16 MSK 2019`

Command:  
`bwa mem Influenza_A_virus_A_USA_RVD1_H3_H3N2.fasta control_3.fastq.gz | samtools view -S -b - | samtools sort - -o control_3_alignment_sorted.bam`

Output:
```
[M::bwa_idx_load_from_disk] read 0 ALT contigs
[M::process] read 67356 sequences (10000126 bp)...
[M::process] read 67208 sequences (10000122 bp)...
[M::mem_process_seqs] Processed 67356 reads in 1.704 CPU sec, 1.603 real sec
[M::process] read 67010 sequences (10000072 bp)...
[M::mem_process_seqs] Processed 67208 reads in 1.890 CPU sec, 1.676 real sec
[M::process] read 48390 sequences (7170166 bp)...
[M::mem_process_seqs] Processed 67010 reads in 1.831 CPU sec, 1.658 real sec
[M::mem_process_seqs] Processed 48390 reads in 1.415 CPU sec, 1.313 real sec
[main] Version: 0.7.17-r1188
[main] CMD: bwa mem Influenza_A_virus_A_USA_RVD1_H3_H3N2.fasta control_3.fastq.gz
[main] Real time: 7.100 sec; CPU: 7.035 sec
```

### Indexing the bam files

Time:  
`Mon Nov 25 13:01:03 MSK 2019`

Command:  
`ls control*.bam | xargs -n1 -P5 samtools index`

Output:
```
```

### Counting maximum coverage 

> (What is the desired value of d if we want to keep all possible variants, given the length of the reference sequence, the number of reads, and the average read length?)

Average coverage can be calculated as:  
average_contig_len * number_of_contigs / reference_len = 149 * 360000 / 1665 ~ 32000

But we can find **actual maximum** coverage with *samtools depth* and *awk*:


Time:  
`Sun Nov 24 17:33:56 MSK 2019`

Command:  
```samtools depth -d 1000000 control_1_alignment_sorted.bam | awk 'BEGIN{a=   0}{if ($3>0+a) a=$3} END{print a}'
samtools depth -d 1000000 control_2_alignment_sorted.bam | awk 'BEGIN{a=   0}{if ($3>0+a) a=$3} END{print a}'
samtools depth -d 1000000 control_3_alignment_sorted.bam | awk 'BEGIN{a=   0}{if ($3>0+a) a=$3} END{print a}'
```

Output:
```
35782
32837
36262
```

## 6. Use VarScan to look for rare variants in the reference files.

### Running VarScan

Time:  
`Mon Nov 25 13:09:04 MSK 2019`

Command:  
`samtools mpileup -d 36000 -f Influenza_A_virus_A_USA_RVD1_H3_H3N2.fasta control_1_alignment_sorted.bam | java -jar VarScan.v2.4.0.jar mpileup2snp --min-var-freq 0.001 --variants --output-vcf 1 > control_1_variants_0_001.vcf`

Output:
```
[mpileup] 1 samples in 1 input files
Only SNPs will be reported
Warning: No p-value threshold provided, so p-values will not be calculated
Min coverage:	8
Min reads2:	2
Min var freq:	0.001
Min avg qual:	15
P-value thresh:	0.01
Input stream not ready, waiting for 5 seconds...
Reading input from STDIN
1665 bases in pileup file
58 variant positions (58 SNP, 0 indel)
1 were failed by the strand-filter
57 variant positions reported (57 SNP, 0 indel)
```

Time:  
`Mon Nov 25 13:10:16 MSK 2019`

Command:  
`samtools mpileup -d 33000 -f Influenza_A_virus_A_USA_RVD1_H3_H3N2.fasta control_2_alignment_sorted.bam | java -jar VarScan.v2.4.0.jar mpileup2snp --min-var-freq 0.001 --variants --output-vcf 1 > control_2_variants_0_001.vcf`

Output:
```
Only SNPs will be reported
Warning: No p-value threshold provided, so p-values will not be calculated
Min coverage:	8
Min reads2:	2
Min var freq:	0.001
Min avg qual:	15
P-value thresh:	0.01
Reading input from STDIN
1665 bases in pileup file
54 variant positions (54 SNP, 0 indel)
2 were failed by the strand-filter
52 variant positions reported (52 SNP, 0 indel)
```

Time:  
`Mon Nov 25 13:11:27 MSK 2019`

Command:  
`samtools mpileup -d 37000 -f Influenza_A_virus_A_USA_RVD1_H3_H3N2.fasta control_3_alignment_sorted.bam | java -jar VarScan.v2.4.0.jar mpileup2snp --min-var-freq 0.001 --variants --output-vcf 1 > control_3_variants_0_001.vcf`

Output:
```
[mpileup] 1 samples in 1 input files
Only SNPs will be reported
Warning: No p-value threshold provided, so p-values will not be calculated
Min coverage:	8
Min reads2:	2
Min var freq:	0.001
Min avg qual:	15
P-value thresh:	0.01
Input stream not ready, waiting for 5 seconds...
Reading input from STDIN
1665 bases in pileup file
61 variant positions (61 SNP, 0 indel)
0 were failed by the strand-filter
61 variant positions reported (61 SNP, 0 indel)
```

### Parsing vcf to csv

Time:  
`Mon Nov 25 13:25:16 MSK 2019`

Command:  
```
cat control_1_variants_0_001.vcf | awk 'FNR==1{print "position,base,alt_base,frequency";next} NR>24 {split($10,a,":"); print $2, $4, $5, a[7]}' OFS=, > control_1_variants_0_001.csv

cat control_2_variants_0_001.vcf | awk 'FNR==1{print "position,base,alt_base,frequency";next} NR>24 {split($10,a,":"); print $2, $4, $5, a[7]}' OFS=, > control_2_variants_0_001.csv

cat control_3_variants_0_001.vcf | awk 'FNR==1{print "position,base,alt_base,frequency";next} NR>24 {split($10,a,":"); print $2, $4, $5, a[7]}' OFS=, > control_3_variants_0_001.csv

cat VarScan_results_0_001.vcf | awk 'FNR==1{print "position,base,alt_base,frequency";next} NR>24 {split($10,a,":"); print $2, $4, $5, a[7]}' OFS=, > VarScan_results_0_001.csv
```

Output:
```
```

## 7. Compare the control results to your roommate’s results
## 8. Epitope mapping

All work done in file `compare_results.ipynb` with python.
**Results** are in file `VarScan_results_0_001_with_significance.csv`.



Time:  
``

Command:  
``

Output:
```
```