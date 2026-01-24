# Resume

A modular LaTeX resume template with custom commands for consistent formatting and ATS (Applicant Tracking System) optimization.

## Features

- **ATS-Friendly**: Single-column layout, standard section headers, Unicode-compliant PDF output
- **Modular Structure**: Separate files for sections, constants, and reusable commands
- **Multi-Engine Support**: Works with pdfLaTeX, LuaLaTeX, and XeLaTeX
- **PDF Metadata**: Automatic title, author, and keywords for search engines and accessibility
- **GitHub Actions**: Automated PDF generation on push
- **Dev Container**: Pre-configured LaTeX development environment

## Structure

```text
├── main.tex              # Main document entry point
├── commands.tex          # Command loader (imports constants, helpers, functions)
├── constants.tex         # User-configurable values (name, contact info)
├── helpers.tex           # Low-level utilities (links, date formatting)
├── functions.tex         # High-level commands (job, education, skills)
├── .latexmkrc            # Latexmk configuration for consistent builds
├── sections/
│   ├── contact.tex       # Header with name and contact links
│   ├── summary.tex       # Professional summary
│   ├── skills.tex        # Technical and professional competencies
│   ├── experience.tex    # Work history (imports from experience/)
│   ├── education.tex     # Degrees, certifications, licenses
│   ├── projects.tex      # Notable projects (optional)
│   └── experience/       # Individual job entries (YYYYMMDD-company-role.tex)
├── .devcontainer/
│   └── devcontainer.json # VS Code dev container configuration
└── .github/
    └── workflows/
        └── build.yml     # GitHub Actions workflow for PDF generation
```

## Development Environment Setup

### Option 1: VS Code Dev Container (Recommended)

The easiest way to get started. Uses [qmcgaw/latexdevcontainer](https://github.com/qdm12/latexdevcontainer), a well-maintained LaTeX development container with TeX Live 2025.

**Requirements:**

- [Docker](https://www.docker.com/products/docker-desktop) installed and running
- [VS Code](https://code.visualstudio.com/) with [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

**Steps:**

1. Clone this repository
2. Open the folder in VS Code
3. When prompted, click "Reopen in Container" (or use Command Palette: `Dev Containers: Reopen in Container`)
4. Wait for the container to build (~4GB download on first run)
5. Edit `.tex` files - PDF auto-generates on save

**Container Features:**

- TeX Live 2025 (full scheme with all packages)
- [LaTeX Workshop extension](https://github.com/James-Yu/LaTeX-Workshop) for auto-build and PDF preview
- `latexmk` for intelligent compilation
- `chktex` for LaTeX linting
- Spell checking with Code Spell Checker

### Option 2: GitHub Codespaces

Open this repository in GitHub Codespaces for instant cloud development:

1. Click "Code" → "Codespaces" → "Create codespace on main"
2. Wait for the environment to build
3. Start editing - PDF generates automatically on save

### Option 3: Local Linux Installation

Install TeX Live directly on your system. Two approaches:

#### Using Distribution Packages (Simpler)

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install texlive-full latexmk

# Fedora
sudo dnf install texlive-scheme-full latexmk

# Arch Linux
sudo pacman -S texlive-full latexmk
```

> **Note:** Distribution packages may be 1-2 years behind the latest TeX Live release.

#### Using Vanilla TeX Live (Latest Version)

For the latest TeX Live 2025 with `tlmgr` package management:

```bash
# Download and extract installer
wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
tar -xzf install-tl-unx.tar.gz
cd install-tl-20*

# Run installer (interactive mode)
sudo perl ./install-tl

# Or non-interactive full installation
sudo perl ./install-tl --no-interaction

# Add to PATH (add to ~/.bashrc or ~/.profile for persistence)
export PATH=/usr/local/texlive/2025/bin/x86_64-linux:$PATH

# Verify installation
pdflatex --version
```

### Option 4: Overleaf (Online)

No installation required:

1. Create an account at [Overleaf](https://www.overleaf.com)
2. Create a new project and upload all `.tex` files
3. Set `main.tex` as the main document
4. Click "Recompile" to generate the PDF

## Building the Resume

### Using latexmk (Recommended)

```bash
# Build PDF (uses .latexmkrc configuration)
latexmk main.tex

# Build and watch for changes
latexmk -pvc main.tex

# Clean auxiliary files
latexmk -c

# Full clean (including PDF)
latexmk -C
```

### Using pdfLaTeX Directly

```bash
# Single compilation (may need multiple runs for references)
pdflatex main.tex

# Full compilation (recommended)
pdflatex main.tex && pdflatex main.tex
```

### Using LuaLaTeX or XeLaTeX

For advanced font features or Unicode support:

```bash
lualatex main.tex
# or
xelatex main.tex
```

### GitHub Actions

The repository includes automated PDF generation:

- **On push to main**: Compiles and uploads PDF as artifact
- **On pull request**: Compiles to validate changes
- **Manual dispatch**: Option to create a GitHub release with the PDF

## Customization

1. Edit `constants.tex` to update name and contact information
2. Modify section files in `sections/` to update content
3. Add new experience entries in `sections/experience/`
4. Adjust formatting in `main.tex` (margins, fonts, spacing)

## ATS Optimization

This template follows best practices for Applicant Tracking System compatibility:

### What's Already Included

- ✅ Single-column layout (most ATS-friendly)
- ✅ Standard section headers (Experience, Education, Skills)
- ✅ Unicode-compliant PDF via `glyphtounicode`
- ✅ No graphics, images, or tables that confuse ATS
- ✅ PDF metadata (title, author, keywords)
- ✅ Clean text extraction via professional fonts

### Tips for Maximum Compatibility

1. **Test your PDF**: Copy-paste the PDF content into a plain text editor to verify text extraction
2. **Use standard section names**: The template uses ATS-recognized headers
3. **Include keywords**: Match keywords from job descriptions in your skills and experience
4. **Keep formatting simple**: Avoid excessive styling or custom symbols
5. **Verify links**: Ensure all hyperlinks are functional and professional

### Testing ATS Readability

```bash
# Extract text from PDF to verify ATS readability
pdftotext resume.pdf - | head -50
```

Or use online tools like [Jobscan](https://www.jobscan.co/) or [Resumeworded](https://resumeworded.com/) to test parsing.

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

## Best Practices

### Content Guidelines

- **Summary**: 2-4 sentences, lead with title and years of experience
- **Experience**: Focus on achievements with metrics, not just responsibilities
- **Skills**: Group by category, list in order of proficiency
- **Education**: Include relevant certifications and credentials

### Formatting Guidelines

- Keep resume to 1 page for <5 years experience, 2 pages max for senior roles
- Use consistent date formats (Mon YYYY)
- Maintain reverse chronological order
- Tailor content to each job application

## License

See [LICENSE](LICENSE) for details.
