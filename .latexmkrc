# Latexmk configuration file
#
# Latexmk automates the LaTeX compilation process, running pdflatex (or other
# engines) the correct number of times and handling bibliographies automatically.
#
# Usage:
#   latexmk main.tex      # Build PDF
#   latexmk -pvc main.tex # Build and watch for changes (continuous preview)
#   latexmk -c            # Clean auxiliary files
#   latexmk -C            # Full clean (including PDF)
#
# Documentation: https://mg.readthedocs.io/latexmk.html
#

# Use pdfLaTeX by default (most ATS-compatible)
# Options: 1 = pdflatex, 4 = lualatex, 5 = xelatex
$pdf_mode = 1;

# pdfLaTeX command with recommended options
$pdflatex = 'pdflatex -file-line-error -halt-on-error -interaction=nonstopmode -synctex=1 %O %S';

# LuaLaTeX command (if using $pdf_mode = 4)
$lualatex = 'lualatex -file-line-error -halt-on-error -interaction=nonstopmode -synctex=1 %O %S';

# XeLaTeX command (if using $pdf_mode = 5)
$xelatex = 'xelatex -file-line-error -halt-on-error -interaction=nonstopmode -synctex=1 %O %S';

# Additional file extensions to clean with latexmk -c
@generated_exts = (@generated_exts, 'synctex.gz', 'synctex', 'run.xml');

# Output directory (optional - uncomment to keep build files separate)
# $out_dir = 'build';
# $aux_dir = 'build';

# Bibtex settings (if using bibliography)
# $bibtex_use = 2;  # Run bibtex/biber when needed

# PDF viewer (optional - platform-specific, uncomment one)
# $pdf_previewer = 'open %S';       # macOS
# $pdf_previewer = 'xdg-open %S';   # Linux
# $pdf_previewer = 'start %S';      # Windows
