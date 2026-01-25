# Resume

<details><summary><strong>🏗️ Work in Progress 🚧</strong></summary>

![repo-self-setup](/../../actions/workflows/_repo-self-setup.yaml/badge.svg)
![build](/../../actions/workflows/build.yaml/badge.svg)
![publish](/../../actions/workflows/publish.yaml/badge.svg)

A modular LaTeX resume template with custom commands for consistent formatting and ATS (Applicant Tracking System) optimization.

## Features

- [x] **ATS-Friendly**: Single-column layout, standard section headers, Unicode-compliant PDF output
- [x] **Modular Structure**: Separate files for sections, constants, and reusable commands
- [x] **Multi-Engine Support**: Works with pdfLaTeX, LuaLaTeX, and XeLaTeX
- [x] **PDF Metadata**: Automatic title, author, and keywords for search engines and accessibility
- [ ] **GitHub Actions**: Automated PDF generation on push

## Create Your Own Resume

1. [Start from this template](https://github.com/new?template_owner=mellolucas&template_name=resume&owner=%40me&name=resume&description=Curriculum%20VitAI&prompt=placeholder-use-custom-agent) to create a new repository for your resume project. Unless you don't want to, then you can just skip to step 3's last option.
2. At the creation prompt, after reviewing the pre-filled details, click on `Create repository` at the bottom of the page.
3. Wait until [GitHub Actions](/../../actions/workflows/_repo-self-setup.yaml) set things up for you (takes less than a minute! Refresh the page to check the status)
4. Open your project in your editor of choice:
   - [![Spin-up a Codespace](https://img.shields.io/badge/Codespace-_?style=flat&logo=github&label=Spin-up%20a&labelColor=2f363d&color=24292e)](https://codespaces.new/mellolucas/resume?quickstart=1) and start coding right away in a full-featured development environment tailored to your needs
   - [![Open in GitHub.dev Web Editor](https://img.shields.io/badge/GitHub.dev-_?style=flat&logo=refinedgithub&logoColor=white&label=Open%20in&labelColor=2f363d&color=24292e)](https://github.dev/mellolucas/resume) if you prefer a lightweight browser-based quick editing experience
   - [![Clone locally with VS Code](https://img.shields.io/badge/Clone_with-VS_Code-0098FF.svg?style=flat&logo=git&logoColor=white)](vscode://vscode.git/clone?url=https://github.com/mellolucas/resume) to work offline from your good-old and trusty IDE
   - [![Clone locally with VS Code Insiders](https://img.shields.io/badge/Clone_with-VS_Code_Insiders-24bfa5.svg?style=flat&logo=gitforwindows&logoColor=white)](vscode-insiders://vscode.git/clone?url=https://github.com/mellolucas/resume) to work offline from your good-new oftentimes-trusty IDE
   - [![Download ZIP](https://img.shields.io/badge/%E2%BF%BB_Download-ZIP-_.svg?color=yellow&style=flat)](/../../archive/refs/heads/main.zip) and upload to [Overleaf](https://www.overleaf.com/) if you just don't want the hassle. If versioning is not your thing, you could just skip the whole GitHub part and download mine and go live your best life... who needs version control anyway? Yeah, c'mon! To live is to risk it all! Otherwise you’re just an inert chunk of randomly assembled molecules drifting wherever the universe blows you!!

5. <todo from here>

## Create Your Own Resume

1. [Start from this template](https://github.com/new?template_owner=mellolucas&template_name=resume&owner=%40me&name=resume&description=Curriculum%20VitAI&prompt=placeholder-use-custom-agent) to create a new repository for your resume project. Unless you don't want to, then you can just skip to step 3's last option.
2. At the creation prompt, after reviewing the pre-filled details, click on `Create repository` at the bottom of the page.
3. Wait until [GitHub Actions](/../../actions/workflows/_repo-self-setup.yaml) set things up for you (takes less than a minute! Refresh the page to check the status)
4. Open your project in your editor of choice:
   - [![Spin-up a Codespace](https://img.shields.io/badge/Codespace-_?style=plastic&logo=github&label=Spin-up%20a&labelColor=2f363d&color=24292e)](https://codespaces.new/mellolucas/resume?quickstart=1) and start coding right away in a full-featured development environment tailored to your needs
   - [![Open in GitHub.dev Web Editor](https://img.shields.io/badge/GitHub.dev-_?style=plastic&logo=refinedgithub&logoColor=white&label=Open%20in&labelColor=2f363d&color=24292e)](https://github.dev/mellolucas/resume) if you prefer a lightweight browser-based quick editing experience
   - [![Clone locally with VS Code](https://img.shields.io/badge/Clone_with-VS_Code-0098FF.svg?style=plastic&logo=git&logoColor=white)](https://vscode.dev/redirect?url=vscode%3A%2F%2Fvscode.git%2Fclone%3Furl%3Dhttps%3A%2F%2Fgithub.com%2Fmellolucas%2Fresume) to work offline from your good-old and trusty IDE
   - [![Clone locally with VS Code Insiders](https://img.shields.io/badge/Clone_with-VS_Code_Insiders-24bfa5.svg?style=plastic&logo=gitforwindows&logoColor=white)](https://vscode.dev/redirect?url=vscode-insiders%3A%2F%2Fvscode.git%2Fclone%3Furl%3Dhttps%3A%2F%2Fgithub.com%2Fmellolucas%2Fresume) to work offline from your good-new and oftentimes-trusty IDE
   - [![Download ZIP](https://img.shields.io/badge/%E2%BF%BB_Download-ZIP-_.svg?color=yellow&style=plastic)](/../../archive/refs/heads/main.zip) and upload to [Overleaf](https://www.overleaf.com/) if you just don't want the hassle. If versioning is not your thing, you could just skip the whole GitHub part and download mine and go live your best life... who needs version control anyway? Yeah, c'mon! To live is to risk it all! Otherwise you’re just an inert chunk of randomly assembled molecules drifting wherever the universe blows you!!

5. <todo from here>

<!-- maybe use https://vscode.dev/redirect?url=<encoded-vscode-protocol-link> -->

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
│   ├── ~~projects.tex      # Notable projects (optional)~~
│   ├── experience/       # Individual job entries (YYYYMMDD-company-level-title-role.tex)
│   └── ~~projects/         # Individual project entries (YYYYMMDD-title.tex)~~
└── .github/
    └── workflows/
        ├── ~~_repo-self-setup.yaml # Initial repository configuration workflow (on fork)~~
        ├── ~~analysis.yaml # Static code analysis workflow~~
        ├── ~~build.yaml    # Compilation and PDF generation workflow~~
        └── ~~publish.yaml  # Publish generated content to target media and PDF to GitHub Releases~~

```

## Usage

1.  [Fork](https://github.com/mellolucas/resume/fork) this repository
2.  ## Open the forked repository with your editor of choice:

- [Open in GitHub Codespaces](https://codespaces.new/mellolucas/resume)

## Building

Compile with any LaTeX engine:

```bash
# pdfLaTeX (recommended for ATS compatibility)
pdflatex main.tex

# LuaLaTeX or XeLaTeX (for advanced font features)
lualatex main.tex
xelatex main.tex
```

### Using Overleaf

1. Create a new project (e.g., "resume-my-name") on [Overleaf](https://www.overleaf.com/)
2. Download your

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

</details>
