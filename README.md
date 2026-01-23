# Resume

A modular LaTeX resume template with custom commands for consistent formatting. Designed for Overleaf but compatible with any LaTeX distribution.

## Features

- **Modular structure**: Separate files for sections, commands, and configuration
- **Custom commands**: High-level commands for jobs, education, skills, and more
- **Modern LaTeX**: Uses expl3 (LaTeX3) syntax for robust text processing
- **ATS-friendly**: Proper PDF metadata and Unicode support for Applicant Tracking Systems
- **Overleaf ready**: Works out-of-the-box in Overleaf with no additional setup
- **Professional typography**: XCharter font and microtype for publication-quality output

## Structure

```text
├── main.tex              # Main document entry point
├── commands.tex          # Command loader (imports constants, helpers, functions)
├── constants.tex         # User-configurable values (name, contact info)
├── helpers.tex           # Low-level utilities (links, date formatting)
├── functions.tex         # High-level commands (job, education, skills)
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

### In Overleaf (Recommended)

1. Create a new project in Overleaf
2. Upload all files maintaining the directory structure
3. Set the main document to `main.tex`
4. Click "Recompile" to generate the PDF
5. The default compiler (pdfLaTeX) works perfectly

### Local Compilation

Compile with any LaTeX engine:

```bash
# pdfLaTeX (default, recommended)
pdflatex main.tex

# LuaLaTeX or XeLaTeX (for advanced font features)
lualatex main.tex
xelatex main.tex

# For a clean build with proper cross-references
pdflatex main.tex && pdflatex main.tex
```

**Requirements**: TeX Live 2020 or later, MiKTeX, or MacTeX with the following packages:
- XCharter (font)
- microtype
- geometry
- enumitem
- titlesec
- hyperref
- bookmark

## Customization

### Quick Start

1. **Edit `constants.tex`**: Update your name and contact information
2. **Modify `sections/summary.tex`**: Write your professional summary
3. **Update `sections/skills.tex`**: Add your skills by category
4. **Edit experience files**: Modify existing files in `sections/experience/` or add new ones
5. **Update `sections/education.tex`**: Add your education, certifications, and licenses
6. **Adjust `main.tex`**: Fine-tune margins, fonts, and spacing if needed

### Adding Experience

Create a new file in `sections/experience/` using the naming convention `YYYYMMDD-company-role.tex`:

```latex
\job[Senior]{Software Engineer}{Platform Team}{Company Name}{City, ST}{2024/01/15}{present}

\vspace{-9pt}
\begin{itemize}
  \item Achievement or responsibility with measurable impact
  \item Another key accomplishment
\end{itemize}
```

Then add the import to `sections/experience.tex` in reverse chronological order.

### Formatting Options

In `main.tex`, you can customize:
- **Paper size**: Change `letterpaper` to `a4paper` for international resumes
- **Margins**: Adjust the `geometry` package settings (0.5in is standard)
- **Font**: Replace `\usepackage{XCharter}` with other fonts like `libertine` or `lmodern`
- **Font size**: Change `11pt` in `\documentclass[11pt]{article}` (10pt-12pt recommended)

## Commands Reference

### Job Entries

```latex
\job[seniority]{profession}{role}{Company}{City, ST}{start}{end}

% Examples:
\job[Senior]{Software Engineer}{DevOps Platform}{Acme Corp}{Austin, TX}{2024/01/15}{present}
\job{Software Engineer}{}{Startup Inc}{Remote}{2022/06/01}{2023/12/31}
```

**Parameters**:
- `[seniority]`: Optional prefix like "Senior", "Lead", or "Principal"
- `{profession}`: Job title (e.g., "Software Engineer")
- `{role}`: Specific role/team (use empty `{}` if not applicable)
- `{Company}`: Company name
- `{City, ST}`: Location (use "Remote" for remote positions)
- `{start}`: Start date in YYYY/MM/DD format
- `{end}`: End date in YYYY/MM/DD format or "present"

**Note**: Does not add a line break. Follow with `\vspace{-9pt}` and `\begin{itemize}` for bullet points.

### Education, Certifications, Licenses

```latex
\education[id][url]{School}{Title}{YYYY/MM/DD}
\certification[id][url]{Issuer}{Title}{YYYY/MM/DD}
\license[id][url]{Issuer}{Title}{YYYY/MM/DD}

% Examples:
\education{University of Texas}{B.S. Computer Science}{2020/05/15}
\certification[ABC123][https://verify.com]{AWS}{Solutions Architect}{2024/03/20}
\license[12345][https://lookup.gov]{State Board}{Professional Engineer}{2023/06/01}
```

**Parameters**:
- `[id]`: Optional credential ID
- `[url]`: Optional verification URL (requires credential ID)
- `{Issuer/School}`: Issuing organization or institution
- `{Title}`: Degree, certification, or license title
- `{date}`: Completion/issue date in YYYY/MM/DD format

**Note**: Automatically adds line breaks for list formatting.

### Skills

```latex
\skill{Category}{skill1, skill2, skill3}

% Example:
\skill{Programming Languages}{Python, JavaScript, Go, Rust}
\skill{Cloud Platforms}{AWS, Azure, GCP}
```

**Note**: Empty items are automatically filtered out, whitespace is trimmed, and line breaks are added automatically.

### Links

```latex
\link{text}{url}        % Underlined link
\linkplain{text}{url}   % Plain link (no underline)

% Examples:
\link{Portfolio}{https://example.com}
\linkplain{github.com/username}{https://github.com/username}
```

**Note**: URLs are automatically escaped, so you don't need to escape special characters like underscores.

### Contact Information

```latex
\contactinfo{
  \contactentry{text1}{url1},
  \contactentry{text2}{url2},
  \contactentry{text3}{url3}
}

% Example:
\contactinfo{
  \contactentry{email@example.com}{mailto:email@example.com},
  \contactentry{linkedin.com/in/user}{https://linkedin.com/in/user},
  \contactentry{github.com/user}{https://github.com/user}
}
```

### Date Formatting

```latex
\dateMY{YYYY/MM/DD}  % Converts to "Mon YYYY" format

% Examples:
\dateMY{2024/03/15}  % Outputs: Mar 2024
\dateMY{present}     % Outputs: present (unchanged)
```

## Best Practices

### Resume Content

- **Keep it concise**: 1-2 pages maximum for most positions
- **Use action verbs**: Started with strong verbs (Built, Designed, Implemented, Led)
- **Quantify achievements**: Include metrics and measurable impact when possible
- **Reverse chronological order**: Most recent experience first
- **Consistent formatting**: Use the provided commands for uniform appearance
- **Tailor for each job**: Adjust summary and skills to match job requirements

### LaTeX Best Practices

- **Test regularly**: Compile after each significant change to catch errors early
- **Use comments**: Document non-obvious formatting choices with `%` comments
- **Modular files**: Keep experience entries in separate files for easier management
- **Version control**: Use Git to track changes and maintain history
- **Backup**: Keep backups of your resume, especially before major changes
- **PDF export**: Always review the final PDF, not just the LaTeX source

### ATS (Applicant Tracking System) Tips

This template is designed to be ATS-friendly:
- Uses standard section headings (Summary, Experience, Skills, Education)
- Includes proper PDF metadata for searchability
- Avoids complex tables and graphics that confuse ATS
- Uses Unicode-compliant text encoding
- Maintains clean, semantic structure

## Troubleshooting

### Common Issues

**Font not found error**:
- In Overleaf: XCharter should work automatically. If not, try changing the compiler to XeLaTeX.
- Local: Install the `XCharter` package via your TeX distribution's package manager
- Alternative: Comment out `\usepackage{XCharter}` to use the default Computer Modern font

**File not found error**:
- Ensure all imported files exist in the correct directories
- Check that file extensions are consistent (`.tex`)
- Verify the file naming convention for experience entries

**Compilation timeout in Overleaf**:
- Usually caused by infinite loops or missing `\end{}` tags
- Check that all `\begin{}` have matching `\end{}`
- Review recent changes for syntax errors

**Hyperlinks not working**:
- Ensure URLs don't have line breaks
- Special characters in URLs are handled automatically by `\link` and `\linkplain`
- For very long URLs, consider using URL shorteners

**Spacing issues**:
- Use `\vspace{-Xpt}` to adjust vertical spacing (negative values reduce space)
- Consistent spacing values are already set in `main.tex`
- For itemize spacing, adjust settings in the `\setlist[itemize]` command

**Date formatting issues**:
- Dates must be in `YYYY/MM/DD` format exactly
- Use lowercase "present" for current positions
- Invalid dates will show "???" for the month

### Getting Help

If you encounter issues:
1. Check the error message carefully - LaTeX errors usually indicate the line number
2. Compile with `pdflatex` locally for more detailed error messages
3. Try commenting out recent changes to isolate the problem
4. Consult the [Overleaf documentation](https://www.overleaf.com/learn)
5. Check the [LaTeX Stack Exchange](https://tex.stackexchange.com/)

## Project Structure Details

```text
├── main.tex              # Main document: document class, packages, PDF metadata
├── commands.tex          # Command loader (imports constants, helpers, functions)
├── constants.tex         # User-configurable values (name, contact info)
├── helpers.tex           # Low-level utilities (links, date formatting)
├── functions.tex         # High-level commands (job, education, skills)
├── .devcontainer/        # VS Code devcontainer configuration
└── sections/
    ├── contact.tex       # Header with name and contact links
    ├── summary.tex       # Professional summary
    ├── skills.tex        # Technical and professional competencies
    ├── experience.tex    # Work history (imports from experience/)
    ├── education.tex     # Degrees, certifications, licenses
    └── experience/       # Individual job entries (YYYYMMDD-company-role.tex)
        ├── 20250915-...tex
        ├── 20240115-...tex
        └── ...
```

### File Organization Philosophy

- **Separation of concerns**: Content, structure, and styling are separated
- **Reusability**: Commands defined once, used throughout
- **Maintainability**: Each experience entry in its own file
- **Configurability**: Constants file for easy customization
- **Modularity**: Easy to add/remove sections or reorganize

## Advanced Customization

### Custom Commands

You can add your own commands in `functions.tex` following the existing patterns:

```latex
\ExplSyntaxOn
\NewDocumentCommand{\mycommand}{m m}{%
  % Your command implementation
}
\ExplSyntaxOff
```

### Adding New Sections

1. Create a new file in `sections/` (e.g., `projects.tex`)
2. Import it in `main.tex`: `\import{sections/}{projects.tex}`
3. Use existing commands or create new ones as needed

### Changing Fonts

Popular font alternatives:
- `\usepackage{libertine}` - Linux Libertine (elegant serif)
- `\usepackage{lmodern}` - Latin Modern (enhanced Computer Modern)
- `\usepackage{helvet}` - Helvetica (sans-serif)
- For XeLaTeX/LuaLaTeX: `\setmainfont{Font Name}` with fontspec

### PDF Customization

Edit the `\hypersetup{}` block in `main.tex` to customize PDF metadata:
- `pdftitle`: Document title
- `pdfauthor`: Your name
- `pdfkeywords`: Keywords for PDF search

## Contributing

This template follows modern LaTeX best practices:
- Uses expl3 (LaTeX3) for robust text processing
- Properly scoped variables with `\l__cv_` prefix
- Comprehensive documentation and comments
- Modular, maintainable structure

Feel free to fork and customize for your needs!

## License

See [LICENSE](LICENSE) for details.
