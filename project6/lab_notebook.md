### Cnverting to .vcf file


Time:  
`Mon Mar 30 19:52:32 MSK 2020`

Command:  
`plink --23file SNP_raw_v4_Full_20170514175358.txt --recode vcf --out SNP`

Output:
```
PLINK v1.90b6.16 64-bit (19 Feb 2020)          www.cog-genomics.org/plink/1.9/
(C) 2005-2020 Shaun Purcell, Christopher Chang   GNU General Public License v3
Logging to SNP.log.
Options in effect:
  --23file SNP_raw_v4_Full_20170514175358.txt
  --out SNP
  --recode vcf

8192 MB RAM detected; reserving 4096 MB for main workspace.
--23file: SNP-temporary.bed + SNP-temporary.bim + SNP-temporary.fam written.
15125 variants with indel calls present.  '--snps-only no-DI' or
--list-23-indels may be useful here.
Inferred sex: male.
610526 variants loaded from .bim file.
1 person (1 male, 0 females) loaded from .fam.
Using 1 thread (no multithreaded calculations invoked).
Before main variant filters, 1 founder and 0 nonfounders present.
Calculating allele frequencies... done.
Warning: 103 het. haploid genotypes present (see SNP.hh ); many commands treat
these as missing.
Total genotyping rate is 0.989512.
610526 variants and 1 person pass filters and QC.
Note: No phenotypes present.
--recode vcf to SNP.vcf ... done.
Warning: At least one VCF allele code violates the official specification;
other tools may not accept the file.  (Valid codes must either start with a
'<', only contain characters in {A,C,G,T,N,a,c,g,t,n}, be an isolated '*', or
represent a breakend.)
```

### Insersection with clinvar database

Time:  
`Mon Mar 30 20:04:20 MSK 2020`

Command:  
`bedtools intersect -a SNP.vcf -b clinvar.vcf  > intersected.vcf`

Output:
```
```

### ANNOVAR

Web-version of ANNOVAR was used. Results are in folder `wANNOVAR_results`.
Also available by [link](http://wannovar.wglab.org/done/252690/zeIQfWu8kvn07CVF/index.html).


Time:  
``

Command:  
``

Output:
```
```