#! /bin/bash

set -e

update_cropped_images()
{
    for i in *.pdf; do
        if [[ $i == *"-crop.pdf" ]]; then
            continue
        fi
        outf="${i%.pdf}-crop.pdf"
        if test "$i" -nt "$outf"; then
            pdfcrop "$i" "$outf"
        fi
    done
}

(cd images; update_cropped_images)

if [[ "$1" = "watch" ]]; then
    git ls-files | entr ./run-org-conversion.sh
else
    ./run-org-conversion.sh
fi

echo "NOTES BUILD SUCCESSFULLY COMPLETED"

# vim: sw=4
