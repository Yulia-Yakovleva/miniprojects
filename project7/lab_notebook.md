### a). Aligning with HISAT2

#### Build genome index

Time:  
`Mon Apr 13 18:49:07 MSK 2020`

Command:  
`hisat2-build GCF_000146045.2_R64_genomic.fna GCF_000146045.2_R64_genomic.fna.index`

Tail of output:
```
Headers:
    len: 12157105
    gbwtLen: 12157106
    nodes: 12157106
    sz: 3039277
    gbwtSz: 3039277
    lineRate: 6
    offRate: 4
    offMask: 0xfffffff0
    ftabChars: 10
    eftabLen: 0
    eftabSz: 0
    ftabLen: 1048577
    ftabSz: 4194308
    offsLen: 759820
    offsSz: 3039280
    lineSz: 64
    sideSz: 64
    sideGbwtSz: 48
    sideGbwtLen: 192
    numSides: 63319
    numLines: 63319
    gbwtTotLen: 4052416
    gbwtTotSz: 4052416
    reverse: 0
    linearFM: Yes
Total time for call to driver() for forward index: 00:00:19
```


#### Run hisat2 in single-end mode

Time:  
`Mon Apr 13 19:23:12 MSK 2020`

Command:  
`hisat2 -p 4 -x GCF_000146045.2_R64_genomic.fna.index -U SRR941816.fastq.gz | samtools sort > fermentation_0_replicate_1.bam`

Output:
```
9043877 reads; of these:
  9043877 (100.00%) were unpaired; of these:
    520137 (5.75%) aligned 0 times
    7929703 (87.68%) aligned exactly 1 time
    594037 (6.57%) aligned >1 times
94.25% overall alignment rate
[bam_sort_core] merging from 2 files and 1 in-memory blocks...
```

Time:  
`Mon Apr 13 19:24:16 MSK 2020`

Command:  
`hisat2 -p 4 -x GCF_000146045.2_R64_genomic.fna.index -U SRR941817.fastq.gz | samtools sort > fermentation_0_replicate_2.bam`

Output:
```
9929568 reads; of these:
  9929568 (100.00%) were unpaired; of these:
    511726 (5.15%) aligned 0 times
    8644591 (87.06%) aligned exactly 1 time
    773251 (7.79%) aligned >1 times
94.85% overall alignment rate
[bam_sort_core] merging from 2 files and 1 in-memory blocks...
```


Time:  
`Mon Apr 13 19:25:24 MSK 2020`

Command:  
`hisat2 -p 4 -x GCF_000146045.2_R64_genomic.fna.index -U SRR941818.fastq.gz | samtools sort > fermentation_30_replicate_1.bam`

Output:
```
1721675 reads; of these:
  1721675 (100.00%) were unpaired; of these:
    66368 (3.85%) aligned 0 times
    1507910 (87.58%) aligned exactly 1 time
    147397 (8.56%) aligned >1 times
96.15% overall alignment rate
```

Time:  
`Mon Apr 13 19:27:05 MSK 2020`

Command:  
`hisat2 -p 4 -x GCF_000146045.2_R64_genomic.fna.index -U SRR941819.fastq.gz | samtools sort > fermentation_30_replicate_2.bam`

Output:
```
6172452 reads; of these:
  6172452 (100.00%) were unpaired; of these:
    234529 (3.80%) aligned 0 times
    5367723 (86.96%) aligned exactly 1 time
    570200 (9.24%) aligned >1 times
96.20% overall alignment rate
[bam_sort_core] merging from 1 files and 1 in-memory blocks...
```

### b) Quantifying with featureCounts

#### Convert from GFF to GTF

Time:  
`Mon Apr 13 20:03:36 MSK 2020`

Command:  
`gffread GCF_000146045.2_R64_genomic.gff -T -o GCF_000146045.2_R64_genomic.gtf`

Output:
```
```

#### Run the feature counts program

Time:  
`Mon Apr 13 20:18:16 MSK 2020`

Command:  
`featureCounts -a GCF_000146045.2_R64_genomic.gtf -o feature_counts fermentation_0_replicate_1.bam fermentation_0_replicate_2.bam fermentation_30_replicate_1.bam fermentation_30_replicate_2.bam`

Output:
```
        ==========     _____ _    _ ____  _____  ______          _____
        =====         / ____| |  | |  _ \|  __ \|  ____|   /\   |  __ \
          =====      | (___ | |  | | |_) | |__) | |__     /  \  | |  | |
            ====      \___ \| |  | |  _ <|  _  /|  __|   / /\ \ | |  | |
              ====    ____) | |__| | |_) | | \ \| |____ / ____ \| |__| |
        ==========   |_____/ \____/|____/|_|  \_\______/_/    \_\_____/
	  v2.0.0

//========================== featureCounts setting ===========================\\
||                                                                            ||
||             Input files : 4 BAM files                                      ||
||                           o fermentation_0_replicate_1.bam                 ||
||                           o fermentation_0_replicate_2.bam                 ||
||                           o fermentation_30_replicate_1.bam                ||
||                           o fermentation_30_replicate_2.bam                ||
||                                                                            ||
||             Output file : feature_counts                                   ||
||                 Summary : feature_counts.summary                           ||
||              Annotation : GCF_000146045.2_R64_genomic.gtf (GTF)            ||
||      Dir for temp files : ./                                               ||
||                                                                            ||
||                 Threads : 1                                                ||
||                   Level : meta-feature level                               ||
||              Paired-end : no                                               ||
||      Multimapping reads : not counted                                      ||
|| Multi-overlapping reads : not counted                                      ||
||   Min overlapping bases : 1                                                ||
||                                                                            ||
\\============================================================================//

//================================= Running ==================================\\
||                                                                            ||
|| Load annotation file GCF_000146045.2_R64_genomic.gtf ...                   ||
||    Features : 6760                                                         ||
||    Meta-features : 6420                                                    ||
||    Chromosomes/contigs : 17                                                ||
||                                                                            ||
|| Process BAM file fermentation_0_replicate_1.bam...                         ||
||    Single-end reads are included.                                          ||
||    Total alignments : 9749624                                              ||
||    Successfully assigned alignments : 7291724 (74.8%)                      ||
||    Running time : 0.17 minutes                                             ||
||                                                                            ||
|| Process BAM file fermentation_0_replicate_2.bam...                         ||
||    Single-end reads are included.                                          ||
||    Total alignments : 10810484                                             ||
||    Successfully assigned alignments : 7987002 (73.9%)                      ||
||    Running time : 0.18 minutes                                             ||
||                                                                            ||
|| Process BAM file fermentation_30_replicate_1.bam...                        ||
||    Single-end reads are included.                                          ||
||    Total alignments : 1880816                                              ||
||    Successfully assigned alignments : 1402168 (74.6%)                      ||
||    Running time : 0.03 minutes                                             ||
||                                                                            ||
|| Process BAM file fermentation_30_replicate_2.bam...                        ||
||    Single-end reads are included.                                          ||
||    Total alignments : 6782903                                              ||
||    Successfully assigned alignments : 4975467 (73.4%)                      ||
||    Running time : 0.12 minutes                                             ||
||                                                                            ||
||                                                                            ||
|| Summary of counting results can be found in file "feature_counts.summary"  ||
||                                                                            ||
\\============================================================================//
```


#### Simplify the counts

Time:  
`Mon Apr 13 20:22:15 MSK 2020`

Command:  
`cat feature_counts | cut -f 1,7-10 > simple_counts.txt`

Output:
```
```

### c) Find differentially expressed genes with Deseq2

#### Calculate metrics

Time:  
`Mon Apr 13 20:59:06 MSK 2020`

Command:  
`cat simple_counts.txt | R -f deseq2.r`

Output:
```
estimating size factors
estimating dispersions
gene-wise dispersion estimates
mean-dispersion relationship
final dispersion estimates
fitting model and testing
```

#### Draw heatmap


Time:  
`Mon Apr 13 21:01:20 MSK 2020`

Command:  
`cat norm-matrix-deseq2.txt | R -f draw-heatmap.r`

Output:
```
```

### d) Result Interpretation

#### Getting first 50 genes

Time:  
``

Command:  
`head -n 50 result.txt | cut -f 1 > genes.txt`

Output:
```
```

#### Using gene ontology terms to get a sense of what these genes are doing

Online version of GO was used, result are in `mapper_genes_4909_*` files.