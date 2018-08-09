# bam_vs_fastq.py
Checks whether the read numbers in the fastq files (single or paired-end) matches the total read numbers in the bam file. If the read numbers match, then the fastq files can be removed to save disk space. 


# Usage
```$ python bam_vs_fastq.py -h
usage: bam_vs_fastq.py [-h] -b BAM -fq FASTQ [FASTQ ...] [-o OUTPUT_DIR]

optional arguments:
  -h, --help            show this help message and exit
  -b BAM, --bam BAM     Bam file
  -fq FASTQ [FASTQ ...], --fastq FASTQ [FASTQ ...]
                        FASTQ files, if paired end reads, then type two fastq
                        file paths separaated by space
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
                        Output directory
```
