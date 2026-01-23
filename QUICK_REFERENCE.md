# LaTeX Resume Quick Reference

## Quick Start Checklist

- [ ] Update `constants.tex` with your name and contact information
- [ ] Edit `sections/summary.tex` with your professional summary
- [ ] Update `sections/skills.tex` with your skills by category
- [ ] Modify experience files in `sections/experience/` or create new ones
- [ ] Update `sections/education.tex` with your credentials
- [ ] Compile in Overleaf or locally with `pdflatex main.tex`
- [ ] Review the generated PDF for formatting and content

## Common Tasks

### Adding a New Job

1. Create `sections/experience/YYYYMMDD-company-role.tex`
2. Add content using the template:
```latex
\job[Senior]{Software Engineer}{Team Name}{Company}{City, ST}{2024/01/15}{present}

\vspace{-9pt}
\begin{itemize}
  \item Key achievement with measurable impact
  \item Another responsibility or accomplishment
  \item Technical contribution or innovation
\end{itemize}
```
3. Import in `sections/experience.tex` (newest first)

### Adjusting Spacing

- Between sections: Modify `\vspace{-Xpt}` in `main.tex`
- Within experience: Adjust `\vspace{-9pt}` after `\job` command
- Bullet points: Edit `\setlist[itemize]` settings in `main.tex`

### Changing Paper Size

In `main.tex`, line 16:
- North America: `letterpaper`
- International: `a4paper`

### Changing Font

In `main.tex`, replace line 23:
- Current: `\usepackage{XCharter}`
- Alternative: `\usepackage{libertine}` or `\usepackage{lmodern}`
- Default: Comment out the line for Computer Modern

## Date Format

Always use `YYYY/MM/DD` format:
- ✅ Correct: `2024/03/15`
- ❌ Wrong: `03/15/2024`, `15-03-2024`, `March 2024`
- ✅ Current position: use lowercase `present`

## Command Syntax Quick Reference

```latex
% Jobs
\job[Seniority]{Title}{Role}{Company}{Location}{YYYY/MM/DD}{YYYY/MM/DD|present}

% Education
\educationline[id][url]{School}{Degree}{YYYY/MM/DD}

% Certifications
\certificationline[id][url]{Issuer}{Title}{YYYY/MM/DD}

% Licenses
\licenseline[id][url]{Issuer}{Title}{YYYY/MM/DD}

% Skills
\skillline{Category}{skill1, skill2, skill3}

% Links
\link{visible text}{url}           % Underlined
\linkplain{visible text}{url}      % Plain
```

## Compilation Commands

```bash
# Basic compilation
pdflatex main.tex

# With latexmk (automatic dependency tracking)
latexmk                 # Build once
latexmk -pvc           # Continuous preview mode
latexmk -c             # Clean auxiliary files
latexmk -C             # Clean everything including PDF

# Manual cleanup
rm -f *.aux *.log *.out *.fls *.fdb_latexmk *.synctex.gz
```

## Troubleshooting Quick Fixes

| Problem | Solution |
|---------|----------|
| Font not found | Comment out `\usepackage{XCharter}` in main.tex |
| File not found | Check file paths and `.tex` extensions |
| Spacing issues | Adjust `\vspace{-Xpt}` values (negative reduces space) |
| Date shows "???" | Use `YYYY/MM/DD` format exactly |
| Link not working | Ensure no line breaks in URL |
| Won't compile | Check for unmatched `\begin{}` and `\end{}` |

## Best Practices

### Content
- Keep it concise (1-2 pages)
- Use action verbs (Built, Designed, Led, Implemented)
- Quantify achievements with metrics
- Tailor for each job application

### Formatting
- Consistent date format throughout
- Reverse chronological order (newest first)
- Parallel structure in bullet points
- Professional email address

### Technical
- Test compile after each major change
- Keep backups of working versions
- Use version control (Git)
- Review final PDF, not just source

## File Structure at a Glance

```
main.tex              ← Compile this file
├── commands.tex      ← Loads all custom commands
│   ├── constants.tex ← YOUR INFO HERE
│   ├── helpers.tex   ← Internal utilities
│   └── functions.tex ← Command definitions
└── sections/
    ├── contact.tex   ← Header (uses constants.tex)
    ├── summary.tex   ← YOUR SUMMARY HERE
    ├── skills.tex    ← YOUR SKILLS HERE
    ├── experience.tex
    │   └── experience/
    │       └── *.tex ← YOUR JOBS HERE
    └── education.tex ← YOUR EDUCATION HERE
```

## Resources

- [Overleaf Documentation](https://www.overleaf.com/learn)
- [LaTeX Stack Exchange](https://tex.stackexchange.com/)
- [CTAN Package Documentation](https://www.ctan.org/)
- Full documentation: See `README.md`
