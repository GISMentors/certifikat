# -*- coding: utf-8 -*-

import argparse
import re
import os

def generate(templatefile, name, date, date_signed, output_file, place, logo):
    """Generate output .tex file based on given data and template
    """

    template_content = open(templatefile).read()
    template_content = re.sub(r'\[place\]', place, template_content)
    template_content = re.sub(r'\[name\]', name, template_content)
    template_content = re.sub(r'\[date\]', date, template_content)
    template_content = re.sub(r'\[date-signed\]', date_signed, template_content)
    template_content = re.sub(r'\[logo\]', logo, template_content)
    a = ''
    if name.endswith('á'):
        a = 'a'
    template_content = re.sub(r'\[a\]', a, template_content)

    outputfile = open(output_file, 'w')
    outputfile.write(template_content)
    outputfile.close()

    return output_file

def main():
    parser = argparse.ArgumentParser(description='Generate certificate')
    parser.add_argument('--template', required=True, help='Soubor .tex s šablonou')
    parser.add_argument('--name', required=True, help='Jméno účastníka')
    parser.add_argument('--date', required=True, help='Datum konání (použijte zápis pro LaTeX')
    parser.add_argument('--place', required=True, help='Místo konání')
    parser.add_argument('--date-signed', required=True, help='Datum podpisu (použijte zápis pro LaTeX')
    parser.add_argument('--output-file', required=True, help='Jméno výstupního .tex souboru (bude uloženo do adresáře "certificates")')

    args = parser.parse_args()
    out = generate(args.template, args.name, args.date, args.date_signed, args.output_file, args.place)
    print("Output written to %s" % (out))

if __name__ == '__main__':
    main()
