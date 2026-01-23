# Resume

A modular LaTeX resume template with custom commands for consistent formatting and ATS (Applicant Tracking System) optimization.

## Features

- **ATS-Friendly**: Single-column layout, standard section headers, Unicode-compliant PDF output
- **Modular Structure**: Separate files for sections, constants, and reusable commands
- **Multi-Engine Support**: Works with pdfLaTeX, LuaLaTeX, and XeLaTeX
- **PDF Metadata**: Automatic title, author, and keywords for search engines and accessibility
- **GitHub Actions**: Automated PDF generation on push

## Structure

```text
├── main.tex              # Main document entry point
├── commands.tex          # Command loader (imports constants, helpers, functions)
├── constants.tex         # User-configurable values (name, contact info)
├── helpers.tex           # Low-level utilities (links, date formatting)
├── functions.tex         # High-level commands (job, education, skills)
├── sections/
│   ├── contact.tex       # Header with name and contact links
│   ├── summary.tex       # Professional summary
│   ├── skills.tex        # Technical and professional competencies
│   ├── experience.tex    # Work history (imports from experience/)
│   ├── education.tex     # Degrees, certifications, licenses
│   ├── projects.tex      # Notable projects (optional)
│   └── experience/       # Individual job entries (YYYYMMDD-company-role.tex)
└── .github/
    └── workflows/
        └── build.yml     # GitHub Actions workflow for PDF generation
```

## Building

### Local Compilation

Compile with any LaTeX engine:

```bash
# pdfLaTeX (recommended for ATS compatibility)
pdflatex main.tex

# LuaLaTeX or XeLaTeX (for advanced font features)
lualatex main.tex
xelatex main.tex
```

### Using Overleaf

1. Upload all `.tex` files to a new Overleaf project
2. Set `main.tex` as the main document
3. Click "Recompile" to generate the PDF

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
