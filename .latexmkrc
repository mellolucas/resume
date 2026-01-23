# .latexmkrc - Configuration for latexmk build automation
#
# Usage: latexmk              (build with default settings)
#        latexmk -pvc         (continuous preview mode)
#        latexmk -c           (clean auxiliary files)
#        latexmk -C           (clean all generated files including PDF)
#
# This file configures latexmk for optimal resume compilation

# Use pdfLaTeX as the default engine (recommended for this template)
$pdf_mode = 1;

# Specify the main document
@default_files = ('main.tex');

# Output directory for auxiliary files (keeps root clean)
# Uncomment to use a build directory:
# $out_dir = 'build';

# Always create PDF output
$postscript_mode = 0;
$dvi_mode = 0;

# Enable synctex for editor integration (jump from PDF to source)
$pdflatex = 'pdflatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';

# Preview PDF with system default viewer
# Uncomment and adjust for your platform:
# $pdf_previewer = 'start';        # Windows
# $pdf_previewer = 'open';         # macOS
# $pdf_previewer = 'xdg-open';     # Linux

# Automatically clean up auxiliary files after successful compilation
# $cleanup_mode = 1;

# Watch for changes in imported files
# This ensures latexmk recompiles when section files are modified
$recorder = 1;

# Customize cleanup: specify which extensions to remove with -c
@generated_exts = qw(aux bbl bcf blg fdb_latexmk fls log out run.xml synctex.gz toc);

# Extra cleanup with -C (removes PDF too)
$clean_ext = 'synctex.gz';

# Show used CPU time
$show_time = 1;

# Number of compilation passes (usually 1 is enough for resumes)
$max_repeat = 2;

# Warnings and errors
$silence_logfile_warnings = 0;
$warnings_as_errors = 0;
