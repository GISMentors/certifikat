Certifikáty GISMentors
======================
Šablony uloženy v adresáři `templates`

pro vygenerování použít např.:

    python generate-certificate.py --template templates/grass-zacatecnik.tex \
    --name "Ing. Pepa Popovič" --date "10. -- 11. listopadu 2014" \
    --date-signed "11. listopadu 2014" --output-file pokus1.tex
    (cd certificates/ && pdflatex pokus1.tex && xpdf pokus1.pdf)
    