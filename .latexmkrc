# Latexmk configuration file
#
# This file configures latexmk for consistent builds across different environments.
# Place in project root or ~/.config/latexmk/latexmkrc for global settings.
#
# Usage: latexmk main.tex
#

# Use pdfLaTeX by default (most ATS-compatible)
$pdf_mode = 1;

# Enable shell escape if needed (not required for this template)
# $pdflatex = 'pdflatex -shell-escape %O %S';

# Clean up auxiliary files
$clean_ext = 'aux bbl blg fls log out toc fdb_latexmk synctex.gz';

# Output directory (optional - comment out to use current directory)
# $out_dir = 'build';

# Bibtex settings (if using bibliography)
# $bibtex_use = 2;

# View PDF after build (platform-specific)
# $pdf_previewer = 'open %S';  # macOS
# $pdf_previewer = 'xdg-open %S';  # Linux
# $pdf_previewer = 'start %S';  # Windows
