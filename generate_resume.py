#!/usr/bin/env python3
"""
Resume Generator

This script generates a LaTeX resume from YAML data files.
It merges data/default.yaml with optional override files like data/resume.yaml.
"""

import argparse
import os
import sys
import yaml
from pathlib import Path
from typing import Any, Dict, List, Union
from jinja2 import Environment, FileSystemLoader, Template
import re


class ResumeGenerator:
    def __init__(self, data_dir: str = "data", template_dir: str = "templates"):
        self.data_dir = Path(data_dir)
        self.template_dir = Path(template_dir)
        
    def load_yaml_file(self, file_path: Path) -> Dict[str, Any]:
        """Load YAML file and return parsed data."""
        if not file_path.exists():
            return {}
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file {file_path}: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            sys.exit(1)
    
    def deep_merge_dicts(self, base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recursively merge two dictionaries, with override values taking precedence.
        Lists in override completely replace lists in base.
        """
        result = base.copy()
        
        for key, value in override.items():
            if key in result:
                if isinstance(result[key], dict) and isinstance(value, dict):
                    result[key] = self.deep_merge_dicts(result[key], value)
                else:
                    # For lists and other types, override completely replaces base
                    result[key] = value
            else:
                result[key] = value
        
        return result
    
    def load_and_merge_data(self, target: str = "resume") -> Dict[str, Any]:
        """
        Load default.yaml and merge with target-specific override file.
        
        Args:
            target: Target platform/resource name (e.g., "resume", "linkedin")
        
        Returns:
            Merged data dictionary
        """
        # Load default data
        default_file = self.data_dir / "default.yaml"
        if not default_file.exists():
            print(f"Error: {default_file} does not exist. This file is required.")
            sys.exit(1)
        
        default_data = self.load_yaml_file(default_file)
        
        # Load override data if it exists
        override_file = self.data_dir / f"{target}.yaml"
        override_data = self.load_yaml_file(override_file)
        
        # Merge data
        merged_data = self.deep_merge_dicts(default_data, override_data)
        
        print(f"Loaded data from {default_file}")
        if override_file.exists():
            print(f"Applied overrides from {override_file}")
        
        return merged_data
    
    def markdown_to_latex(self, text: str) -> str:
        """
        Convert basic markdown formatting to LaTeX.
        Supports: **bold**, *italic*, [link text](url)
        """
        if not isinstance(text, str):
            return str(text)
        
        # Convert **bold** to \textbf{bold}
        text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', text)
        
        # Convert *italic* to \textit{italic}
        text = re.sub(r'\*(.*?)\*', r'\\textit{\1}', text)
        
        # Convert [text](url) to \href{url}{text}
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\\href{\2}{\1}', text)
        
        return text
    
    def process_data_for_latex(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process data to convert markdown formatting to LaTeX.
        """
        def process_value(value):
            if isinstance(value, str):
                return self.markdown_to_latex(value)
            elif isinstance(value, dict):
                return {k: process_value(v) for k, v in value.items()}
            elif isinstance(value, list):
                return [process_value(item) for item in value]
            else:
                return value
        
        return process_value(data)
    
    def generate_resume(self, target: str = "resume", output_file: str = "resume.tex") -> None:
        """
        Generate LaTeX resume from YAML data.
        
        Args:
            target: Target platform/resource name
            output_file: Output LaTeX file path
        """
        # Load and merge data
        data = self.load_and_merge_data(target)
        
        # Process markdown formatting
        data = self.process_data_for_latex(data)
        
        # Setup Jinja2 environment
        env = Environment(
            loader=FileSystemLoader(self.template_dir),
            block_start_string='{%',
            block_end_string='%}',
            variable_start_string='{{',
            variable_end_string='}}',
            comment_start_string='{#',
            comment_end_string='#}'
        )
        
        # Load template
        template_file = f"{target}.tex.j2"
        template_path = self.template_dir / template_file
        
        # Fallback to resume template if target-specific template doesn't exist
        if not template_path.exists():
            template_file = "resume.tex.j2"
            template_path = self.template_dir / template_file
        
        if not template_path.exists():
            print(f"Error: Template {template_path} does not exist.")
            sys.exit(1)
        
        try:
            template = env.get_template(template_file)
        except Exception as e:
            print(f"Error loading template {template_file}: {e}")
            sys.exit(1)
        
        # Render template
        try:
            output = template.render(**data)
        except Exception as e:
            print(f"Error rendering template: {e}")
            sys.exit(1)
        
        # Write output
        output_path = Path(output_file)
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"Generated {output_path}")
        except Exception as e:
            print(f"Error writing output file {output_path}: {e}")
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Generate LaTeX resume from YAML data")
    parser.add_argument(
        "--target", 
        default="resume", 
        help="Target platform/resource name (default: resume)"
    )
    parser.add_argument(
        "--output", 
        default="resume.tex", 
        help="Output LaTeX file (default: resume.tex)"
    )
    parser.add_argument(
        "--data-dir", 
        default="data", 
        help="Data directory path (default: data)"
    )
    parser.add_argument(
        "--template-dir", 
        default="templates", 
        help="Template directory path (default: templates)"
    )
    
    args = parser.parse_args()
    
    generator = ResumeGenerator(args.data_dir, args.template_dir)
    generator.generate_resume(args.target, args.output)


if __name__ == "__main__":
    main()