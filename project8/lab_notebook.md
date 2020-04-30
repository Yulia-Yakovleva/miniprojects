# Part 1. Amplicon sequencing.

### 1. QIIME2 installation

easy breezy

### 2. Importing data.


#### Importing

Time:  
`Tue Apr 28 14:42:00 MSK 2020`

Command:  
`qiime tools import   --type 'SampleData[SequencesWithQuality]'   --input-path manifest.tsv   --output-path sequences.qza   --input-format SingleEndFastqManifestPhred33V2`

Output:
`Imported manifest.tsv as SingleEndFastqManifestPhred33V2 to sequences.qza`


#### Validation

Time:  
`Tue Apr 28 14:42:56 MSK 2020`

Command:  
`qiime tools validate sequences.qza`

Output:
`Result sequences.qza appears to be valid at level=max.`

### 3. Demultiplexing and QC

Reads are already demultiplexed. Let's get a summary of the distribution of sequence qualities.

Time:  
`Tue Apr 28 14:44:31 MSK 2020`

Command:  
`qiime demux summarize   --i-data sequences.qza   --o-visualization sequences.qzv`

Output:
`Saved Visualization to: sequences.qzv`

This `.gzv` file can be visualized at [https://view.qiime2.org/](https://view.qiime2.org/).


### 4. Feature table construction (and more QC)

#### Trimming

Based on Interactive Quality Plot tab in the sequences.qzv we will choose `n = 166` as total length of the good quality sequence after the trimming.
Also we will set `m = 10 + 22 = 32` as a total length of the artificial sequences (barcode + primer).

Time:  
`Tue Apr 28 14:51:43 MSK 2020`

Command:  
`qiime dada2 denoise-single   --i-demultiplexed-seqs sequences.qza   --p-trim-left 32 --p-trunc-len 166 --o-representative-sequences rep-seqs.qza --o-table table.qza --o-denoising-stats stats.qza`

Output:
```
Saved FeatureTable[Frequency] to: table.qza
Saved FeatureData[Sequence] to: rep-seqs.qza
Saved SampleData[DADA2Stats] to: stats.qza
```

#### Check how many reads are passed the filter and were clustered

Time:  
`Tue Apr 28 15:13:15 MSK 2020`

Command:  
`qiime metadata tabulate   --m-input-file stats.qza   --o-visualization stats.qzva`

Output:
`Saved Visualization to: stats.qzv`

As we can see 96.18 % of bone dataset and 96.4 % of calculus dataset reads passed the feliter.


### 5. FeatureTable and FeatureData summaries

#### Create visual summaries of the data - how many sequences are associated with each sample and with each feature, etc

Time:  
`Tue Apr 28 15:36:06 MSK 2020`

Command:  
`qiime feature-table summarize   --i-table table.qza   --o-visualization table.qzv   --m-sample-metadata-file sample-metadata.tsv`

Output:
`Saved Visualization to: table.qzv`


#### Map feature IDs to sequences, to use these representative sequences in other applications

Time:  
`Tue Apr 28 15:37:24 MSK 2020`

Command:  
`qiime feature-table tabulate-seqs  --i-data rep-seqs.qza   --o-visualization rep-seqs.qzv`

Output:
`Saved Visualization to: rep-seqs.qzv`

### 6. Taxonomic analysis

Time:  
`Tue Apr 28 15:37:24 MSK 2020`

Command:  
`qiime feature-classifier classify-sklearn   --i-classifier gg-13-8-99-nb-classifier.qza   --i-reads rep-seqs.qza   --o-classification taxonomy.qza`

Output:
`Saved FeatureData[Taxonomy] to: taxonomy.qza`


#### Visualising

Time:  
`Tue Apr 28 15:49:29 MSK 2020`

Command:  
`qiime metadata tabulate --m-input-file taxonomy.qza --o-visualization taxonomy.qzv`

Output:
`Saved Visualization to: taxonomy.qzv`

#### Generating interactive bar plots for the taxonomic composition

Time:  
`Tue Apr 28 15:51:07 MSK 2020`

Command:  
```qiime taxa barplot \
  --i-table table.qza \
  --i-taxonomy taxonomy.qza \
  --m-metadata-file sample-metadata.tsv \
  --o-visualization taxa-bar-plots.qzv
  ```

Output:
`Saved Visualization to: taxa-bar-plots.qzv`



# Part 2


### 1. Shotgun sequence data profiling

Time:  
`Tue Apr 28 19:12:48 MSK 2020`

Command:  
`metaphlan2.py G12_assembly.fna.gz --input_type fasta --nproc 4 > G12_output.txt`

Output:
```
Help message for read_fastx.py
```

### 2. Comparison with samples from HMP

Time:  
`Tue Apr 28 19:16:13 MSK 2020`

Command:  
```
$ for f in *.fasta
> do
> metaphlan2.py $f --input_type fasta --nproc 4 > ${f%.fasta}_profile.txt
> done
```

Output:
```
Warning! Biom python library not detected!
 Exporting to biom format will not work!
Help message for read_fastx.py
Warning! Biom python library not detected!
 Exporting to biom format will not work!
Help message for read_fastx.py
Warning! Biom python library not detected!
 Exporting to biom format will not work!
Help message for read_fastx.py
Warning! Biom python library not detected!
 Exporting to biom format will not work!
Help message for read_fastx.py
Warning! Biom python library not detected!
 Exporting to biom format will not work!
Help message for read_fastx.py
```


### 3. Visualization of the metaphlan results with a heat map

#### Merging the metaphlan profile files into a single abundance table

Time:  
`Tue Apr 28 22:22:07 MSK 2020`

Command:  
`merge_metaphlan_tables.py G12_output.txt SRS014459-Stool_profile.txt SRS014464-Anterior_nares_profile.txt SRS014470-Tongue_dorsum_profile.txt SRS014472-Buccal_mucosa_profile.txt SRS014494-Posterior_fornix_profile.txt > merged.txt`

Output:
```
```


#### Making a heat map

Time:  
`Tue Apr 28 22:34:14 MSK 2020`

Command:  
`metaphlan_hclust_heatmap.py --in merged.txt --out heat_map.pdf -s log --top 50`

Output:
```
```

### 4. Comparison with ancient Tannerella forsythia genome

#### Align contigs on the reference of T. forsythia


Time:  
`Tue Apr 28 23:01:57 MSK 2020`

Command:  
`bwa index GCA_000238215.1_ASM23821v1_genomic.fna.gz`

Output:
```
[bwa_index] Pack FASTA... 0.06 sec
[bwa_index] Construct BWT for the packed sequence...
[bwa_index] 1.33 seconds elapse.
[bwa_index] Update BWT... 0.03 sec
[bwa_index] Pack forward-only FASTA... 0.04 sec
[bwa_index] Construct SA from BWT and Occ... 0.53 sec
[main] Version: 0.7.17-r1188
[main] CMD: bwa index GCA_000238215.1_ASM23821v1_genomic.fna.gz
[main] Real time: 2.135 sec; CPU: 1.985 sec
```

Time:  
`Tue Apr 28 23:02:13 MSK 2020`

Command:  
`bwa mem GCA_000238215.1_ASM23821v1_genomic.fna.gz G12_assembly.fna.gz > G12_alignment.sam`

Output:
```
[M::bwa_idx_load_from_disk] read 0 ALT contigs
[M::process] read 33142 sequences (10000684 bp)...
[M::process] read 34258 sequences (10000241 bp)...
[M::mem_process_seqs] Processed 33142 reads in 6.437 CPU sec, 7.275 real sec
[M::process] read 35404 sequences (10000120 bp)...
[M::mem_process_seqs] Processed 34258 reads in 6.035 CPU sec, 6.019 real sec
[M::process] read 36534 sequences (10000152 bp)...
[M::mem_process_seqs] Processed 35404 reads in 5.981 CPU sec, 5.975 real sec
[M::process] read 38278 sequences (10001697 bp)...
[M::mem_process_seqs] Processed 36534 reads in 5.933 CPU sec, 5.903 real sec
[M::process] read 38866 sequences (10000030 bp)...
[M::mem_process_seqs] Processed 38278 reads in 6.338 CPU sec, 6.376 real sec
[M::process] read 40534 sequences (10000318 bp)...
[M::mem_process_seqs] Processed 38866 reads in 7.062 CPU sec, 8.316 real sec
[M::process] read 42182 sequences (10000459 bp)...
[M::mem_process_seqs] Processed 40534 reads in 6.408 CPU sec, 6.535 real sec
[M::process] read 43782 sequences (10000165 bp)...
[M::mem_process_seqs] Processed 42182 reads in 6.198 CPU sec, 6.287 real sec
[M::process] read 45484 sequences (10000333 bp)...
[M::mem_process_seqs] Processed 43782 reads in 6.580 CPU sec, 6.957 real sec
[M::process] read 47172 sequences (10000275 bp)...
[M::mem_process_seqs] Processed 45484 reads in 6.529 CPU sec, 6.747 real sec
[M::process] read 49554 sequences (10000202 bp)...
[M::mem_process_seqs] Processed 47172 reads in 5.979 CPU sec, 6.000 real sec
[M::process] read 51030 sequences (10000167 bp)...
[M::mem_process_seqs] Processed 49554 reads in 6.207 CPU sec, 6.235 real sec
[M::process] read 53878 sequences (10000268 bp)...
[M::mem_process_seqs] Processed 51030 reads in 6.294 CPU sec, 6.368 real sec
[M::process] read 56196 sequences (10000036 bp)...
[M::mem_process_seqs] Processed 53878 reads in 5.925 CPU sec, 5.968 real sec
[M::process] read 59072 sequences (10000141 bp)...
[M::mem_process_seqs] Processed 56196 reads in 5.957 CPU sec, 5.958 real sec
[M::process] read 60188 sequences (10000115 bp)...
[M::mem_process_seqs] Processed 59072 reads in 6.343 CPU sec, 6.657 real sec
[M::process] read 66608 sequences (10000039 bp)...
[M::mem_process_seqs] Processed 60188 reads in 5.819 CPU sec, 5.765 real sec
[M::process] read 73439 sequences (9958998 bp)...
[M::mem_process_seqs] Processed 66608 reads in 5.724 CPU sec, 5.668 real sec
[M::mem_process_seqs] Processed 73439 reads in 5.577 CPU sec, 5.584 real sec
[main] Version: 0.7.17-r1188
[main] CMD: bwa mem GCA_000238215.1_ASM23821v1_genomic.fna.gz G12_assembly.fna.gz
[main] Real time: 120.848 sec; CPU: 117.509 sec
```

#### Calling regions obtained during the strain evolution

Time:
`Tue Apr 28 23:10:22 MSK 2020`

Command:  
`bedtools bamtobed -i G12_alignment.sam > G12_alignment.bed`

Output:
```
```

Time:
`Tue Apr 28 23:16:20 MSK 2020`

Command:  
`bedtools intersect -a GCA_000238215.1_ASM23821v1_genomic.gff.gz -b G12_alignment.bed -v > obtained.bed`

Output:
```
```