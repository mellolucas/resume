# ---------- .latexmkrc ----------
#
# Latexmk configuration for the resume project.
# Used by LaTeX Workshop and command-line builds.
#
# Build: latexmk main.tex
# Clean: latexmk -c
#

# Use XeLaTeX for better Unicode and font support
$pdf_mode = 5;  # 5 = xelatex

# XeLaTeX command with options
$xelatex = 'xelatex -file-line-error -halt-on-error -interaction=nonstopmode -synctex=1 %O %S';

# Output directory (optional - uncomment to use)
# $out_dir = 'build';

# Clean up auxiliary files
$clean_ext = 'aux bbl blg fdb_latexmk fls log out synctex.gz';
