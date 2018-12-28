#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys
import csv
import subprocess
import shutil
import pathlib

from generate_certificate import generate


def generate_from_csv(csvfile, target, templatefile, date, place, logo,
                      lectors):
    """Generate output .tex file based on given CSV data and template
    """
    logo_file = pathlib.Path(logo).name
    try:
        with open(csvfile) as fd:
            csvreader = csv.reader(fd, delimiter=',', quotechar='"')
            # next(fd) # skip first (header) line
            for row in csvreader:
                name = row[0].strip()

                output_file = str(pathlib.Path(target, '{}.tex'.format(name)))
                generate(templatefile, name, date, output_file, place,
                         logo_file, lectors)

        logo_dst = str(pathlib.Path(target, pathlib.Path(logo).name))
        shutil.copyfile(logo, logo_dst)
        shutil.copyfile("images/placka-eps-converted-to.pdf",
                        str(pathlib.Path(
                            target, "placka-eps-converted-to.pdf"
                        )))
    except Exception as e:
        sys.exit(e)


def generate_pdf():
    """Generate .pdf file from .tex using pdflatex
    """
    print("Creating PDFs...")
    for file in os.listdir('.'):
        if os.path.splitext(file)[1] != '.tex':
            continue
        subprocess.Popen(['pdflatex', file])


def main():
    parser = argparse.ArgumentParser(
        description='Generate certificates from CSV file'
    )
    parser.add_argument('--csv', required=True, help='Soubor .csv')
    parser.add_argument(
        '--target', required=True,
        help='Cílový adresář pro uložení šablon a obrázků.'
    )
    parser.add_argument(
        '--template', required=True, help='Soubor .tex s šablonou'
    )
    parser.add_argument(
        '--date', required=True, help='Datum konání (použijte zápis pro LaTeX'
    )
    parser.add_argument('--place', help='Místo konání', default='Praze')
    parser.add_argument(
        '--logo', required=True, help='Plná cesta k logo souboru s kurzem'
    )
    parser.add_argument(
        '--lectors', required=True, nargs="+", help='Seznam školitelů'
    )

    args = parser.parse_args()

    if not os.path.exists(args.target):
        os.makedirs(args.target)

    generate_from_csv(args.csv, args.target,
                      args.template, args.date, args.place, args.logo,
                      args.lectors)
    os.chdir(args.target)
    generate_pdf()


if __name__ == '__main__':
    main()
