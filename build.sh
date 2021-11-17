#!/bin/bash
pdflatex dotgrid.tex
pdflatex dotgrid.tex
convert -density 300 dotgrid.pdf -quality 90 dotgrid.png
python paginate.py

# broken up like this because imagemagik keeps crashing on memory limits
echo "Converting images to PDFs"
convert pages/dotgrid_paginated-1*.png pages/signet-1.pdf
convert pages/dotgrid_paginated-2*.png pages/signet-2.pdf
convert pages/dotgrid_paginated-3*.png pages/signet-3.pdf
convert pages/dotgrid_paginated-4*.png pages/signet-4.pdf
convert pages/dotgrid_paginated-5*.png pages/signet-5.pdf
gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=journal.pdf ./pages/signet*.pdf

# Cleanup
rm dotgrid.png dotgrid.aux dotgrid.log dotgrid.pdf

echo "FINISHED"
