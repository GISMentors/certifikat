Certifikáty GISMentors
======================
Šablony uloženy v adresáři `templates`

pro vygenerování použít např.:

    python3 generate_certificate.py --template templates/grass-zacatecnik.tex \
    --logo "images/qgislogo_vector.eps",
    --name "Ing. Pepa Popovič" --date "10. -- 11. listopadu 2014" \
    --place "Olomouci" \
    --date-signed "11. listopadu 2014" --output-file pokus1.tex
    (cd certificates/ && pdflatex pokus1.tex && xpdf pokus1.pdf)

ve for smyčce:

    IFS=$'\n'       # make newlines the only separator
    for i in `cat /tmp/ucastnici.txt`; do
        python3 generate_certificates.py --template .... ;
    done

Další možností je generovat certifikáty přímo z CSV souboru:

    ./generate_certificates_from_csv.py \
    --logo "images/qgislogo_vector.eps",
    --template templates/qgis-zacatecnik.tex \
    --date '3. března 2017' \
    --csv /tmp/qgis-3-3-2017.csv
