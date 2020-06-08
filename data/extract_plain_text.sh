#!/bin/bash

export PYTHONIOENCODING=utf-8

cat | while IFS=$' ' read -r DIRECTORY SCRIPT_NAME ; do
    find websites/$DIRECTORY -type f -name '*.html' | \
    while read HTML; do
        OUT_TXT=$(echo $HTML | sed 's/^websites/plain_text/;s#html$#txt#')
        OUT_DIR=$(echo $OUT_TXT | sed 's#/[^/]*$##')
        echo $OUT_TXT
        mkdir -p "$OUT_DIR"
        html2text --ignore-emphasis --ignore-links --ignore-images --ignore-tables --decode-errors=ignore < $HTML | \
            plain_text_scripts/plaintext_"$SCRIPT_NAME".py > "$OUT_TXT"
        TOTAL_LINES=$(wc -l < "$OUT_TXT")
        EMPTY_LINES=$(grep '^$' "$OUT_TXT" | wc -l)
        if [[ ($TOTAL_LINES -lt 20) || ($(echo "($EMPTY_LINES / $TOTAL_LINES) > 0.5" | bc -l) -eq 1) ]]; then
            rm "$OUT_TXT"
            echo "Too short or sparse, deleted ($TOTAL_LINES lines, $EMPTY_LINES empty)."
        fi
    done
done << EOF
lemire.me lemire
www.danielslater.net danielslater
blogs.technet.microsoft.com microsoft
www.machinedlearnings.com machinedlearning
blog.kaggle.com kaggle
arstechnica.com arstechnica
blog.wtf.sg blogwtf
charlesmartin14.wordpress.com charlesmartin14
colah.github.io colah
developers.googleblog.com googleblog
karpathy.github.io karpathy
nlpers.blogspot.com nlpers
research.googleblog.com googleblog
techcrunch.com techcrunch
thehackernews.com hackernews
www.joelonsoftware.com joelonsoftware
www.virtuouscode.com virtuouscode
www.wired.com wired
www.foldl.me foldl
timdettmers.com timdettmers
odetocode.com odetocode
blog.codinghorror.com codinghorror
www.hanselman.com hanselman
thedailywtf.com thedailywtf
github.com github
davidwalsh.name davidwalsh
www.catonmat.net catonmat
martinfowler.com martinfowler
highscalability.com highscalability
EOF
