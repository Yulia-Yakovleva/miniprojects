## 1. (Optional, 1 point) Repeat masking


Time:  
`Tue Feb 25 14:10:41 MSK 2020`

Command:  
`RepeatMasker -pa 32 -species tardigrades GCA_001949185.1_Rvar_4.0_genomic.fna`

Output:
```
RepeatMasker version open-4.0.7
Search Engine: NCBI/RMBLAST [ 2.6.0+ ]
Warning...unknown stuff <
>
Master RepeatMasker Database: /nfs/home/azabelkin/.conda/envs/cooler/share/RepeatMasker/Libraries/RepeatMaskerLib.embl ( Complete Database: dc20170127 )


Building species libraries in: /nfs/home/azabelkin/.conda/envs/cooler/share/RepeatMasker/Libraries/dc20170127/tardigrada
   - 174 ancestral and ubiquitous sequence(s) for tardigrada
   - 0 lineage specific sequence(s) for tardigrada

analyzing file GCA_001949185.1_Rvar_4.0_genomic.fna

Checking for E. coli insertion elements

... 
e.t.c.
...
```

## 4. Intro -  Functional annotation.

### Extracting protein sequences

Time:  
`Tue Feb 25 14:16:55 MSK 2020`

Command:  
`./getAnnoFasta.pl data/augustus.whole.gff`

Output:
```
```

### Counting the number of obtained protein

Time:  
`Tue Feb 25 14:19:46 MSK 2020`

Command:  
`grep -c "^>" augustus.whole.aa`

Output:
```
16435
```

## 5. Physical localization 

### Creating local database from the protein fasta file

Time:  
`Tue Feb 25 15:29:06 MSK 2020`

Command:  
`makeblastdb -in augustus.whole.aa -dbtype prot`

Output:
```
Building a new DB, current time: 02/25/2020 15:51:42
New DB name:   /Users/alexey/PycharmProjects/miniprojects/project4/data/augustus.whole.aa
New DB title:  augustus.whole.aa
Sequence type: Protein
Keep MBits: T
Maximum file size: 1000000000B
Adding sequences from FASTA; added 16435 sequences in 0.529705 seconds.
```

### Looking with blastp using your peptide sequence file as a query

Time:  
`Tue Feb 25 15:49:54 MSK 2020`

Command:  
`blastp -query peptides.fa -db augustus.whole.aa -out blastp.out`

Output:
```
```


### Create an index file for ausustus proteins

Time:  
`Tue Feb 25 15:50:23 MSK 2020`

Command:  
`samtools faidx augustus.whole.aa`

Output:
```
```

### Picking up proteins by blastp results

Time:  
`Tue Feb 25 16:06:03 MSK 2020`

Command:  
`awk -F "\t" '{print $2}' blastp.out | sort -u | xargs samtools faidx augustus.whole.aa > peptides_augustus.aa`

Output:
```
```


### Counting the number of obtained protein

Time:  
`Tue Feb 25 16:06:42 MSK 2020`

Command:  
`grep -c "^>" peptides_augustus.aa`

Output:
```
34
```


## 6. Localization prediction, TargetP 1.1 Server

Web version was used:

> Summary of 34 predicted sequences from Non-Plant

Results are available in `targetp_results` folder.


## 7. BLAST search

Performed with `run_blast.py` python script. Results are available in `blast_result.csv` file.

## 8. Pfam prediction



### Trying to useweb-version:
> Your job is queued behind 27845 other searches. (approximate wait time: 15 hours and 28 minutes)

Oops, look's like we need to use local hmmsearch.

Time:  
`Wed Feb 26 13:46:17 MSK 2020`

Command:  
`hmmscan -o peptides_augustus_hmm.out --tblout peptides_augustus_hmm_tblout.csv --domtblout peptides_augustus_hmm_domtblout.csv --pfamtblout peptides_augustus_hmm_pfamtblout.csv  db/pfam/Pfam-A.hmm peptides_augustus.aa`

Output:
```
```

## 9. Integrate your various pieces of evidence

Since every protein contains multiple found domains and blast's hits, it's not properly to merge it to one table with a single row for every protein.

Result of BLAST are available in `blast_result.csv` file. Results of TargetP are available in `targetp_results` folder. And results of hmmsearch are available in `hmm_results` folder.