#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys
import csv
import subprocess
import atexit

from generate_certificate import generate

def generate_from_csv(csvfile, templatefile, date, place):
    """Generate output .tex file based on given CSV data and template
    """
    try:
        with open(csvfile) as fd:
            csvreader = csv.reader(fd, delimiter=',', quotechar='"')
            next(fd) # skip first (header) line
            for row in csvreader:
                name=row[0].strip()

                output_file = '{}.tex'.format(name)
                generate(templatefile, name, date, date, output_file, place)

    except Exception as e:
        sys.exit(e)

def generate_pdf():
    """Generate .pdf file from .tex using pdflatex
    """
    print("Creating PDFs...")
    os.chdir('certificates')
    for file in os.listdir():
        if os.path.splitext(file)[1] != '.tex':
            continue
        subprocess.Popen(['pdflatex', file])

def cleanup():
    """Clean up
    """
    print("Cleaning...")
    for file in os.listdir():
        if os.path.splitext(file)[1] != '.pdf':
            continue
        print (file)
        os.remove(file)

def main():
    parser = argparse.ArgumentParser(description='Generate certificates from CSV file')
    parser.add_argument('--csv', required=True, help='Soubor .csv')
    parser.add_argument('--template', required=True, help='Soubor .tex s šablonou')
    parser.add_argument('--date', required=True, help='Datum konání (použijte zápis pro LaTeX')
    parser.add_argument('--place', help='Místo konání', default='Praze')

    args = parser.parse_args()
    generate_from_csv(args.csv, args.template, args.date, args.place)
    generate_pdf()
        
if __name__ == '__main__':
    #atexit.register(cleanup)
    main()
