# Resume

A modular LaTeX resume template with custom commands for consistent formatting.

## Features

- **ATS-Friendly**: Single-column layout, standard fonts, and machine-readable PDF output
- **Modular Structure**: Separate files for each section, easy to customize
- **CI/CD Ready**: GitHub Actions workflow for automated PDF builds
- **DevContainer Support**: Ready-to-use development environment with LaTeX tooling

## Structure

```text
├── main.tex              # Main document entry point
├── commands.tex          # Command loader (imports constants, helpers, functions)
├── constants.tex         # User-configurable values (name, contact info)
├── helpers.tex           # Low-level utilities (links, date formatting)
├── functions.tex         # High-level commands (job, education, skills)
├── .latexmkrc            # Latexmk build configuration
└── sections/
    ├── contact.tex       # Header with name and contact links
    ├── summary.tex       # Professional summary
    ├── skills.tex        # Technical and professional competencies
    ├── experience.tex    # Work history (imports from experience/)
    ├── education.tex     # Degrees, certifications, licenses
    ├── projects.tex      # Notable projects (optional)
    └── experience/       # Individual job entries (YYYYMMDD-company-role.tex)
```

## Building

### Using Latexmk (Recommended)

```bash
# Build PDF (uses XeLaTeX via .latexmkrc)
latexmk main.tex

# Clean auxiliary files
latexmk -c
```

### Using LaTeX Directly

```bash
# XeLaTeX (recommended for Unicode and font support)
xelatex main.tex

# pdfLaTeX (faster, less font flexibility)
pdflatex main.tex

# LuaLaTeX (alternative to XeLaTeX)
lualatex main.tex
```

### Using DevContainer

1. Open the repository in VS Code with the Dev Containers extension
2. Click "Reopen in Container" when prompted
3. Edit any `.tex` file and save - the PDF will build automatically
4. View the PDF in the VS Code tab that opens

### Using GitHub Actions

The repository includes a GitHub Actions workflow that:

- Triggers on push to `main` (when `.tex` files change)
- Compiles the resume using XeLaTeX
- Uploads the PDF as a workflow artifact
- Commits the PDF back to the repository

## Customization

1. Edit `constants.tex` to update name and contact information
2. Modify section files in `sections/` to update content
3. Add new experience entries in `sections/experience/`
4. Adjust formatting in `main.tex` (margins, fonts, spacing)

## Commands Reference

### Job Entries

```latex
\job[seniority]{profession}{role}{Company}{City, ST}{start}{end}
\jobline[...]  % Same as \job, but adds line break
```

### Education, Certifications, Licenses

```latex
\educationline[id][url]{School}{Title}{YYYY/MM/DD}
\certificationline[id][url]{Issuer}{Title}{YYYY/MM/DD}
\licenseline[id][url]{Issuer}{Title}{YYYY/MM/DD}
```

### Skills

```latex
\skillline{Category}{skill1, skill2, skill3}
```

### Links

```latex
\link{text}{url}        % Underlined link
\linkplain{text}{url}   % Plain link
```

## License

See [LICENSE](LICENSE) for details.
