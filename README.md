# Resume Generator

A YAML-based resume generation system that creates LaTeX resumes from structured data with support for platform-specific overrides.

## Overview

This system centralizes professional information in YAML files and generates customized resumes for different platforms (resume, LinkedIn, etc.). It uses a default data structure with optional override files to allow platform-specific customizations.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate a resume:**
   ```bash
   python3 generate_resume.py --target resume --output resume.tex
   ```

3. **Compile to PDF (requires LaTeX):**
   ```bash
   pdflatex resume.tex
   ```

## Data Structure

### Required Files

- `data/default.yaml` - Main source of truth containing all professional information
- `templates/resume.tex.j2` - Jinja2 template for LaTeX resume generation

### Optional Files

- `data/{target}.yaml` - Override files for specific platforms (e.g., `data/resume.yaml`, `data/linkedin.yaml`)

### Data Schema

The `default.yaml` file should contain the following root sections:

```yaml
personal:
  name: "Your Name"
  headline: "Your professional headline"
  company: "Current Company"
  location: "City, State"
  role:
    title: "Job Title"
    level: "Senior/Junior/etc"
    domain: "Domain Area"
  contacts:
    - name: "email"
      value: "email@example.com"
    - name: "portfolio"
      value: "https://yoursite.com"

skills:
  - category: "Programming Languages"
    items: ["Python", "Java", "JavaScript"]
  - category: "Frameworks"
    items: ["Django", "React"]

languages:
  - name: "English"
    level: "Native"

experience:
  - title: "Job Title"
    company: "Company Name"
    location: "City, State"
    startDate: "YYYY-MM"
    endDate: "Present"
    bullets:
      - "Achievement with **bold text** and *italic text*"

projects:
  - title: "Project Name"
    url: "https://github.com/user/project"
    bullets:
      - "Project description"

education:
  - degree: "Degree Name"
    school: "University Name"
    location: "City, State"
    graduationDate: "YYYY-MM"
```

## Features

### Markdown Support

The system supports basic markdown formatting in text fields:
- `**bold text**` → `\textbf{bold text}`
- `*italic text*` → `\textit{italic text}`
- `[link text](url)` → `\href{url}{link text}`

### Data Merging

Override files merge with the default data:
- Matching keys in override files replace values in default.yaml
- Lists are completely replaced (not merged)
- Nested dictionaries are recursively merged

### Example Override

Create `data/resume.yaml` to customize the resume version:

```yaml
personal:
  headline: "Resume-specific headline"

# Only show most relevant experience
experience:
  - title: "Senior Engineer"
    company: "Current Company"
    # ... abbreviated experience
```

## Command Line Usage

```bash
python3 generate_resume.py [options]

Options:
  --target TARGET       Target platform name (default: resume)
  --output OUTPUT       Output LaTeX file (default: resume.tex)
  --data-dir DIR        Data directory path (default: data)
  --template-dir DIR    Template directory path (default: templates)
```

## Examples

Generate different versions:
```bash
# Standard resume
python3 generate_resume.py --target resume --output resume.tex

# LinkedIn version (if data/linkedin.yaml exists)
python3 generate_resume.py --target linkedin --output linkedin.tex

# Custom output location
python3 generate_resume.py --target resume --output output/my_resume.tex
```

## File Structure

```
.
├── data/
│   ├── default.yaml      # Main data source
│   ├── resume.yaml       # Resume-specific overrides
│   └── linkedin.yaml     # LinkedIn-specific overrides (optional)
├── templates/
│   └── resume.tex.j2     # LaTeX template
├── generate_resume.py    # Main script
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Template Customization

The Jinja2 template in `templates/resume.tex.j2` can be customized to change the resume layout and styling. The template has access to all data from the merged YAML files.

## Troubleshooting

- Ensure all required fields are present in `default.yaml`
- Check YAML syntax if getting parsing errors
- Verify that template file exists in the templates directory
- For LaTeX compilation issues, ensure you have a complete LaTeX installation