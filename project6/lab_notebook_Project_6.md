```python
import pandas as pd
```


```python
# Calculate ancestry composition (admixture proportions)
! python admix/admix/admix.py -f SNP_raw_v4_Full_20170514175358.txt -v 23andme
```

    
    No model specified, all available models will be used.
    
    
    Admixture calculation models: K7b,K12b,globe13,globe10,world9,Eurasia7,Africa9,weac2,E11,K36,EUtest13,Jtest14,HarappaWorld,TurkicK11,KurdishK10,AncientNearEast13,K7AMI,K8AMI,MDLPK27,puntDNAL,K47,K7M1,K13M2,K14M1,K18M4,K25R1,MichalK25
    
    Calcuation is started...
    
    K7b
    South Asian: 2.26%
    West Asian: 25.59%
    Siberian: 2.02%
    African: 0.39%
    Southern: 21.04%
    Atlantic Baltic: 48.70%
    East Asian: 0.00%
    
    
    K12b
    Gedrosia: 8.30%
    Siberian: 1.62%
    Northwest African: 1.77%
    Southeast Asian: 0.00%
    Atlantic Med: 18.45%
    North European: 34.11%
    South Asian: 1.65%
    East African: 0.01%
    Southwest Asian: 8.14%
    East Asian: 0.00%
    Caucasus: 25.96%
    Sub Saharan: 0.00%
    
    
    globe13
    Siberian: 1.37%
    Amerindian: 0.28%
    West African: 0.00%
    Palaeo African: 0.26%
    Southwest Asian: 12.95%
    East Asian: 0.00%
    Mediterranean: 24.44%
    Australasian: 0.93%
    Artic: 0.57%
    West Asian: 20.17%
    North European: 37.56%
    South Asian: 1.45%
    East African: 0.03%
    
    
    globe10
    Ameriandian: 0.56%
    West Asian: 24.59%
    Australasian: 0.98%
    Palaeo African: 0.30%
    Neo African: 0.00%
    Siberian: 2.22%
    Southern: 18.16%
    East Asian: 0.00%
    Atlantic Baltic: 50.79%
    South Asian: 2.41%
    
    
    world9
    Amerindian: 0.00%
    East Asian: 0.14%
    African: 0.00%
    Atlantic Baltic: 51.64%
    Australasian: 0.01%
    Siberian: 0.01%
    Caucasus Gedrosia: 48.24%
    Southern: 0.01%
    South Asian: 0.00%
    
    
    Eurasia7
    Sub Saharan: 0.39%
    West Asian: 26.79%
    Atlantic Baltic: 49.98%
    East Asian: 0.00%
    Southern: 16.97%
    South Asian: 3.56%
    Siberian: 2.32%
    
    
    Africa9
    Europe: 61.75%
    Northwest Africa: 5.93%
    Southwest Asia: 29.71%
    East Africa: 0.00%
    South Africa: 0.00%
    Mbuti: 0.00%
    West Africa: 0.00%
    Biaka: 2.62%
    San: 0.00%
    
    
    weac2
    Palaeoafrican: 0.36%
    Atlantic Baltic: 54.83%
    Northeast Asian: 2.16%
    Near East: 34.08%
    Sub Saharan: 0.12%
    South Asian: 8.45%
    Southeast Asian: 0.00%
    
    
    E11
    African: 2.02%
    European: 68.54%
    India: 22.17%
    Malay: 0.30%
    South Chinese Dai: 0.00%
    Southwest Chinese Yi: 0.00%
    East Chinese: 0.00%
    Japanese: 0.00%
    North Chinese Oroqen: 1.04%
    Yakut: 1.35%
    American: 4.58%
    
    
    K36
    Amerindian: 0.00%
    Arabian: 2.71%
    Armenian: 2.12%
    Basque: 0.71%
    Central African: 0.00%
    Central Euro: 2.16%
    East African: 0.00%
    East Asian: 0.00%
    East Balkan: 6.25%
    East Central Asian: 0.00%
    East Central Euro: 14.57%
    East Med: 10.79%
    Eastern Euro: 11.42%
    Fennoscandian: 4.12%
    French: 1.89%
    Iberian: 1.93%
    Indo-Chinese: 0.00%
    Italian: 11.77%
    Malayan: 0.00%
    Near Eastern: 2.64%
    North African: 1.65%
    North Atlantic: 2.84%
    North Caucasian: 9.07%
    North Sea: 3.26%
    Northeast African: 0.00%
    Oceanian: 0.00%
    Omotic: 0.00%
    Pygmy: 0.00%
    Siberian: 0.00%
    South Asian: 0.00%
    South Central Asian: 5.66%
    South Chinese: 0.00%
    Volga-Ural: 0.00%
    West African: 0.00%
    West Caucasian: 2.65%
    West Med: 1.79%
    
    
    EUtest13
    South Baltic: 17.40%
    East Euro: 15.12%
    North-Central Euro: 11.15%
    Atlantic: 9.29%
    West Med: 7.69%
    East Med: 19.00%
    West Asian: 12.98%
    Middle Eastern: 4.94%
    South Asian: 2.21%
    East African: 0.00%
    East Asian: 0.00%
    Siberian: 0.02%
    West African: 0.21%
    
    
    Jtest14
    South Baltic: 17.34%
    East Euro: 14.44%
    North-Central Euro: 10.56%
    Atlantic: 7.95%
    West Med: 6.67%
    Ashkenazim: 8.92%
    East Med: 16.68%
    West Asian: 11.81%
    Middle Eastern: 3.30%
    South Asian: 2.10%
    East African: 0.00%
    East Asian: 0.00%
    Siberian: 0.08%
    West African: 0.14%
    
    
    HarappaWorld
    South-Indian: 0.70%
    Baloch: 12.22%
    Caucasian: 23.77%
    Northeast-Euro: 34.18%
    Southeast-Asian: 0.00%
    Siberian: 1.45%
    Northeast-Asian: 0.00%
    Papuan: 0.93%
    American: 0.05%
    Beringian: 0.00%
    Mediterranean: 17.88%
    Southwest-Asian: 8.44%
    San: 0.20%
    East-African: 0.00%
    Pygmy: 0.19%
    West-African: 0.00%
    
    
    TurkicK11
    Southeast European: 26.48%
    West Asian: 23.01%
    Southeast Asian: 0.06%
    Sub-Saharan African: 0.13%
    Northeast European: 33.15%
    Indian: 3.67%
    Northwest European: 10.52%
    Turkic: 1.89%
    Mongol: 0.01%
    Papuan: 0.71%
    Northeast Asian: 0.43%
    
    
    KurdishK10
    Kurdish: 18.37%
    Southeast-European: 17.90%
    Norhteast-European: 31.98%
    Indian: 3.05%
    East-Asian: 0.47%
    Northwest-European: 9.11%
    Siberian: 0.00%
    Sardinian: 10.49%
    Southwest-Asian: 8.62%
    Sub-Saharan: 0.00%
    
    
    AncientNearEast13
    Southeast Asian: 1.54%
    Anatolia Neolithic: 13.76%
    CHG-EEF: 35.10%
    Polar: 0.00%
    EHG: 14.11%
    Sub-Saharan: 0.00%
    Iran-Neolithic: 12.24%
    Karitiana: 0.60%
    Ancestral-Indian: 1.93%
    Natufian: 9.52%
    Siberian: 0.00%
    Papuan: 1.42%
    SHG-WHG: 9.77%
    
    
    K7AMI
    Sub-Saharan: 0.22%
    Oceanian: 1.55%
    Amerindian: 2.18%
    Euro Hunter-Gatherer: 45.99%
    Siberian: 1.57%
    Southeast Asian: 0.00%
    Near Eastern: 48.49%
    
    
    K8AMI
    Amerindian: 1.27%
    Siberian: 0.67%
    Euro Hunter-Gatherer: 39.07%
    Oceanian: 0.93%
    Sub-Saharan: 0.10%
    Southeast Asian: 0.00%
    Linearbandkeramik: 35.00%
    South-Central Asian: 22.96%
    
    
    MDLPK27
    Nilotic-Omotic: 0.14%
    Ancestral-South-Indian: 0.95%
    North-European-Baltic: 32.15%
    Uralic: 0.99%
    Australo-Melanesian: 1.82%
    East-Siberean: 0.56%
    Ancestral-Yayoi: 0.00%
    Caucasian-Near-Eastern: 22.42%
    Tibeto-Burman: 0.00%
    Austronesian: 0.04%
    Central-African-Pygmean: 0.53%
    Central-African-Hunter-Catherers: 0.00%
    Nilo-Sahrian: 0.00%
    North-African: 2.85%
    Gedrosia-Caucasian: 10.12%
    Cushitic: 0.98%
    Congo-Pygmean: 0.08%
    Bushmen: 0.00%
    South-Meso-Amerindian: 0.97%
    South-West-European: 11.78%
    North-Amerindian: 0.00%
    Arabic: 5.80%
    North-Circumpolar: 0.00%
    Kalash: 4.98%
    Papuan-Australian: 0.00%
    Baltic-Finnic: 2.82%
    Bantu: 0.00%
    
    
    puntDNAL
    EHG-Steppe: 25.73%
    Oceanian: 1.15%
    East Eurasian: 0.00%
    Iran Neolithic: 12.89%
    Siberian: 1.00%
    Sub-Saharan: 0.00%
    African HG: 0.00%
    South Eurasian: 1.05%
    Western HG: 16.46%
    Natufian HG: 8.54%
    Amerinidian: 0.82%
    Anatolian Neolithic: 32.35%
    
    
    K47
    Kushitic: 0.00%
    North-Iberian: 2.66%
    East-Iberian: 1.08%
    Tibeto-Burman: 0.00%
    North-African: 1.06%
    South-Caucasian: 5.48%
    North-Caucasian: 6.65%
    Paleo-Balkan: 5.90%
    Turkic-Altai: 0.00%
    Proto-Austronesian: 0.00%
    Nilotic: 0.00%
    East-Med: 7.98%
    Omotic: 0.21%
    Munda: 0.00%
    North-Amerind: 0.00%
    Arabic: 5.22%
    East-Euro: 24.79%
    Central-African: 0.00%
    Andean: 0.03%
    Indo-Chinese: 0.00%
    South-Indian: 0.02%
    NE-Asian: 0.00%
    Volgan: 2.21%
    Mongolian: 0.00%
    Siberian: 0.00%
    North-Sea-Germanic: 0.97%
    Celtic: 3.79%
    West-African: 0.00%
    West-Finnic: 2.75%
    Uralic: 0.00%
    Sahelian: 0.00%
    NW-Indian: 0.21%
    East-African: 0.00%
    East-Asian: 0.00%
    Amuro-Manchurian: 0.00%
    Scando-Germanic: 1.84%
    Iranian: 8.55%
    South-African: 0.00%
    Amazonian: 0.00%
    Baltic: 8.88%
    Malay: 0.00%
    Meso-Amerind: 0.00%
    South-Chinese: 0.00%
    Papuan: 0.27%
    West-Med: 3.84%
    Pamirian: 0.62%
    Central-Med: 5.00%
    
    
    K7M1
    North Euro: 25.84%
    Mediterranean: 39.41%
    Caspian Sea: 24.00%
    North Africa & Middle East: 10.75%
    Africa: 0.00%
    SE Asia: 0.00%
    NE Asia: 0.00%
    
    
    K13M2
    West Europe: 28.65%
    East Europe: 29.83%
    South Med: 9.75%
    Caucasus: 18.57%
    Arabia: 9.68%
    Siberia: 0.00%
    Central Asia: 2.08%
    India: 1.44%
    South East Asia: 0.00%
    West Africa: 0.00%
    East Africa: 0.00%
    Oceania: 0.00%
    East Asia: 0.00%
    
    
    K14M1
    NorthWest Euro: 5.53%
    NorthCentral Euro: 19.88%
    NorthEast Eruo: 17.23%
    SouthWest Euro: 5.47%
    SouthEast Euro: 12.48%
    Anatolia: 21.79%
    East Anatolia: 0.00%
    Caspian Sea: 1.94%
    Persic Gulf: 14.66%
    North Africa & Arabia: 1.02%
    Equatorial Africa: 0.00%
    South Himalayas: 0.00%
    SouthEast Asia: 0.00%
    NorthEast Asia: 0.00%
    
    
    K18M4
    Atlantic: 7.78%
    Central Euro: 4.88%
    North Euro: 0.00%
    West Med: 0.11%
    NW Black Sea: 10.03%
    East Med: 18.44%
    Steppe Russia: 37.13%
    East Caspian: 0.00%
    East Anatolia: 3.80%
    Persian Gulf: 15.70%
    North Russia: 0.00%
    North Africa & Near East: 2.14%
    Equatorial Africa: 0.00%
    Central Asia: 0.00%
    South Central Asia: 0.00%
    Bay of Bengal: 0.00%
    South China Sea: 0.00%
    East Asia: 0.00%
    
    
    K25R1
    Atlantic: 4.44%
    Scandinavia: 5.01%
    NW Europe: 3.60%
    South Alps: 2.35%
    West Med: 3.43%
    Baltic: 3.92%
    Russian Steppes: 35.43%
    North Black Sea: 0.00%
    South East Europe: 19.45%
    South Med: 3.96%
    East Caspian: 0.00%
    South Caspian: 9.02%
    Arabia: 6.89%
    South Caucasus: 0.57%
    North Anatolia: 1.92%
    Sahara: 0.00%
    Equatorial Africa: 0.00%
    East Africa: 0.00%
    Siberian: 0.00%
    East Asia: 0.00%
    South Asia: 0.00%
    SE Asia: 0.00%
    Central Asia: 0.00%
    Amerindian: 0.00%
    North Russian: 0.00%
    
    
    MichalK25
    Nasoic: 1.66%
    Uralic: 1.66%
    South Amerindian: 0.97%
    North Indian: 2.90%
    Central African: 0.01%
    Altaic: 0.01%
    Kamchatkan: 0.33%
    Mediterranean: 17.49%
    Eskimoic: 0.01%
    Siberian: 0.01%
    Caucasian: 15.95%
    Amazonian: 0.01%
    East Asian: 0.01%
    East African: 0.01%
    Druzian: 10.91%
    North Amerindian: 0.61%
    Arabic: 5.47%
    Berberic: 3.55%
    Papuan: 0.01%
    Northeast European: 33.21%
    Khomani San: 0.14%
    Taiwanese Aboriginal: 0.26%
    Kalash: 4.47%
    Northeast Asian: 0.34%
    West African: 0.01%
    
    



```python
dict = {'K7b':'Atlantic Baltic', 
        'K12b':'North European', 
        'globe13':'North European', 
        'globe10':'Atlantic Baltic',
        'world9':'Atlantic Baltic',
        'Eurasia7':'Atlantic Baltic',
        'Africa9':'Europe',
        'weac2':'Atlantic Baltic',
        'E11':'European',
        'K36':'East Central Euro',
        'EUtest13':'South Baltic',
        'Jtest14':'South Baltic',
        'HarappaWorld':'Northeast-Euro',
        'TurkicK11':'Southeast European',
        'KurdishK10':'Norhteast-European',
        'AncientNearEast13':'Anatolia Neolithic',
        'K7AMI':'Near Eastern',
        'K8AMI':'Euro Hunter-Gatherer',
        'MDLPK27':'North-European-Baltic',
        'puntDNAL':'Anatolian Neolithic',
        'K47':'East-Euro',
        'K7M1':'Mediterranean',
        'K13M2':'East Europe',
        'K14M1':'Anatolia',
        'K18M4':'Steppe Russia',
        'K25R1':'Russian Steppes',
        'MichalK25':'Northeast European',        
       }
print(pd.DataFrame(dict.items(), columns=['Model', 'Major Value']).to_latex(index=False))
```

    \begin{tabular}{ll}
    \toprule
                 Model &            Major Value \\
    \midrule
                   K7b &        Atlantic Baltic \\
                  K12b &         North European \\
               globe13 &         North European \\
               globe10 &        Atlantic Baltic \\
                world9 &        Atlantic Baltic \\
              Eurasia7 &        Atlantic Baltic \\
               Africa9 &                 Europe \\
                 weac2 &        Atlantic Baltic \\
                   E11 &               European \\
                   K36 &      East Central Euro \\
              EUtest13 &           South Baltic \\
               Jtest14 &           South Baltic \\
          HarappaWorld &         Northeast-Euro \\
             TurkicK11 &     Southeast European \\
            KurdishK10 &     Norhteast-European \\
     AncientNearEast13 &     Anatolia Neolithic \\
                 K7AMI &           Near Eastern \\
                 K8AMI &   Euro Hunter-Gatherer \\
               MDLPK27 &  North-European-Baltic \\
              puntDNAL &    Anatolian Neolithic \\
                   K47 &              East-Euro \\
                  K7M1 &          Mediterranean \\
                 K13M2 &            East Europe \\
                 K14M1 &               Anatolia \\
                 K18M4 &          Steppe Russia \\
                 K25R1 &        Russian Steppes \\
             MichalK25 &     Northeast European \\
    \bottomrule
    \end{tabular}
    



```python
# Our professor is Atlantic Baltic
```


```python
! grep 'MT' SNP_raw_v4_Full_20170514175358.txt > MT_SNPs.txt
! grep 'X' SNP_raw_v4_Full_20170514175358.txt > X_SNPs.txt
! grep 'Y' SNP_raw_v4_Full_20170514175358.txt > Y_SNPs.txt
! cat X_SNPs.txt MT_SNPs.txt > MT_X_SNPs.txt
! head *.txt
```

    ==> MT_SNPs.txt <==
    
    
    
    
    
    
    
    
    
    
    
    ==> MT_X_SNPs.txt <==
    
    
    
    
    
    
    
    
    
    
    
    ==> ManuSporny-genome.txt <==
    
    
    
    
    
    
    
    
    
    
    
    ==> SNP_raw_v4_Full_20170514175358.txt <==
    
    
    
    
    
    
    
    
    
    
    
    ==> X_SNPs.txt <==
    
    
    
    
    
    
    
    
    
    
    
    ==> Y_SNPs.txt <==
    
    
    
    
    
    
    
    
    
    



```python
! /home/yulia/src/plink_linux_x86_64_20200219/plink --23file SNP_raw_v4_Full_20170514175358.txt --recode vcf --out SNP
```

    PLINK v1.90b6.16 64-bit (19 Feb 2020)          www.cog-genomics.org/plink/1.9/
    (C) 2005-2020 Shaun Purcell, Christopher Chang   GNU General Public License v3
    Logging to SNP.log.
    Options in effect:
      --23file SNP_raw_v4_Full_20170514175358.txt
      --out SNP
      --recode vcf
    
    7840 MB RAM detected; reserving 3920 MB for main workspace.
    --23file: SNP-temporary.bed + SNP-temporary.bim + SNP-temporary.fam written.
    15125 variants with indel calls present.  '--snps-only no-DI' or
    --list-23-indels may be useful here.
    Inferred sex: male.
    610526 variants loaded from .bim file.
    1 person (1 male, 0 females) loaded from .fam.
    Using 1 thread (no multithreaded calculations invoked).
    Before main variant filters, 1 founder and 0 nonfounders present.
    Calculating allele frequencies... 10111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485868788899091929394959697989 done.
    Warning: 103 het. haploid genotypes present (see SNP.hh ); many commands treat
    these as missing.
    Total genotyping rate is 0.989512.
    610526 variants and 1 person pass filters and QC.
    Note: No phenotypes present.
    --recode vcf to SNP.vcf ... 101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899done.
    Warning: At least one VCF allele code violates the official specification;
    other tools may not accept the file.  (Valid codes must either start with a
    '<', only contain characters in {A,C,G,T,N,a,c,g,t,n}, be an isolated '*', or
    represent a breakend.)



```python
! bedtools intersect -a SNP.vcf -b clinvar.vcf > intersected.vcf
```


```python
genome = pd.read_csv('query.output.genome_summary.csv')
exome = pd.read_csv('query.output.exome_summary.csv')
exome
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Chr</th>
      <th>Start</th>
      <th>End</th>
      <th>Ref</th>
      <th>Alt</th>
      <th>Func.refGene</th>
      <th>Gene.refGene</th>
      <th>GeneDetail.refGene</th>
      <th>ExonicFunc.refGene</th>
      <th>AAChange.refGene</th>
      <th>...</th>
      <th>Otherinfo.3</th>
      <th>Otherinfo.4</th>
      <th>Otherinfo.5</th>
      <th>Otherinfo.6</th>
      <th>Otherinfo.7</th>
      <th>Otherinfo.8</th>
      <th>Otherinfo.9</th>
      <th>Otherinfo.10</th>
      <th>Otherinfo.11</th>
      <th>Otherinfo.12</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2494330</td>
      <td>2494330</td>
      <td>A</td>
      <td>G</td>
      <td>exonic</td>
      <td>TNFRSF14</td>
      <td>NaN</td>
      <td>synonymous SNV</td>
      <td>TNFRSF14:NM_003820:exon7:c.G721G:p.V241V</td>
      <td>...</td>
      <td>1</td>
      <td>2494330</td>
      <td>rs2234167</td>
      <td>A</td>
      <td>G</td>
      <td>.</td>
      <td>.</td>
      <td>PR</td>
      <td>GT</td>
      <td>0/1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>3328358</td>
      <td>3328358</td>
      <td>C</td>
      <td>T</td>
      <td>exonic</td>
      <td>PRDM16</td>
      <td>NaN</td>
      <td>synonymous SNV</td>
      <td>PRDM16:NM_022114:exon9:c.T1597T:p.S533S,PRDM16...</td>
      <td>...</td>
      <td>1</td>
      <td>3328358</td>
      <td>rs870124</td>
      <td>C</td>
      <td>T</td>
      <td>.</td>
      <td>.</td>
      <td>PR</td>
      <td>GT</td>
      <td>0/1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3328659</td>
      <td>3328659</td>
      <td>C</td>
      <td>T</td>
      <td>exonic</td>
      <td>PRDM16</td>
      <td>NaN</td>
      <td>nonsynonymous SNV</td>
      <td>PRDM16:NM_022114:exon9:c.C1898T:p.P633L,PRDM16...</td>
      <td>...</td>
      <td>1</td>
      <td>3328659</td>
      <td>rs2493292</td>
      <td>C</td>
      <td>T</td>
      <td>.</td>
      <td>.</td>
      <td>PR</td>
      <td>GT</td>
      <td>0/1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>9323910</td>
      <td>9323910</td>
      <td>A</td>
      <td>G</td>
      <td>exonic</td>
      <td>H6PD</td>
      <td>NaN</td>
      <td>synonymous SNV</td>
      <td>H6PD:NM_001282587:exon5:c.G1391G:p.R464R,H6PD:...</td>
      <td>...</td>
      <td>1</td>
      <td>9323910</td>
      <td>rs6688832</td>
      <td>A</td>
      <td>G</td>
      <td>.</td>
      <td>.</td>
      <td>PR</td>
      <td>GT</td>
      <td>0/1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>11181327</td>
      <td>11181327</td>
      <td>C</td>
      <td>T</td>
      <td>exonic</td>
      <td>MTOR</td>
      <td>NaN</td>
      <td>synonymous SNV</td>
      <td>MTOR:NM_004958:exon49:c.G6909A:p.L2303L</td>
      <td>...</td>
      <td>1</td>
      <td>11181327</td>
      <td>rs11121691</td>
      <td>C</td>
      <td>T</td>
      <td>.</td>
      <td>.</td>
      <td>PR</td>
      <td>GT</td>
      <td>0/1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1132</th>
      <td>22</td>
      <td>42523943</td>
      <td>42523943</td>
      <td>A</td>
      <td>G</td>
      <td>exonic</td>
      <td>CYP2D6</td>
      <td>NaN</td>
      <td>nonsynonymous SNV</td>
      <td>CYP2D6:NM_001025161:exon5:c.T733C:p.C245R,CYP2...</td>
      <td>...</td>
      <td>22</td>
      <td>42523943</td>
      <td>rs16947</td>
      <td>A</td>
      <td>G</td>
      <td>.</td>
      <td>.</td>
      <td>PR</td>
      <td>GT</td>
      <td>0/1</td>
    </tr>
    <tr>
      <th>1133</th>
      <td>22</td>
      <td>42523943</td>
      <td>42523943</td>
      <td>A</td>
      <td>G</td>
      <td>exonic</td>
      <td>CYP2D6</td>
      <td>NaN</td>
      <td>nonsynonymous SNV</td>
      <td>CYP2D6:NM_001025161:exon5:c.T733C:p.C245R,CYP2...</td>
      <td>...</td>
      <td>22</td>
      <td>42523943</td>
      <td>rs16947</td>
      <td>A</td>
      <td>G</td>
      <td>.</td>
      <td>.</td>
      <td>PR</td>
      <td>GT</td>
      <td>0/1</td>
    </tr>
    <tr>
      <th>1134</th>
      <td>22</td>
      <td>44342116</td>
      <td>44342116</td>
      <td>A</td>
      <td>G</td>
      <td>exonic</td>
      <td>PNPLA3</td>
      <td>NaN</td>
      <td>nonsynonymous SNV</td>
      <td>PNPLA3:NM_025225:exon9:c.A1300G:p.K434E</td>
      <td>...</td>
      <td>22</td>
      <td>44342116</td>
      <td>i6060617</td>
      <td>A</td>
      <td>G</td>
      <td>.</td>
      <td>.</td>
      <td>PR</td>
      <td>GT</td>
      <td>0/1</td>
    </tr>
    <tr>
      <th>1135</th>
      <td>22</td>
      <td>50658424</td>
      <td>50658424</td>
      <td>C</td>
      <td>T</td>
      <td>exonic</td>
      <td>TUBGCP6</td>
      <td>NaN</td>
      <td>synonymous SNV</td>
      <td>TUBGCP6:NM_020461:exon17:c.A4129A:p.T1377T</td>
      <td>...</td>
      <td>22</td>
      <td>50658424</td>
      <td>rs11703226</td>
      <td>C</td>
      <td>T</td>
      <td>.</td>
      <td>.</td>
      <td>PR</td>
      <td>GT</td>
      <td>0/1</td>
    </tr>
    <tr>
      <th>1136</th>
      <td>22</td>
      <td>51117580</td>
      <td>51117580</td>
      <td>C</td>
      <td>T</td>
      <td>exonic</td>
      <td>SHANK3</td>
      <td>NaN</td>
      <td>synonymous SNV</td>
      <td>SHANK3:NM_033517:exon6:c.T734T:p.I245I</td>
      <td>...</td>
      <td>22</td>
      <td>51117580</td>
      <td>i6060136</td>
      <td>C</td>
      <td>T</td>
      <td>.</td>
      <td>.</td>
      <td>PR</td>
      <td>GT</td>
      <td>0/1</td>
    </tr>
  </tbody>
</table>
<p>1137 rows × 139 columns</p>
</div>




```python
save = exome[['Chr', 'Start', 'Ref', 'Alt', 'Gene.refGene', 'Otherinfo.5', 'ClinVar_SIG', 'ClinVar_DIS']]
save
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Chr</th>
      <th>Start</th>
      <th>Ref</th>
      <th>Alt</th>
      <th>Gene.refGene</th>
      <th>Otherinfo.5</th>
      <th>ClinVar_SIG</th>
      <th>ClinVar_DIS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2494330</td>
      <td>A</td>
      <td>G</td>
      <td>TNFRSF14</td>
      <td>rs2234167</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>3328358</td>
      <td>C</td>
      <td>T</td>
      <td>PRDM16</td>
      <td>rs870124</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3328659</td>
      <td>C</td>
      <td>T</td>
      <td>PRDM16</td>
      <td>rs2493292</td>
      <td>Benign</td>
      <td>not_specified</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>9323910</td>
      <td>A</td>
      <td>G</td>
      <td>H6PD</td>
      <td>rs6688832</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>11181327</td>
      <td>C</td>
      <td>T</td>
      <td>MTOR</td>
      <td>rs11121691</td>
      <td>.</td>
      <td>.</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1132</th>
      <td>22</td>
      <td>42523943</td>
      <td>A</td>
      <td>G</td>
      <td>CYP2D6</td>
      <td>rs16947</td>
      <td>drug response</td>
      <td>Debrisoquine\x2c_ultrarapid_metabolism_of</td>
    </tr>
    <tr>
      <th>1133</th>
      <td>22</td>
      <td>42523943</td>
      <td>A</td>
      <td>G</td>
      <td>CYP2D6</td>
      <td>rs16947</td>
      <td>drug response</td>
      <td>Debrisoquine\x2c_ultrarapid_metabolism_of</td>
    </tr>
    <tr>
      <th>1134</th>
      <td>22</td>
      <td>44342116</td>
      <td>A</td>
      <td>G</td>
      <td>PNPLA3</td>
      <td>i6060617</td>
      <td>Likely benign</td>
      <td>Susceptibility_to_Nonalcoholic_Fatty_Liver_Dis...</td>
    </tr>
    <tr>
      <th>1135</th>
      <td>22</td>
      <td>50658424</td>
      <td>C</td>
      <td>T</td>
      <td>TUBGCP6</td>
      <td>rs11703226</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1136</th>
      <td>22</td>
      <td>51117580</td>
      <td>C</td>
      <td>T</td>
      <td>SHANK3</td>
      <td>i6060136</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>1137 rows × 8 columns</p>
</div>




```python
save[save['ClinVar_SIG'] == 'Pathogenic']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Chr</th>
      <th>Start</th>
      <th>Ref</th>
      <th>Alt</th>
      <th>Gene.refGene</th>
      <th>Otherinfo.5</th>
      <th>ClinVar_SIG</th>
      <th>ClinVar_DIS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>413</th>
      <td>6</td>
      <td>49580247</td>
      <td>C</td>
      <td>T</td>
      <td>RHAG</td>
      <td>rs16879498</td>
      <td>Pathogenic</td>
      <td>Rh-null_hemolytic_anemia\x2c_regulator_type</td>
    </tr>
    <tr>
      <th>632</th>
      <td>11</td>
      <td>36595600</td>
      <td>A</td>
      <td>G</td>
      <td>RAG1</td>
      <td>rs3740955</td>
      <td>Pathogenic</td>
      <td>not_provided</td>
    </tr>
    <tr>
      <th>633</th>
      <td>11</td>
      <td>36595600</td>
      <td>A</td>
      <td>G</td>
      <td>RAG1</td>
      <td>rs3740955</td>
      <td>Pathogenic</td>
      <td>not_provided</td>
    </tr>
  </tbody>
</table>
</div>




```python
1029
```
