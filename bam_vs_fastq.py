#!/home/users/cjyoon/anaconda3/bin/python
import sys
import os
import subprocess
import shlex
import re
import argparse
import gzip 
import multiprocessing

def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bam', required=True, help='Bam file')
    parser.add_argument('-fq', '--fastq', required=True, help='FASTQ files, if paired end reads, then type two fastq file paths separaated by space', nargs='+')


    parser.add_argument('-o', '--output_dir', required=False, default=os.getcwd(), help='Output directory')
    args = vars(parser.parse_args())

    return args['bam'], args['fastq'], args['output_dir']


def open_file(filepath):
    '''open gzip file with gzip package, and uncompressed file with just open'''
    if filepath.endswith('.gz'):
        return gzip.open(filepath, 'rt')
    else:
        return open(filepath, 'r')

def get_bam_read_count(bam):
    '''total read count in the bam file including unmapped reads'''
    view = subprocess.Popen(shlex.split('samtools view -F 2048 ' + bam), stdout=subprocess.PIPE)
    counts = subprocess.check_output(shlex.split('wc -l'), stdin=view.stdout)
    return int(counts.decode('utf-8').strip())

def get_fastq_read_count(fastq):
    '''total read count in fastq file'''
    file_handle = open_file(fastq)
    count = 0 
    for line in file_handle:
        if line.strip() == '+':
            count += 1

    return count

def main():
    bam, fastq_files, output_dir = argument_parser()
    with multiprocessing.Pool(3) as pool:
        fq_read_counts = pool.map(get_fastq_read_count, fastq_files)
        bam_read_counts = pool.map(get_bam_read_count, [bam])

    print('fastq reads: ' + str(fq_read_counts))
    print('bam_read_counts: ' + str(bam_read_counts))
    if sum(bam_read_counts) == sum(fq_read_counts):
        print('read count matching')
    else:
        print('read count NOT matching')
if __name__=='__main__':
    main()


