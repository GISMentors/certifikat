# -*- coding: utf-8 -*-

import argparse
import re
import os

def generate(templatefile, name, date, output_file, place, logo,
             lectors):
    """Generate output .tex file based on given data and template
    """

    template_content = open(templatefile).read()
    template_content = re.sub(r'\[place\]', place, template_content)
    template_content = re.sub(r'\[name\]', name, template_content)
    template_content = re.sub(r'\[date\]', date, template_content)
    template_content = re.sub(r'\[logo\]', logo, template_content)
    a = ''
    if name.endswith('á'):
        a = 'a'
    template_content = re.sub(r'\[a\]', a, template_content)

    lector_template = """
    \\\\vfill

    {lector}\\\\\\
    """
    lectors = [lector_template.format(lector=l) for l in lectors]
    lectors = "\n".join(lectors)


    template_content = re.sub(r'\[lectors\]', lectors, template_content)

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
    parser.add_argument('--output-file', required=True, help='Jméno výstupního .tex souboru (bude uloženo do adresáře "certificates")')
    parser.add_argument('--logo', required=True, help='Logo kurzu')
    parser.add_argument('--lectors', required=True, nargs="+",
                        help='Jména lektorů')

    args = parser.parse_args()
    out = generate(args.template, args.name, args.date, args.output_file,
                   args.place, args.logo, args.lectors)
    print("Output written to %s" % (out))

if __name__ == '__main__':
    main()
