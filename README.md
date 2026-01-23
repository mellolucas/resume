# Resume

A modular LaTeX resume template with custom commands for consistent formatting.

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

Compile with any LaTeX engine:

```bash
# pdfLaTeX (default)
pdflatex main.tex

# LuaLaTeX or XeLaTeX (for advanced font features)
lualatex main.tex
xelatex main.tex
```

## Customization

1. Edit `constants.tex` to update name and contact information
2. Modify section files in `sections/` to update content
3. Add new experience entries in `sections/experience/`
4. Adjust formatting in `main.tex` (margins, fonts, spacing)

## Commands Reference

### Job Entries

```latex
\job[seniority][role]{profession}{Company}{City, ST}{start}{end}
```

### Education, Certifications, Licenses

```latex
\education[id][url]{School}{Title}{YYYY/MM/DD}
\certification[id][url]{Issuer}{Title}{YYYY/MM/DD}
\license[id][url]{Issuer}{Title}{YYYY/MM/DD}
```

### Skills

```latex
\skill[Category]{skill1, skill2, skill3}
```

### Links

```latex
\link{text}{url}        % Underlined link
\linkplain{text}{url}   % Plain link
```

## License

See [LICENSE](LICENSE) for details.
