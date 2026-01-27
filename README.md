<!-- prettier-ignore -->
<div style="display: flex; justify-content: space-between; align-items: center;">
    <span>
        <!-- <a id="workflow-repo-self-setup" href="/../../actions/workflows/_repo-self-setup.yaml">
            <img src="/../../actions/workflows/_repo-self-setup.yaml/badge.svg"/>
        </a>
        <a id="workflow-build" href="/../../actions/workflows/build.yaml">
            <img src="/../../actions/workflows/build.yaml/badge.svg"/>
        </a>
        <a id="workflow-publish" href="/../../actions/workflows/publish.yaml">
            <img src="/../../actions/workflows/publish.yaml/badge.svg"/>
        </a> -->
    </span>
    <span>
        <a id="stars" href="https://github.com/mellolucas/resume/stargazers">
            <img src="https://img.shields.io/github/stars/mellolucas/resume"/>
        </a>
        &nbsp;
        <a id="subscription" href="https://github.com/mellolucas/resume/subscription">
            <img src="https://img.shields.io/github/watchers/mellolucas/resume"/>
        </a>
    </span>
    <span>
        <img src="https://img.shields.io/badge/-LaTeX-008080?style=flat&logo=latex&logoColor=white"/>
    </span>
</div>
<br>
<div align="center">

<!-- <img src="./packages/webapp/public/favicon.png" alt="" align="center" height="64" /> -->

# Resume

[![use this template](https://img.shields.io/badge/%F0%9F%93%A0_Use_this_-Template-_.svg?color=008000&style=for-the-badge)](https://github.com/new?template_owner=mellolucas&template_name=resume&owner=%40me&name=resume&description=Curriculum%20VitAI&prompt=placeholder-use-custom-agent)
[![Kickstart in Overleaf](https://img.shields.io/badge/Overleaf-_?style=for-the-badge&logo=overleaf&logoColor=white&label=Kickstart%20in&color=47A141)](https://www.overleaf.com/docs?snip_uri=https%3A%2F%2Fgithub.com%2Fmellolucas%2Fresume%2Farchive%2Frefs%2Fheads%2Fmain.zip&snup_name=resume)

<br>

:star: If you find this project useful, star it on GitHub, and subscribe for updates!

[See what it dows](/../../main?tab=readme-ov-file) • [Create your own](#create-your-own) • [Understand the structure](#structure) • [Get help](#getting-help) • [Contribute](#contributing)

![Animation showing the resume being compiled](./docs/images/demo.gif)

A modular, ATS-friendly LaTeX resume with reusable commands, clean defaults, and a ready-to-ship structure for fast customization.

> [!TIP]
> You can test this application locally without any cost using [Ollama](https://ollama.com/). Follow the instructions in the [Local Development](#local-development) section to get started.

</div>

## Features

todo

## Create Your Own

1. Decide where your resume project will live:

   [![Create a new repository from this template](https://img.shields.io/badge/%F0%9F%93%A0_Start_a_new_repo_from_this_-Template-_.svg?color=008000&style=plastic)](https://github.com/new?template_owner=mellolucas&template_name=resume&owner=%40me&name=resume&description=Curriculum%20VitAI&prompt=placeholder-use-custom-agent)
   [![Kickstart a new project in Overleaf](https://img.shields.io/badge/Overleaf-_?style=flat&logo=overleaf&logoColor=white&label=Kickstart%20a%20new%20project%20in&color=47A141)](https://www.overleaf.com/docs?snip_uri=https%3A%2F%2Fgithub.com%2Fmellolucas%2Fresume%2Farchive%2Frefs%2Fheads%2Fmain.zip&snup_name=resume)
   [![Download source code as ZIP](https://img.shields.io/badge/%E2%BF%BB_Download_source_code_as-ZIP-_.svg?color=yellow&style=flat-square)](/../../archive/refs/heads/main.zip)

2. If you picked the GitHub option, review the pre-filled details at the creation prompt, then click on `Create repository` at the bottom of the page. Then, wait until [GitHub Actions](/../../actions/workflows/_repo-self-setup.yaml) set things up for you (takes less than a minute! Refresh the page to check the status)
3. Open your project in your editor of choice:
<details>
    <summary><strong>
        <a id="github-codespaces" href="https://codespaces.new/mellolucas/resume?quickstart=1">
            <img src="https://img.shields.io/badge/Codespace-_?style=plastic&logo=github&label=Spin-up%20a&labelColor=2f363d&color=24292e"/>
        </a>
    </summary>
    Start coding right away in a full-featured development environment tailored to your needs
</details>
<details>
    <summary><strong>
        <a id="github-dev" href="https://github.dev/mellolucas/resume">
            <img src="https://img.shields.io/badge/GitHub.dev-_?style=plastic&logo=refinedgithub&logoColor=white&label=Open%20in&labelColor=2f363d&color=24292e"/>
        </a>
    </summary>
    If you prefer a lightweight browser-based quick editing experience
</details>
<details>
    <summary><strong>
        <a id="vscode" href="https://vscode.dev/redirect?url=vscode%3A%2F%2Fvscode.git%2Fclone%3Furl%3Dhttps%3A%2F%2Fgithub.com%2Fmellolucas%2Fresume">
            <img src="https://img.shields.io/badge/Clone_with-VS_Code-0098FF.svg?style=plastic&logo=git&logoColor=white"/>
        </a>
    </summary>
    To work offline from your good-old and trusty IDE
</details>
<details>
    <summary><strong>
        <a id="vscode-insiders" href="https://vscode.dev/redirect?url=vscode-insiders%3A%2F%2Fvscode.git%2Fclone%3Furl%3Dhttps%3A%2F%2Fgithub.com%2Fmellolucas%2Fresume">
            <img src="https://img.shields.io/badge/Clone_with-VS_Code_Insiders-24bfa5.svg?style=plastic&logo=gitforwindows&logoColor=white"/>
        </a>
    </summary>
    To work offline from your good-new and oftentimes-trusty IDE
</details>

<!-- TODO: in hindsight, a better option is nesting under each "clone/copy/start" option and then guide the user mentioning only the relevant steps and options for the chosen method -->

<details><summary><strong>🏗️ Work in Progress 🚧</strong></summary>

## Features

- [x] **ATS-Friendly**: Single-column layout, standard section headers, Unicode-compliant PDF output
- [x] **Modular Structure**: Separate files for sections, constants, and reusable commands
- [x] **Multi-Engine Support**: Works with pdfLaTeX, LuaLaTeX, and XeLaTeX
- [x] **PDF Metadata**: Automatic title, author, and keywords for search engines and accessibility
- [ ] **GitHub Actions**: Automated PDF generation on push

## Create Your Own Resume

5. <todo from here>

## Create Your Own Resume

1. [![Start from this template](https://img.shields.io/badge/%F0%9F%93%A0_Start_from_this_-Template-_.svg?color=008000&style=flat)](https://github.com/new?template_owner=mellolucas&template_name=resume&owner=%40me&name=resume&description=Curriculum%20VitAI&prompt=placeholder-use-custom-agent) to create a new repository for your resume project. Unless you don't want to, then you can just skip to step 3's last option.
2. At the creation prompt, after reviewing the pre-filled details, click on `Create repository` at the bottom of the page.
3. Wait until [GitHub Actions](/../../actions/workflows/_repo-self-setup.yaml) set things up for you (takes less than a minute! Refresh the page to check the status)
4. Open your project in your editor of choice:
   - [![Spin-up a Codespace](https://img.shields.io/badge/Codespace-_?style=plastic&logo=github&label=Spin-up%20a&labelColor=2f363d&color=24292e)](https://codespaces.new/mellolucas/resume?quickstart=1) and start coding right away in a full-featured development environment tailored to your needs
   - [![Open in GitHub.dev Web Editor](https://img.shields.io/badge/GitHub.dev-_?style=plastic&logo=refinedgithub&logoColor=white&label=Open%20in&labelColor=2f363d&color=24292e)](https://github.dev/mellolucas/resume) if you prefer a lightweight browser-based quick editing experience
   - [![Clone locally with VS Code](https://img.shields.io/badge/Clone_with-VS_Code-0098FF.svg?style=plastic&logo=git&logoColor=white)](https://vscode.dev/redirect?url=vscode%3A%2F%2Fvscode.git%2Fclone%3Furl%3Dhttps%3A%2F%2Fgithub.com%2Fmellolucas%2Fresume) to work offline from your good-old and trusty IDE
   - [![Clone locally with VS Code Insiders](https://img.shields.io/badge/Clone_with-VS_Code_Insiders-24bfa5.svg?style=plastic&logo=gitforwindows&logoColor=white)](https://vscode.dev/redirect?url=vscode-insiders%3A%2F%2Fvscode.git%2Fclone%3Furl%3Dhttps%3A%2F%2Fgithub.com%2Fmellolucas%2Fresume) to work offline from your good-new and oftentimes-trusty IDE
   - [![Upload as a Project to Overleaf](https://img.shields.io/badge/Overleaf-_?style=flat&logo=overleaf&logoColor=white&label=Upload%20as%20a%20Project%20in&color=47A141)](https://www.overleaf.com/docs?snip_uri=https%3A%2F%2Fgithub.com%2Fmellolucas%2Fresume%2Farchive%2Frefs%2Fheads%2Fmain.zip&snup_name=resume)
   - [![Download ZIP](https://img.shields.io/badge/%E2%BF%BB_Download-ZIP-_.svg?color=yellow&style=plastic)](/../../archive/refs/heads/main.zip) if you just don't want the hassle. If versioning is not your thing, you could just skip the whole GitHub part and download mine and go live your best life... who needs version control anyway? Yeah, c'mon! To live is to risk it all! Otherwise you’re just an inert chunk of randomly assembled molecules drifting wherever the universe blows you!!

5. <todo from here>

<!-- later use https://vscode.dev/redirect?url=<encoded-vscode-protocol-link> -->

other options:

<details>
    <summary>
        <a id="latex-test" href="https://www.overleaf.com/docs?snip_uri=https%3A%2F%2Fgithub.com%2Fmellolucas%2Fresume%2Farchive%2Frefs%2Fheads%2Fmain.zip&snup_name=resume">
            <img src="https://img.shields.io/badge/-LaTeX-008080?style=flat&logo=latex&logoColor=white"/>
         </a>
    </summary>
[![⭐+1](https://img.shields.io/badge/%2B1-_?style=social&label=%E2%AD%90)](https://github.com/mellolucas/resume)
[![🔔 Subscribe](https://img.shields.io/badge/🔔-blue?style=social&logoColor=white)]()

</details>

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
